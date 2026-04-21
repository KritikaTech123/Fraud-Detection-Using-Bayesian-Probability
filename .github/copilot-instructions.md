# Project Guidelines

## Architecture
- Keep boundaries clear:
  - ml_model/: training, model artifacts, and explanation utilities.
  - backend/app/: FastAPI API, DB models, schemas, and prediction service wiring.
  - frontend/src/: dashboard UI code that consumes backend endpoints.
- Backend should not retrain models; it must load artifacts produced by ml_model/train.py.

## Build and Run
- Python env setup:
  - pip install -r ml_model/requirements.txt
  - pip install -r backend/requirements.txt
- Train model artifacts first:
  - python ml_model/train.py
- Run backend locally:
  - uvicorn backend.app.main:app --reload --port 8000
- Full stack with containers:
  - docker compose up --build
- Testing status:
  - No automated test suite is currently present in this repository.

## Conventions
- Use Python type hints consistently (existing files use from __future__ import annotations).
- Respect fixed fraud feature order: Time, V1..V28, Amount.
- Keep Pydantic request models strict (TransactionInput forbids extra keys).
- Keep risk score semantics unchanged unless explicitly requested:
  - score = round(probability * 100)
  - low < 35, medium 35-69, high >= 70
- Preserve explanation response shape:
  - top features with feature, impact, abs_impact fields.

## Environment Gotchas
- Training requires dataset at ml_model/data/creditcard.csv.
- Backend startup requires ml_model/artifacts/model_bundle.joblib.
- Local backend defaults to SQLite at backend/fraudshield.db; Docker uses MySQL via DATABASE_URL.
- API key auth is optional, but enforced when API_KEY is set.
- CORS defaults assume frontend origins http://localhost:5173 and http://localhost:3000.

## Existing Docs
- Setup, API overview, and deployment notes: README.md
- Dataset placement details: ml_model/data/README.md
