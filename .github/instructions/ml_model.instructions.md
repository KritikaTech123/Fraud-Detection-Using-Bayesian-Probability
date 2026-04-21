---
description: "Use when editing training, prediction, feature engineering, model bundle artifacts, or SHAP explanation logic in ml_model. Covers feature order, bundle compatibility, and training-data assumptions."
name: "ML Pipeline Guidelines"
applyTo: "ml_model/**/*.py"
---
# ML Pipeline Guidelines

- Keep fixed feature order unchanged: `Time`, `V1..V28`, `Amount`.
- Keep training and inference artifact compatibility with backend model loading.
- Preserve model bundle keys expected by backend:
  - `model_name`, `model`, `imputer`, `scaler`, `feature_names`, `threshold`, `metrics`, `background`
- Keep threshold semantics stable unless explicitly requested (`0.5` default classification threshold).
- Keep class imbalance handling via SMOTE in training (sampling config from `ml_model/config.py`).
- Keep explanation outputs consumable by backend/frontend (top features with impact magnitude fields).
- Dataset assumptions are strict: CSV must include `Time`, `V1..V28`, `Amount`, `Class`.
- For setup and dataset location, link to existing docs:
  - [Project setup](../../README.md)
  - [Dataset placement](../../ml_model/data/README.md)
  - [Current training workflow](../../ml_model/train.py)
