# =====================================================================
# DOCKERFILE FOR RAILWAY DEPLOYMENT
# Turnitin Paraphrase Automator
# =====================================================================
FROM python:3.11-slim

# Prevent Python from writing .pyc and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app

# Install system dependencies needed for lxml and PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Ensure storage directories exist
RUN mkdir -p uploads outputs

# Expose port (Railway injects $PORT environment variable)
EXPOSE 8000

# Start Uvicorn ASGI server with dynamic port binding
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
