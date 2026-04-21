---
description: "Retrain or update the fraud model pipeline in ml_model while preserving artifact compatibility with backend loading."
name: "Retrain Fraud Model"
argument-hint: "Describe what to change in training, features, metrics, thresholds, or explanation behavior"
agent: "agent"
---
Update model training or inference code in ml_model based on the user request.

Requirements:
- Work only in ml_model files relevant to training, prediction, feature engineering, or explanations.
- Follow project conventions from [.github/copilot-instructions.md](../copilot-instructions.md).
- Follow ML-specific guidance in [.github/instructions/ml_model.instructions.md](../instructions/ml_model.instructions.md).
- Preserve backend compatibility unless the user explicitly requests a breaking change.
- Keep fixed feature ordering intact unless explicitly requested to change it.
- If artifact schema changes are required, update backend loading paths and metadata handling in the same task.

Execution checklist:
1. Inspect current training and prediction flow in [ml_model/train.py](../../ml_model/train.py), [ml_model/predict.py](../../ml_model/predict.py), and [ml_model/explain.py](../../ml_model/explain.py).
2. Implement minimal changes to satisfy the request.
3. Ensure produced artifacts remain usable by backend service loading.
4. Report changed files, behavior impact, and any retraining command to run.
