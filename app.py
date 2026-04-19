import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Docker Homework App")


def str_to_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


@app.route("/")
def home():
    port = os.getenv("PORT", "8080")
    debug = os.getenv("DEBUG", "false")

    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
                line-height: 1.6;
            }}
            .card {{
                border: 1px solid #dddddd;
                border-radius: 12px;
                padding: 24px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            }}
            code {{
                background: #f4f4f4;
                padding: 2px 6px;
                border-radius: 6px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{APP_NAME}</h1>
            <p>Приложение успешно запущено в Docker-контейнере.</p>
            <p><strong>Порт:</strong> <code>{port}</code></p>
            <p><strong>Режим DEBUG:</strong> <code>{debug}</code></p>
            <p><strong>Маршрут проверки:</strong> <code>/health</code></p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(
        status="ok",
        app=APP_NAME
    ), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    debug = str_to_bool(os.getenv("DEBUG", "false"))

    app.run(host="0.0.0.0", port=port, debug=debug, use_reloader=False)
