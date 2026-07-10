# Casey Skills North-Star Architecture

## Objective

Create a portable, versioned capability layer for agents operating across repositories, connectors, memory systems, evidence stores, and automation platforms.

The skills repository defines **how work must be performed**. It does not store private case facts, original evidence, credentials, or live connector configuration.

## Architecture

```text
Source Systems
  court records | evidence vault | repositories | email | Drive | Dropbox | Notion
        |
        v
Connector Control Plane
  registry | trust | permissions | health | audit | fallback | revocation
        |
        v
Memory and Evidence Control Plane
  identities | provenance | fact status | case isolation | contradictions | versions
        |
        v
Skill Router
  prerequisites | risk gates | authorization | execution | validation | handoff
        |
        v
Domain Skills
  legal analysis | evidence | repository operations | drafting | orchestration
        |
        v
Projections
  ledgers | timelines | motions | reports | dashboards | tasks
```

## First-Class Pillars

- orchestration
- memory
- evidence
- legal-analysis
- infrastructure
- repositories
- research
- drafting
- operations

Each pillar must declare:

- owned skills
- owned connectors
- trust requirements
- permitted side effects
- source-of-truth boundaries
- escalation path
- failure behavior

## Three-Layer Connector Model

### 1. Interface Layer

Normalized capability contracts such as search, read, write, execute, publish, and notify.

### 2. Governance Layer

Ownership, trust, authorization, audit logging, rate limits, health, fallback, and revocation.

### 3. Provider Layer

GitHub, Google Drive, Dropbox, Notion, databases, sandboxes, local filesystem, and other concrete providers.

Agents route through capability contracts and governance. They do not select a provider merely because it is available.

## Source-of-Truth Rule

Every data class has one canonical owner. Other systems may hold caches, indexes, projections, or working copies, but they must record their relationship to the canonical source.

## Public and Private Split

### Public Skills Repository

- generalized skill instructions
- schemas
- sanitized examples
- validation rules
- test fixtures without private data
- governance documentation

### Private Overlay

- case identifiers and facts
- evidence locations and hashes
- private repositories and endpoints
- credentials and tokens
- privileged strategy
- personal information
- live connector scopes

## Routing Sequence

1. Classify the request and domain.
2. Determine factual and operational risk.
3. Resolve required sources and connectors.
4. Verify trust, permissions, and case boundary.
5. Load the smallest sufficient skill set.
6. Execute with provenance and audit capture.
7. Validate outputs against exit criteria.
8. Invoke the Do It Again protocol when material defects remain.
9. Advance to the next leg when the current leg stabilizes.

## Primary Failure Modes

- connector proliferation without ownership
- multiple systems claiming canonical status
- generated summaries promoted to facts
- case-number or procedural-track contamination
- write-capable agents operating without authorization
- silent fallback to an unsafe provider
- public repository leakage of private data
- complete-looking templates mistaken for complete evidence
- endless refinement without phase advancement

## Initial Skill Spine

1. `casey.connector-registry`
2. `casey.mcp-stack-auditor`
3. `casey.memory-control-plane`
4. `casey.evidence-provenance`
5. `casey.legal-fact-classifier`
6. `casey.actor-violation-ledger`
7. `casey.do-it-again`

This sequence establishes control before expansion.