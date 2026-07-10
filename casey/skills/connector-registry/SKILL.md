---
name: connector-registry
description: Register connectors as domain-owned capabilities with explicit trust, permissions, data boundaries, write policies, health, and failure behavior.
---

# Connector Registry

## Objective

Replace an unstructured connector collection with a controlled capability registry. Connector availability does not imply authorization, factual reliability, or permission to write.

## Required Declaration

Each connector must declare:

- connector identifier and provider;
- owning pillar or domain;
- trust level: `safe`, `external`, `system`, or `untrusted`;
- supported capabilities;
- authentication mode;
- read and write scopes;
- canonical data types;
- prohibited data types;
- rate and concurrency limits;
- health-check method;
- idempotency behavior;
- retry and backoff policy;
- audit-log destination;
- failure and fallback behavior;
- human-approval requirements.

## Procedure

1. Inventory the connector and verify actual capabilities.
2. Assign one domain owner and any secondary consumers.
3. Apply least-privilege permissions.
4. Separate read, create, update, delete, and administrative capabilities.
5. Define what the connector may treat as canonical.
6. Define write boundaries and approval gates.
7. Test authentication, health, pagination, rate limits, and failure responses.
8. Record connector version and configuration fingerprint without storing secrets.
9. Route every invocation through auditable policy checks.
10. Quarantine connectors with unknown ownership, excessive scope, or unhandled failure modes.

## Prohibitions

- No secrets in source control.
- No silent fallback from a canonical source to a lower-trust source.
- No automatic destructive writes without explicit authorization and audit logging.
- No treating connector trust as evidentiary status.
- No connector may own the same canonical data type without a conflict-resolution rule.

## Required Output

Return a normalized registry entry, scope findings, security findings, health status, unresolved risks, and recommended remediation.

## Exit Criteria

The connector leg is complete when every active connector has an owner, trust level, explicit capability scope, write policy, audit path, and tested failure behavior.