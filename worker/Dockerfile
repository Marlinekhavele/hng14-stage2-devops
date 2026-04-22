FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . .

RUN useradd -m appuser
USER appuser

ENV PATH=/root/.local/bin:$PATH

# Simple healthcheck (process running)
HEALTHCHECK CMD pgrep -f worker.py || exit 1

CMD ["python", "worker.py"]