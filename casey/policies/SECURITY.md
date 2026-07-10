# Security and Privacy Boundary

## Public Repository Rule

The `casey/` subtree is public and sanitized. It may contain reusable procedures, schemas, tests, and generic examples. It must not contain:

- names or identifiers tied to active private matters;
- court filings, evidence, exhibits, transcripts, or private timelines;
- home addresses, phone numbers, email addresses, medical information, or child information;
- API keys, tokens, cookies, credentials, private URLs, or connector secrets;
- privileged communications or private litigation strategy;
- hashes that reveal or unnecessarily fingerprint private evidence;
- production database identifiers or internal storage paths.

## Private Overlay Pattern

Private deployments should reference public skills by immutable identifier and version:

```yaml
skill_ref: casey.legal-fact-classifier@1.0.0
overlay: private://legal-control-plane/overlays/example-case.yaml
```

The overlay may provide authorized domain configuration, source mappings, identities, and case-specific constraints. The public skill remains reusable and contains no private payload.

## Write Safety

- Default to read-only.
- Require explicit authorization for external writes.
- Require human approval for destructive, public, legal, financial, or identity-affecting actions.
- Preserve an audit record containing the skill version, connector, action, target, timestamp, and result.
- Never log secrets or full sensitive payloads.

## Incident Rule

If sensitive content is committed:

1. stop further propagation;
2. revoke exposed credentials immediately;
3. remove the content from current history;
4. assess whether repository history must be rewritten;
5. record the incident in the private security log;
6. verify caches, forks, artifacts, and mirrors;
7. rotate affected identifiers or secrets;
8. add a regression test preventing recurrence.
