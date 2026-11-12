from flask import Flask, render_template
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        hostname=socket.gethostname(),
        ip=socket.gethostbyname(socket.gethostname()),
        version=os.getenv("APP_VERSION", "v1"),
        time=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)