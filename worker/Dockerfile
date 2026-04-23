FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.11-slim

WORKDIR /app

# copy installed packages
COPY --from=builder /usr/local /usr/local

# copy code
COPY . .

RUN useradd -m appuser
USER appuser

HEALTHCHECK CMD pgrep -f worker.py || exit 1

CMD ["python", "worker.py"]