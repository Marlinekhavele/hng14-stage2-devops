# DevOps Stage 2 – Microservices Containerization & CI/CD

## 📌 Overview
This project containerizes and deploys a multi-service job processing system using Docker and a full CI/CD pipeline.

### Services
- **Frontend (Node.js)** – Submits and tracks jobs  
- **API (FastAPI)** – Creates jobs and returns status  
- **Worker (Python)** – Processes jobs asynchronously  
- **Redis** – Message queue  

---

## ⚙️ Prerequisites
- Docker (v20+)
- Docker Compose (v2)
- Git

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Marlinekhavele/hng14-stage2-devops
cd hng14-stage2-devops

```
### 2. Create environment file
```bash
cp .env.example .env
```
### 3. Build and run the application
```bash
docker compose up --build
```
### 4. Check application status
```bash
docker compose ps
```
### 5. run tests locally
```bash
python -m pytest api
```

Expected Output
- API available at → http://localhost:8000
- Frontend available at → http://localhost:3000
- Worker running in background
- Redis running internally (not exposed)

Test the System Create a job
```bash
curl -X POST http://localhost:8000/jobs
```
Check job status
```bash
curl http://localhost:8000/jobs/<job_id>
```

Expected response:
```
{
  "status": "completed"
}
```

🐳 Docker Implementation
- Multi-stage Docker builds
- All services run as non-root users
- Healthchecks implemented for all services
- Minimal production-ready images

🔗 Docker Compose Features
- Internal network communication
- Redis not exposed to host
- Services depend on health checks
- Environment variable configuration
- CPU and memory limits defined

🔄 CI/CD Pipeline
Implemented using GitHub Actions:
```
lint → test → build → security scan → integration test → deploy
```
- Lint – flake8, eslint, hadolint
- Test – pytest with Redis mocked
- Build – Docker images built and tagged
- Security Scan – Trivy scan (fails on CRITICAL issues)
- Integration Test – full stack tested inside CI
- Deploy – runs on main after health check

📄 Documentation
- [FIXES.md](FIXES.md) – all identified bugs and fixes
- .env.example – environment variable template