from __future__ import annotations

import os

from fraud_bayes import create_app


app = create_app()


if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.getenv("PORT", "8000"))
    app.run(host=host, port=port, debug=False)