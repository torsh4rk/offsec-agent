---
name: docker-security
description: Assess authorized Docker hosts, images, registries, Compose deployments, daemon exposure, runtime isolation, and container-to-host trust boundaries.
license: MIT
compatibility: opencode,codex
metadata:
  domain: container-security
  platform: docker
  safety: authorized-only
---

# Docker Security

## Purpose

Evaluate Docker build, distribution, daemon, runtime, storage, and host boundaries with evidence-driven validation.

## Core workflow

1. Confirm hosts, daemons, registries, images, Compose projects, containers, accounts, and approved actions.
2. Collect read-only daemon configuration, socket exposure, container settings, mounts, capabilities, networks, secrets, images, and provenance.
3. Map trust boundaries among users, the Docker API, registries, containers, volumes, and the host.
4. Prioritize daemon exposure, privileged configurations, writable host resources, secret leakage, and supply-chain weaknesses.
5. Validate with inspection or a designated disposable test container when authorized.
6. Provide hardened Dockerfile, Compose, daemon, and runtime recommendations.

## Coverage

- Docker socket and remote API exposure, authorization plugins, rootless mode, user namespaces, and daemon TLS.
- Privileged mode, capabilities, seccomp, AppArmor/SELinux, devices, PID/IPC/network namespaces, and host mounts.
- Dockerfiles, build secrets, multi-stage builds, base images, tags/digests, SBOMs, signatures, registry access, and scanning.
- Compose secrets, environment variables, volumes, networks, health checks, resource limits, logging, and restart behavior.

## Evidence standard

Record host, daemon endpoint, container/image identifier, effective user, relevant configuration, expected isolation, observed state, timestamp, and scope reference. A privileged-looking setting is not a demonstrated escape without an authorized, minimal proof of crossed trust boundary.

## Approval boundaries

- Inspection and static image/configuration review are the default.
- Container creation, exec, host mounts, daemon writes, image pushes, registry changes, secret reads, escape attempts, privilege escalation, or host modification require explicit approval.
- Never stop, restart, remove, or alter production containers or images without a change window.

## Deliverables

- Daemon and runtime exposure map.
- Image and build-security review.
- Container-to-host boundary findings.
- Hardened configuration and retest checklist.
