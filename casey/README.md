# Casey Skills Control Plane

A versioned, testable capability layer for reusable agent skills.

## Purpose

This subtree converts recurring procedures, prompts, schemas, and tool disciplines into discoverable skills with explicit contracts. It is not a prompt dump and it is not an evidence store.

## Core Rules

1. One skill, one bounded capability.
2. Every skill declares inputs, outputs, trust requirements, failure modes, and exit criteria.
3. Skills may read source material but must not silently promote summaries, allegations, or inferences into facts.
4. Public skills contain no case facts, personal information, credentials, secrets, or private connector configuration.
5. Case-specific overlays belong in private control-plane repositories and reference these generic skills by identifier and version.
6. `Do It Again` means recursive material improvement with preserved validated intelligence, explicit deltas, and autonomous advancement when exit criteria are met.
7. Generated artifacts remain projections until their material assertions resolve to authoritative sources.
8. A complete schema or template is not complete evidence.
9. Connector availability does not determine connector authority.

## Layout

```text
casey/
├── docs/
│   └── NORTH_STAR_ARCHITECTURE.md
├── registry/
│   └── skills.yaml
├── schemas/
│   └── skill-manifest.schema.json
├── policies/
│   └── SECURITY.md
└── skills/
    ├── do-it-again/
    ├── memory-control-plane/
    ├── legal-fact-classifier/
    ├── evidence-provenance/
    ├── connector-registry/
    ├── mcp-stack-auditor/
    └── actor-violation-ledger/
```

## Initial Capability Spine

| Skill | Purpose | Risk |
|---|---|---|
| `casey.connector-registry` | Assign connector ownership, trust, permissions, and fallback behavior | high |
| `casey.mcp-stack-auditor` | Analyze stack overlap, unsafe writes, and consolidation priorities | high |
| `casey.memory-control-plane` | Normalize memory with provenance, case isolation, and supersession | high |
| `casey.evidence-provenance` | Preserve originals, hashes, derivation history, and chain of custody | critical |
| `casey.legal-fact-classifier` | Separate record facts, evidence, allegations, disputes, and inference | high |
| `casey.actor-violation-ledger` | Build evidence-gated actor accountability records | critical |
| `casey.do-it-again` | Recursively improve and advance between completed legs | medium |

## Skill Lifecycle

```text
experimental -> reviewed -> stable -> deprecated
```

Promotion requires:

- valid manifest;
- bounded scope;
- documented failure modes;
- deterministic acceptance checks where feasible;
- no secrets or private evidence;
- version and changelog entry;
- successful adversarial review.

## Public / Private Boundary

This repository stores portable, sanitized capability definitions. Private repositories store:

- case-specific facts and evidence;
- actor identities tied to active matters;
- credentials and connector secrets;
- private source locations;
- litigation strategy overlays;
- deployment configuration.

The public skill is the reusable engine. The private overlay supplies authorized context.
