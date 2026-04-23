# DevOps Stage 2 – Microservices Containerization & CI/CD

## Overview
This project containerizes and deploys a multi-service job processing system consisting of:

- Frontend (Node.js)
- API (FastAPI)
- Worker (Python)
- Redis (queue)

The system allows users to submit jobs, process them asynchronously, and track their status.

---

## Prerequisites

Ensure you have the following installed:

- Docker
- Docker Compose
- Git

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-fork-url>
cd hng14-stage2-devops
```
2. Create environment variables
```bash
cp .env.example .env
```
```bash
REDIS_HOST=redis
REDIS_PORT=6379
API_URL=http://api:8000
```
3. Build and run the application
```bash
docker-compose up --build
```
Application URLs
- Frontend: http://localhost:3000
- API: http://localhost:8000

How It Works
- User submits job via frontend
- API stores job in Redis queue
- Worker processes job
- Status updated in Redis
- Frontend polls API for updates

Health Checks
Each service includes Docker healthchecks:
- API: /health
- Worker: process check
- Frontend: HTTP check

Running Tests
```bash
pytest api
```