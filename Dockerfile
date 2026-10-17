FROM python:3.11-slim

WORKDIR /app

# Install dependencies using precompiled wheels
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Ensure storage directories exist
RUN mkdir -p uploads outputs

EXPOSE 8080

CMD ["python", "main.py"]
