"""Bounded, localhost-only financial API authorization/security checks."""
from __future__ import annotations

import http.client
import ipaddress
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

CASES = (
    ("BOLA-ACCOUNT", "/lab/accounts/acct-alice", "bob", 403, "CWE-639", "Account ownership boundary"),
    ("BOLA-PORTFOLIO", "/lab/portfolios/portfolio-alice", "bob", 403, "CWE-639", "Brokerage portfolio ownership"),
    ("BOLA-ORDER", "/lab/orders/order-alice", "bob", 403, "CWE-639", "Trade/order ownership"),
    ("BOLA-KYC", "/lab/kyc/kyc-alice", "bob", 403, "CWE-639", "KYC data ownership"),
    ("BFLA-ADMIN", "/lab/admin/reconciliation", "alice", 403, "CWE-862", "Administrative function authorization"),
)

class ScopeError(ValueError):
    pass


def validate_scope(scope: dict) -> dict:
    if not isinstance(scope, dict):
        raise ScopeError("Engagement must be a JSON object")
    if scope.get("authorization") != "I_OWN_THIS_SYNTHETIC_LAB" or scope.get("environment") != "local-synthetic-lab":
        raise ScopeError("A signed financial authorization is not modeled; only the explicitly owned synthetic lab is accepted")
    if not re.fullmatch(r"LAB-[A-Za-z0-9-]{4,48}", str(scope.get("engagement_id", ""))):
        raise ScopeError("An explicit LAB- engagement ID is required")
    if scope.get("allowed_host") != "127.0.0.1" or scope.get("max_requests") not in (10, 12):
        raise ScopeError("Only 127.0.0.1 and bounded 10/12 request profiles are accepted")
    expires = scope.get("expires_at")
    try:
        end = datetime.fromisoformat(str(expires).replace("Z", "+00:00"))
    except ValueError as exc:
        raise ScopeError("expires_at must be an ISO-8601 timestamp") from exc
    if end.tzinfo is None or end <= datetime.now(timezone.utc):
        raise ScopeError("Authorization expired or timezone missing")
    return scope


def load_scope(path: Path) -> dict:
    return validate_scope(json.loads(path.read_text(encoding="utf-8")))


def parse_target(target: str) -> int:
    try:
        u = urlsplit(target)
        if u.scheme != "http" or u.hostname != "127.0.0.1" or not u.port:
            raise ScopeError("Refusing target: only http://127.0.0.1:<port> is allowed")
        if u.username or u.password or u.path not in ("", "/") or u.query or u.fragment:
            raise ScopeError("Target may not contain userinfo, path, query, or fragment")
        if not 1024 <= u.port <= 65535:
            raise ScopeError("Port out of allowed range")
        if ipaddress.ip_address(u.hostname) != ipaddress.ip_address("127.0.0.1"):
            raise ScopeError("Non-loopback host is forbidden")
        return u.port
    except ValueError as exc:
        if isinstance(exc, ScopeError):
            raise
        raise ScopeError("Invalid target URL") from exc


def fetch(port: int, path: str, actor: str) -> tuple[int, dict[str, str]]:
    """Fixed paths, GET only, no redirects, no proxies, no customer response bodies."""
    if not path.startswith("/lab/") or not re.fullmatch(r"/lab/[A-Za-z0-9/_-]+", path):
        raise ScopeError("Unsafe path")
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
    try:
        conn.request("GET", path, headers={"X-Demo-Actor": actor, "Accept": "application/json",
                                                "User-Agent": "TORSh4rk-Financial-Lab/0.1"})
        resp = conn.getresponse()
        # Do not persist data; discard the small capped demo body.
        resp.read(8192)
        return resp.status, {k.lower(): v for k, v in resp.getheaders()}
    finally:
        conn.close()


def finance_scan(scope: dict, target: str) -> dict:
    scope = validate_scope(scope)
    port = parse_target(target)
    if scope["max_requests"] < len(CASES) + 3:
        raise ScopeError("Engagement request limit is too low for this fixed 8-request profile")
    findings = []
    checks = []
    # 5 unauthorized GETs + 2 authorized GETs + health = 8 requests.
    for test_id, path, actor, expected, cwe, label in CASES:
        code, _ = fetch(port, path, actor)
        good = code == expected
        checks.append({"test": test_id, "observed_status": code, "expected_status": expected,
                       "outcome": "pass" if good else "review"})
        if not good:
            findings.append({"id": test_id, "title": f"Potential authorization control failure: {label}",
                             "cwe": cwe, "severity": "high", "observed_status": code,
                             "expected_status": expected, "evidence": "Synthetic identity and fixed local GET path",
                             "limitations": "Lab evidence only; confirm underlying authorization logic"})
    for path, actor, tag in [
        ("/lab/accounts/acct-alice", "alice", "ACCOUNT-CACHE"),
        ("/lab/portfolios/portfolio-alice", "alice", "PORTFOLIO-CACHE"),
    ]:
        code, headers = fetch(port, path, actor)
        caching = "no-store" in headers.get("cache-control", "").lower()
        checks.append({"test": tag, "observed_status": code, "cache_no_store": caching,
                       "outcome": "pass" if code == 200 and caching else "review"})
        if code != 200 or not caching:
            findings.append({"id": tag, "title": "Synthetic sensitive response lacks required no-store caching policy",
                             "cwe": "CWE-525", "severity": "medium", "observed_status": code,
                             "limitations": "Local laboratory assumption; manual review required"})
    code, _ = fetch(port, "/lab/health", "anonymous")
    checks.append({"test": "HEALTH", "observed_status": code, "outcome": "pass" if code == 200 else "review"})
    return {"version": "0.1.0", "engagement_id": scope["engagement_id"],
            "target": target, "environment": "synthetic-local-only", "request_count": len(checks),
            "summary": {"checks": len(checks), "findings": len(findings)},
            "findings": findings, "checks": checks,
            "limitations": ["No live banking or brokerage targets", "Only fixed read-only local endpoints",
                            "X-Demo-Actor is a synthetic identity fixture, not real authentication",
                            "Status code signals are not proof of impact"]}
