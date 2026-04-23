# -------- BUILD STAGE --------
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .


# -------- RUNTIME --------
FROM node:20-alpine

WORKDIR /app

# Copy only necessary files
COPY --from=builder /app /app

# Non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 3000

HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1



CMD ["node", "app.js"]