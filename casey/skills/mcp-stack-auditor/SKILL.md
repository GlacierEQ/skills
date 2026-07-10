---
name: mcp-stack-auditor
description: Audit a multi-connector MCP and agent stack, identify duplication and control-plane gaps, and produce a prioritized consolidation plan.
version: 1.0.0
risk: high
---

# MCP Stack Auditor

## Purpose

Convert a large connector configuration into a governed capability map. The objective is not to maximize connector count. It is to establish clear ownership, trust, permissions, routing, observability, and failure containment.

## Inputs

- MCP server and connector configuration
- Repository inventory
- Agent and workflow inventory
- Authentication and permission scopes
- Existing memory, task, evidence, and deployment systems
- Known reliability, latency, and duplication problems

## Required Analysis

1. Inventory every connector and capability.
2. Assign one primary pillar and optional secondary consumers.
3. Separate connector trust from factual reliability.
4. Record read, write, delete, execute, and administrative permissions.
5. Detect duplicate capabilities and competing systems of record.
6. Identify single points of failure, unsafe fan-out, and hidden write paths.
7. Define canonical routing rules and fallback order.
8. Define health, audit, and revocation controls.
9. Recommend consolidation before adding new connectors.

## Mandatory Output

- Current-state capability matrix
- Duplicate and overlap report
- Trust and permission matrix
- Canonical owner for every capability
- Source-of-truth map
- Failure-mode register
- Prioritized remediation plan
- North-star architecture
- Explicit assumptions and missing configuration

## Governing Rules

- More connectors are not automatically more capability.
- No connector may become canonical merely because it is convenient.
- High-risk writes require explicit authorization and an audit trail.
- Evidence storage, memory retrieval, task management, and generated artifacts must remain logically distinct.
- A connector outage must not silently redirect writes to an unapproved system.
- Credentials, tokens, private endpoints, and case-specific paths never enter a public skills repository.

## Exit Criteria

This skill is complete when every active connector has an owner, trust level, permission profile, canonical purpose, fallback rule, and retirement or retention decision.