from __future__ import annotations

from math import prod

ANOMALY_RULES: dict[str, dict[str, float | str]] = {
    "amount_spike": {
        "label": "Transaction amount is much larger than the customer's typical amount",
        "p_e_given_fraud": 0.84,
        "p_e_given_legit": 0.10,
    },
    "odd_hour": {
        "label": "Transaction happened at an unusual hour",
        "p_e_given_fraud": 0.62,
        "p_e_given_legit": 0.14,
    },
    "new_merchant": {
        "label": "Transaction was sent to a new merchant",
        "p_e_given_fraud": 0.70,
        "p_e_given_legit": 0.12,
    },
    "foreign_location": {
        "label": "Transaction originated from a foreign or unexpected location",
        "p_e_given_fraud": 0.76,
        "p_e_given_legit": 0.08,
    },
    "rapid_repeat": {
        "label": "Rapid repeat transactions were detected",
        "p_e_given_fraud": 0.81,
        "p_e_given_legit": 0.11,
    },
    "device_mismatch": {
        "label": "Device or browser does not match the user's usual pattern",
        "p_e_given_fraud": 0.68,
        "p_e_given_legit": 0.09,
    },
}


def classify_risk(probability: float) -> str:
    score = round(probability * 100)
    if score < 35:
        return "Low risk"
    if score < 70:
        return "Medium risk"
    return "High risk"


def parse_percentage(value: str | None, default: float) -> float:
    try:
        parsed = float(value) / 100 if value is not None else default
    except (TypeError, ValueError):
        return default
    return min(max(parsed, 0.001), 0.999)


def parse_number(value: str | None, default: float) -> float:
    try:
        return float(value) if value is not None else default
    except (TypeError, ValueError):
        return default


def build_form_values(form_data: dict[str, str]) -> dict[str, object]:
    transaction_amount = parse_number(form_data.get("transaction_amount"), 320.0)
    typical_amount = max(parse_number(form_data.get("typical_amount"), 95.0), 0.01)
    transaction_hour = int(parse_number(form_data.get("transaction_hour"), 13))

    values: dict[str, object] = {
        "prior_fraud_rate": form_data.get("prior_fraud_rate", "2.0"),
        "transaction_amount": transaction_amount,
        "typical_amount": typical_amount,
        "transaction_hour": transaction_hour,
    }

    values["amount_spike"] = transaction_amount >= typical_amount * 1.75
    values["odd_hour"] = transaction_hour < 6 or transaction_hour >= 23

    for key in ANOMALY_RULES:
        values[key] = form_data.get(key) == "1"

    return values


def compute_posterior(form_values: dict[str, object]) -> dict[str, object]:
    prior = parse_percentage(str(form_values["prior_fraud_rate"]), 0.02)
    active_evidence: list[dict[str, object]] = []
    likelihood_ratios: list[float] = []

    for key, rule in ANOMALY_RULES.items():
        if bool(form_values[key]):
            likelihood_ratio = float(rule["p_e_given_fraud"]) / float(rule["p_e_given_legit"])
            active_evidence.append(
                {
                    "label": str(rule["label"]),
                    "likelihood_ratio": f"{likelihood_ratio:.2f}x",
                }
            )
            likelihood_ratios.append(likelihood_ratio)

    prior_odds = prior / (1 - prior)
    posterior_odds = prior_odds * prod(likelihood_ratios) if likelihood_ratios else prior_odds
    posterior = posterior_odds / (1 + posterior_odds)

    return {
        "probability_percent": round(posterior * 100),
        "risk_level": classify_risk(posterior),
        "evidence": active_evidence,
    }
