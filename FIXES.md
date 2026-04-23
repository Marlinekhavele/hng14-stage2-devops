## 1. Hardcoded Redis connection API
- File: api/main.py
- Issue: Redis host was hardcoded to localhost
- Fix: Replaced with environment variables REDIS_HOST and REDIS_PORT

## 2. Hardcoded Redis connection Worker
- File: worker/worker.py
- Issue: Worker connected to localhost instead of containerized Redis
- Fix: Replaced with environment variables

## 3. Missing health endpoint
- File: api/main.py
- Issue: No health endpoint for Docker healthchecks
- Fix: Added /health route

## 4. Hardcoded API URL Frontend
- File: frontend/app.js
- Issue: API URL pointed to localhost
- Fix: Replaced with process.env.API_URL

## 5. Dependencies inaccessible due to --user install
- File: api/Dockerfile, worker/Dockerfile
- Issue: Packages installed in /root/.local not accessible to non-root user
- Fix: Installed globally and copied /usr/local instead

## 6. Permission issue with uvicorn
- File: api/Dockerfile
- Issue: Non-root user couldn't execute uvicorn
- Fix: Switched to global install path

## 7. Incorrect Dockerfile instruction order
- File: api/Dockerfile
- Issue: apt-get run after USER switch caused permission failure
- Fix: Moved system package installation before USER

## 8. Missing redis dependency
- File: worker/requirements.txt
- Issue: redis package not listed
- Fix: Added redis dependency

## 9. .env file included in build context
- File: api/.env
- Issue: Sensitive config included in repo and Docker build
- Fix: Removed .env and added .dockerignore

## 10. Redis exposed risk
- File: docker-compose.yml
- Issue: Redis could be exposed
- Fix: Removed ports mapping for Redis

## 11. No dependency health checks
- File: docker-compose.yml
- Issue: Services started before dependencies were ready
- Fix: Added depends_on with service_healthy condition

## 12. Added tests
- File: test_api.py
- Issue: No tests to check the API behaviour
- Fix: Added tests to check the API

## 12. Return 404 status code 
- File: test_api.py
- Issue:  The API returns a 200 status code when a job is not found
- Fix: Added a condition to return a 404 status code when the job is not found.
