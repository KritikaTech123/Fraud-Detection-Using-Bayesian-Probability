# Bayesian Fraud Detector

A small Flask web app that estimates the probability of fraud with Bayes' theorem.

## Project Layout

- `app.py` launches the Flask app.
- `fraud_bayes/` contains the application factory and Bayesian scoring logic.
- `templates/index.html` renders the UI.
- `static/styles.css` styles the UI.

## What It Does

- Lets you enter a prior fraud rate and transaction details
- Flags common anomalies such as unusual amount, odd hour, new merchant, foreign location, rapid repeats, and device mismatch
- Combines the active anomaly signals with a naive Bayes update
- Shows a fraud probability and a simple low/medium/high risk label

## Run It

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8000` in your browser.

## Notes

- This is a lightweight demo, not a production fraud model.
- The previous backend, frontend, and ML pipeline were removed in favor of a single Python app.
