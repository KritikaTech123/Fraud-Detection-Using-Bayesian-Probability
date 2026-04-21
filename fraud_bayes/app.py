from __future__ import annotations

from pathlib import Path

from flask import Flask, render_template, request

from .bayes import ANOMALY_RULES, build_form_values, compute_posterior


def create_app() -> Flask:
    project_root = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        template_folder=str(project_root / "templates"),
        static_folder=str(project_root / "static"),
    )

    @app.get("/")
    def index() -> str:
        form_values = {
            "prior_fraud_rate": "2.0",
            "transaction_amount": 320.0,
            "typical_amount": 95.0,
            "transaction_hour": 13,
            "amount_spike": True,
            "odd_hour": False,
            **{key: False for key in ANOMALY_RULES},
        }
        return render_template("index.html", anomaly_rules=ANOMALY_RULES, form_values=form_values, result=None)

    @app.post("/")
    def score() -> str:
        form_values = build_form_values(request.form.to_dict(flat=True))
        result = compute_posterior(form_values)
        return render_template("index.html", anomaly_rules=ANOMALY_RULES, form_values=form_values, result=result)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "Bayesian Fraud Detector"}

    return app
