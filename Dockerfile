# =====================================================================
# DOCKERFILE FOR RAILWAY DEPLOYMENT
# Turnitin Paraphrase Automator
# =====================================================================
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

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

# Expose port (Railway dynamically injects $PORT)
EXPOSE 8000

# Start server using python main.py
CMD ["python", "main.py"]
