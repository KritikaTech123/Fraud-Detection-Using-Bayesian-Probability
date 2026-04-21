---
description: "Add or update a FastAPI endpoint in backend/app with matching schema and service wiring while preserving project conventions."
name: "Add Backend Endpoint"
argument-hint: "Describe endpoint path, method, request/response fields, validation rules, and DB behavior"
agent: "agent"
---
Add or update one backend API endpoint in this repository based on the user request.

Requirements:
- Work only in backend files relevant to the endpoint.
- Follow project conventions from [.github/copilot-instructions.md](../copilot-instructions.md).
- Keep existing authentication behavior (`Depends(require_api_key)`) unless explicitly changed.
- Add or update Pydantic schemas in [backend/app/schemas.py](../../backend/app/schemas.py) when request or response shapes change.
- Add or update endpoint handlers in [backend/app/main.py](../../backend/app/main.py).
- If prediction logic changes are needed, update [backend/app/services/model_service.py](../../backend/app/services/model_service.py) without changing risk-score semantics unless asked.
- Preserve backward compatibility for existing endpoints unless explicitly asked to break it.

Execution checklist:
1. Identify existing endpoint and schema patterns before editing.
2. Implement minimal code changes for the requested endpoint behavior.
3. Validate imports and typing consistency.
4. Report exactly which files changed and any follow-up steps.
