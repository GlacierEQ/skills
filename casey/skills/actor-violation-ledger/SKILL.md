---
name: actor-violation-ledger
description: Build an actor-by-actor legal accountability ledger without converting allegations or template theories into established facts.
version: 1.0.0
risk: critical
---

# Actor Violation Ledger

## Purpose

Create a structured analytical ledger linking actors, conduct, sources, legal duties, disputed propositions, harm, and potential remedies while preserving evidentiary status and case boundaries.

## Inputs

- Case identifier and procedural track
- Authenticated filings and orders
- Docket metadata and notices
- Evidence items with provenance
- Party allegations and declarations
- Verified legal authorities
- Existing actor and event registries

## Required Classifications

Every proposition must be labeled as exactly one of:

- established_record_fact
- authenticated_evidence
- party_allegation
- disputed_fact
- inference
- verification_target
- strategic_recommendation

## Actor Record

Each actor entry must include:

- canonical actor ID and role
- case-specific capacity
- alleged act or omission
- date or bounded time range
- supporting source IDs and pinpoint locations
- contradicting or qualifying sources
- duty or authority implicated
- legal theory status: candidate, researched, verified, rejected
- causation status
- harm or prejudice status
- immunity, privilege, jurisdiction, and procedural barriers
- missing evidence
- court-safe formulation
- prohibited overstatement

## Governing Rules

- A pre-structured theory is not evidence.
- Empty fields remain empty; never fabricate factual completion.
- Statutes and cases must be independently verified before use.
- Criminal labels, fraud, conspiracy, kidnapping, corruption, bias, and intentional misconduct require element-by-element support and must not be inferred from irregularity alone.
- Keep separate cases and procedural tracks separate even when actors overlap.
- Record exculpatory, contradictory, and mitigating evidence.
- Distinguish conduct by a person from conduct attributable to an institution.
- Identify immunity and jurisdictional barriers before recommending escalation.

## Mandatory Output

- Actor ledger
- Source-to-claim matrix
- Element and authority matrix
- Contradiction register
- Evidentiary-gap list
- Safe findings supported by the present record
- Claims not presently supportable
- Recommended verification steps

## Exit Criteria

The ledger is ready for downstream drafting only when every material accusation has a provenance path, classification, verified legal predicate, contradiction review, and explicit confidence boundary.