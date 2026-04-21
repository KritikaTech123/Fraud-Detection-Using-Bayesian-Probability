---
description: "Add or update a frontend dashboard feature in frontend/src while keeping compatibility with backend fraud API contracts."
name: "Add Frontend Feature"
argument-hint: "Describe the UI feature, data source endpoint, fields to display, and interaction behavior"
agent: "agent"
---
Add or update one frontend feature for this project.

Requirements:
- Work in frontend files under `frontend/src`.
- Follow project conventions from [.github/copilot-instructions.md](../copilot-instructions.md).
- Follow frontend guidance from [.github/instructions/frontend.instructions.md](../instructions/frontend.instructions.md).
- Keep API contract compatibility with backend endpoints and response fields.
- Preserve risk display semantics and explanation field usage unless explicitly requested to change.

Execution checklist:
1. Identify existing component and API helper patterns (or create minimal structure if missing).
2. Implement the smallest set of files needed for the requested feature.
3. Keep API calls and types consistent with backend schema contracts.
4. Report changed files and any follow-up setup needed to run the UI.
