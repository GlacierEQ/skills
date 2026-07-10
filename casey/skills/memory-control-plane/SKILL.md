---
name: memory-control-plane
description: Normalize durable memories into domain-owned, provenance-linked, versioned records with explicit trust, certainty, contradiction, and supersession status.
---

# Memory Control Plane

## Objective

Convert fragmented notes, summaries, files, and system memories into a controlled registry without erasing uncertainty or mixing unrelated domains.

## Core Model

Every durable memory must declare:

- canonical identifier;
- owning domain;
- memory type;
- source and provenance;
- connector trust;
- evidentiary or certainty status;
- actors and entities;
- temporal scope;
- contradiction links;
- supersession status;
- review status.

Connector trust and factual certainty are independent. A trusted database can store an unverified allegation. An external source can contain an authenticated official record.

## Procedure

1. Identify the source object and preserve its original form.
2. Assign the correct domain and enforce domain isolation.
3. Extract candidate assertions without promoting them to facts.
4. Classify each assertion as established fact, authenticated evidence, allegation, disputed fact, inference, verification target, recommendation, or generated summary.
5. Link actors, events, filings, evidence, authorities, and requested relief through stable identifiers.
6. Detect duplicates and near-duplicates.
7. Preserve contradictions as first-class records.
8. Apply source precedence without deleting lower-precedence records.
9. Mark incorrect or stale memories as deprecated or superseded; do not silently erase them.
10. Publish only reviewed records into canonical memory.

## Prohibitions

- No mixed case numbers or domain contamination.
- No summary-to-fact promotion.
- No last-write-wins resolution of conflicting evidence.
- No silent deletion.
- No use of vector embeddings as the source of truth.
- No private evidence or credentials in public registries.

## Output

Return normalized memory records, duplicate clusters, contradiction records, unresolved verification targets, and a migration delta.

## Exit Criteria

The leg is complete when every retained memory has a domain owner, provenance, classification, canonical identifier, and explicit conflict or supersession status.