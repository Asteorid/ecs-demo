from flask import Flask, render_template
import socket
import os
from datetime import UTC, datetime

app = Flask(__name__)


def get_container_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        return "Unavailable"


@app.route("/health")
def health():
    return "OK", 200


@app.route("/")
def index():
    return render_template(
        "index.html",
        title=os.getenv("APP_TITLE", "ECS Demo"),
        message=os.getenv("APP_MESSAGE", "Hello from AWS ECS!"),
        hostname=socket.gethostname(),
        ip=get_container_ip(),
        version=os.getenv("APP_VERSION", "v1"),
        environment=os.getenv("APP_ENVIRONMENT", "local"),
        owner=os.getenv("APP_OWNER", "not set"),
        aws_region=os.getenv("AWS_REGION", "local"),
        time=datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC"),
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", "80"))
    app.run(host="0.0.0.0", port=port)
