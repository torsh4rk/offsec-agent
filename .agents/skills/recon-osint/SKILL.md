---
name: recon-osint
description: Perform authorized OSINT and attack-surface discovery with strict scope control, provenance tracking, deduplication, and passive-first validation.
license: MIT
compatibility: opencode,codex
metadata:
  domain: reconnaissance
  safety: authorized-only
---

# Recon and OSINT

## Purpose

Map the externally observable attack surface of an explicitly authorized organization, product, domain, or lab before active testing.

## Core workflow

1. Read `AGENTS.md` and the engagement scope.
2. Normalize root domains, subsidiaries, brands, CIDRs, cloud tenants, mobile packages, repositories, and exclusions.
3. Prefer passive sources before DNS resolution, HTTP probing, or port scanning.
4. Record source, timestamp, confidence, ownership evidence, and scope decision for every asset.
5. Deduplicate aliases and separate discovered, verified, in-scope, out-of-scope, and uncertain assets.
6. Produce a prioritized surface map for the relevant testing Skills.

## Coverage

- Domain, subdomain, certificate-transparency, DNS, ASN, CIDR, and service discovery.
- Public repositories, package registries, mobile applications, API schemas, documentation, and archived endpoints.
- Cloud-hosting indicators, third-party dependencies, exposed administration surfaces, and technology fingerprints.
- Organization-owned assets only; do not investigate private individuals or unrelated infrastructure.

## Evidence standard

For every asset, preserve the discovery source, resolution result, HTTP/service observation, ownership rationale, confidence, and final scope status. A hostname discovered by keyword similarity alone is not considered owned or authorized.

## Approval boundaries

- Passive collection is preferred and must respect source terms and privacy law.
- Active DNS brute force, HTTP probing, port scanning, screenshots, or crawling must match the engagement rate limit.
- Do not bypass access controls, purchase leaked data, use stolen credentials, perform social engineering, or enumerate personal information unrelated to the assessment.
- Redirects, shared hosting, SaaS tenants, CDNs, and third-party integrations remain out of scope until ownership is verified.

## Deliverables

- Asset inventory with provenance and confidence.
- Scope-decision log.
- Technology and exposure summary.
- Prioritized handoff to Web/API, Cloud, Mobile, MCP, or other applicable Skills.
