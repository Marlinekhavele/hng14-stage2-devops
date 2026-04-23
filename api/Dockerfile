# -------- STAGE 1: Build --------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# -------- STAGE 2: Runtime --------
FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY --from=builder /install /usr/local

# Copy app
COPY . .

# Create non-root user (safe version)
RUN adduser --disabled-password --gecos "" appuser
USER appuser

EXPOSE 8000




HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]