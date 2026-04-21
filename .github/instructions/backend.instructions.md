---
description: "Use when editing FastAPI endpoints, Pydantic schemas, SQLAlchemy models, or prediction wiring in backend/app. Covers API shape, auth dependency usage, and DB persistence patterns."
name: "Backend API Guidelines"
applyTo: "backend/app/**/*.py"
---
# Backend API Guidelines

- Keep backend responsibilities limited to serving inference and persistence. Do not retrain models in backend code.
- Keep request models strict. `TransactionInput` must continue forbidding unknown keys.
- Keep non-health endpoints protected with `Depends(require_api_key)` so API key behavior remains consistent.
- Keep prediction response shape stable (`transaction_uid`, prediction/probability fields, risk fields, model name, explanation, timestamp).
- Preserve risk semantics unless explicitly requested:
  - `risk_score = round(probability * 100)`
  - low `< 35`, medium `35-69`, high `>= 70`
- Preserve explanation payload shape with top features containing `feature`, `impact`, and `abs_impact`.
- Follow existing DB flow in endpoint handlers: construct records, add to session, commit once.
- For context and setup details, link to docs instead of duplicating:
  - [Project setup and API overview](../../README.md)
  - [Current API patterns](../../backend/app/main.py)
  - [Current schema contracts](../../backend/app/schemas.py)
