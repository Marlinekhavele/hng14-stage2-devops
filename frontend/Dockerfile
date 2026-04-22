# -------- BUILD STAGE --------
FROM node:20-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install --production

COPY . .


# -------- RUNTIME --------
FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app /app

# Non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Healthcheck
HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1

EXPOSE 3000

CMD ["node", "app.js"]