# -------- STAGE 1: Build --------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# -------- STAGE 2: Runtime --------
FROM python:3.11-slim

WORKDIR /app

# Copy dependencies
COPY --from=builder /install /usr/local

# Copy code
COPY . .

# Non-root user
RUN adduser --disabled-password --gecos "" appuser
USER appuser

HEALTHCHECK CMD pgrep -f worker.py || exit 1

CMD ["python", "worker.py"]