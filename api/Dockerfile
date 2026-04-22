# -------- STAGE 1: Build --------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# -------- STAGE 2: Runtime --------
FROM python:3.11-slim

WORKDIR /app

# Install system deps FIRST (as root)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy only installed deps
COPY --from=builder /usr/local /usr/local
# Copy app code
COPY . .

# Create non-root user AFTER installs
RUN useradd -m appuser
USER appuser

# Ensure binaries are available
ENV PATH=/root/.local/bin:$PATH

# Healthcheck
HEALTHCHECK --interval=10s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]