---
description: "Use when editing frontend dashboard UI code, API client wiring, or transaction visualization in frontend/src. Covers backend contract alignment and risk display conventions."
name: "Frontend Dashboard Guidelines"
applyTo: "frontend/src/**"
---
# Frontend Dashboard Guidelines

- Keep frontend scoped to UI rendering and API consumption; business logic for fraud scoring stays in backend/ml_model.
- Preserve backend API contract usage from [README.md](../../README.md):
  - prediction endpoint: `POST /predict`
  - read endpoints: `GET /history`, `GET /alerts`, `GET /metadata`
- Preserve risk display semantics:
  - low `< 35`, medium `35-69`, high `>= 70`
  - use backend-provided `risk_score` and `risk_level` without re-deriving unless requested.
- Handle API-key mode cleanly: include `X-API-Key` only when configured.
- Keep request payload shape aligned to model features (`Time`, `V1..V28`, `Amount`).
- Keep explanation UI aligned with backend shape: each item includes `feature`, `impact`, `abs_impact`.
- Prefer small, composable components in `frontend/src/components` and keep API helpers in `frontend/src/lib`.
- For setup details and endpoint reference, link instead of duplicating:
  - [Project setup and API overview](../../README.md)
  - [Backend response contracts](../../backend/app/schemas.py)
