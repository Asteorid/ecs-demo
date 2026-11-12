FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ templates/

ENV PORT=80 \
    APP_TITLE="ECS Demo" \
    APP_MESSAGE="Hello from AWS ECS!" \
    APP_VERSION="v1" \
    APP_ENVIRONMENT="local" \
    APP_OWNER="not set"

EXPOSE 80

CMD ["python", "app.py"]
