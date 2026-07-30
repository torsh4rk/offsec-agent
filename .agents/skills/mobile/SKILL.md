---
name: mobile
description: Authorized Android and iOS assessment aligned with MASVS/MASTG, covering static review, dynamic analysis, client trust boundaries, and backend authorization.
license: MIT
compatibility: opencode,codex
---

# Mobile Security

## Workflow

1. Record exact package, version, build, device, OS, and test account.
2. Perform static review before instrumentation.
3. Map components, permissions, entitlements, deep links, intents, URL schemes, WebViews, storage, and cryptographic use.
4. Capture baseline network traffic and map features to backend endpoints.
5. Use reversible instrumentation only on owned or explicitly authorized devices.
6. Validate backend impact separately from client-side bypasses.

## Checks

- Exported components and unsafe IPC.
- Sensitive local storage, logs, backups, clipboard, and screenshots.
- Certificate validation and network-security configuration.
- WebView bridges, JavaScript exposure, and file access.
- Biometric fallback, key invalidation, and session handling.
- Deep-link and URL-scheme validation.
- Backend authorization, device binding, and replay protection.

## Approval boundaries

Do not target third-party accounts, stores, production push infrastructure, or unrelated backend services. Avoid state-changing bypasses and never treat root/jailbreak-detection bypass as proof of backend compromise.
