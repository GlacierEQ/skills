---
name: evidence-provenance
description: Preserve original evidence, hashes, derivatives, chain of custody, extraction lineage, and citation-ready proof paths.
---

# Evidence Provenance

## Objective

Create a defensible lineage from an original source object to every derivative, extraction, assertion, and generated artifact that relies on it.

## Required Inputs

- original file or source reference;
- acquisition method and timestamp;
- source system and custodian when known;
- case or domain assignment;
- authorized operation.

## Procedure

1. Acquire without modifying the original.
2. Record original filename, byte size, media type, timestamps, source location, and acquisition method.
3. Compute a cryptographic hash before transformation.
4. Assign a stable evidence identifier.
5. Store the original in immutable or write-restricted storage.
6. Create transformations as separately identified derivatives.
7. Record the tool, version, parameters, operator, timestamp, and parent hash for every derivative.
8. Preserve OCR, transcription, redaction, compression, stamping, and annotation as distinct lineage events.
9. Generate page, line, frame, or timecode anchors where feasible.
10. Link extracted assertions to the exact source anchor.
11. Record transfers, access, and write events in an append-only custody log.
12. Validate hashes before use in a court-facing artifact.

## Non-Negotiable Rules

- Never overwrite an original with an OCR, compressed, redacted, or annotated version.
- Never claim authentication merely because a file exists in a trusted connector.
- Never omit failed extraction attempts or quality warnings.
- Never expose private evidence in a public skills repository.
- Never use a generated summary as a substitute for the underlying source.

## Required Output

- evidence record;
- original hash;
- derivative graph;
- custody events;
- extraction-quality report;
- citation anchors;
- unresolved authenticity or completeness issues.

## Exit Criteria

The evidence leg is complete when every derivative resolves to an unchanged original, every transformation is reproducible or documented, and each relied-upon assertion has a precise source anchor.