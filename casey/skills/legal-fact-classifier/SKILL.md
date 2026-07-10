---
name: legal-fact-classifier
description: Separate established record facts, authenticated evidence, allegations, disputes, inferences, verification targets, and recommendations before legal drafting.
---

# Legal Fact Classifier

## Objective

Prevent legal analysis and drafting from overstating the record. Every material proposition must be classified before it is used.

## Classification Set

- `established_record_fact`: directly supported by an authenticated record;
- `authenticated_evidence`: authenticated exhibit or original with provenance;
- `party_allegation`: attributed claim not independently established;
- `disputed_fact`: materially conflicting support exists;
- `inference`: reasoned conclusion from identified facts;
- `verification_target`: potentially material proposition lacking required support;
- `strategic_recommendation`: proposed action, not evidence;
- `generated_summary`: derivative synthesis requiring source resolution.

## Procedure

1. Split compound statements into atomic propositions.
2. Identify the source for each proposition.
3. Assign one classification and a confidence level.
4. Record supporting and contradicting sources separately.
5. Identify missing authentication, date, page, line, docket, or timecode information.
6. Rewrite the proposition using language permitted by its classification.
7. Block court-facing use when the proof path is incomplete.
8. Produce a contradiction and verification queue.

## Court-Safe Language Rules

- State established facts directly and cite them.
- Attribute allegations to the declarant or filing party.
- Describe disputed matters as disputed.
- Label inferences and identify their factual basis.
- Phrase verification targets as questions or required proof, not conclusions.
- Keep recommendations out of factual declarations.

## Prohibitions

- No intent attribution without admissible support.
- No conflation of docket metadata with merits findings.
- No conversion of repetition into corroboration.
- No mixed procedural records across separate matters.
- No invented citation, quotation, deadline, or legal authority.

## Required Output

For each proposition return: identifier, normalized statement, classification, confidence, source links, contradiction links, missing proof, permitted wording, prohibited wording, and court-use status.

## Exit Criteria

The classification leg is complete when every material proposition has a proof path or is explicitly blocked and queued for verification.