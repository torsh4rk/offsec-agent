"""Explicitly synthetic bank/brokerage API: localhost-only, no real financial data."""
from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

PATHS = {
    "/lab/accounts/acct-alice": ("alice", "account", {"account": "acct-alice", "balance": "1250.10", "currency": "USD"}),
    "/lab/portfolios/portfolio-alice": ("alice", "portfolio", {"portfolio": "portfolio-alice", "equity": "9250.00"}),
    "/lab/orders/order-alice": ("alice", "order", {"order": "order-alice", "symbol": "TEST", "status": "filled"}),
    "/lab/kyc/kyc-alice": ("alice", "kyc", {"record": "synthetic-kyc-alice", "status": "verified"}),
    "/lab/admin/reconciliation": ("admin", "admin", {"report": "synthetic-reconciliation"}),
}


def handler_class(simulate_bola: bool = False, simulate_bfla: bool = False,
                  simulate_cache: bool = False):
    class DemoHandler(BaseHTTPRequestHandler):
        server_version = "SyntheticFinancialLab/0.1"

        def do_GET(self):
            parsed = urlsplit(self.path)
            # Never reflect arbitrary request paths or query data.
            path = parsed.path
            actor = self.headers.get("X-Demo-Actor", "anonymous")
            if path == "/lab/health":
                self.respond(200, {"status": "synthetic-lab-only"})
            elif path == "/lab/quotes/TEST":
                self.respond(200, {"symbol": "TEST", "price": "42.00"}, sensitive=False)
            elif path in PATHS:
                owner, category, record = PATHS[path]
                permitted = (actor == owner or actor == "admin")
                if category == "admin" and simulate_bfla:
                    permitted = True
                if category != "admin" and simulate_bola:
                    permitted = True
                if permitted:
                    self.respond(200, record, sensitive=True)
                else:
                    self.respond(403, {"error": "Forbidden"}, sensitive=True)
            else:
                self.respond(404, {"error": "Not found"})

        def respond(self, code, obj, sensitive=False):
            body = json.dumps(obj, separators=(",", ":")).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("X-Content-Type-Options", "nosniff")
            if sensitive and not simulate_cache:
                self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, fmt, *args):
            return  # Avoid recording simulated account data and request headers.

    return DemoHandler


def serve(port: int, simulate_bola=False, simulate_bfla=False, simulate_cache=False):
    if not 1024 <= port <= 65535:
        raise ValueError("Port must be 1024–65535")
    with ThreadingHTTPServer(("127.0.0.1", port), handler_class(simulate_bola, simulate_bfla, simulate_cache)) as srv:
        print(f"Synthetic financial lab listening on http://127.0.0.1:{port} (CTRL+C to stop)", flush=True)
        srv.serve_forever(poll_interval=0.25)


def main():
    ap = argparse.ArgumentParser(description="Start a synthetic, localhost-only financial API")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--simulate-bola", action="store_true", help="Intentionally disable ownership checks in the LOCAL lab")
    ap.add_argument("--simulate-bfla", action="store_true", help="Intentionally disable admin role checks in the LOCAL lab")
    ap.add_argument("--simulate-cache", action="store_true", help="Intentionally omit no-store for LOCAL sensitive responses")
    a = ap.parse_args()
    serve(a.port, a.simulate_bola, a.simulate_bfla, a.simulate_cache)

if __name__ == "__main__":
    main()
