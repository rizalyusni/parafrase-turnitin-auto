# -*- coding: utf-8 -*-
"""
Configuration settings for Turnitin Automated Paraphrase Tool.
Supports Railway deployment (DATABASE_URL, PORT) and local execution.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Database URL handling for Railway PostgreSQL
# Railway provides DATABASE_URL in postgres:// format, SQLAlchemy 2.0 requires postgresql://
RAW_DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/turnitin_paraphrase.db")
if RAW_DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = RAW_DATABASE_URL.replace("postgres://", "postgresql://", 1)
else:
    DATABASE_URL = RAW_DATABASE_URL

# Gemini or OpenAI API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Server configuration
PORT = int(os.getenv("PORT", 8000))
HOST = os.getenv("HOST", "0.0.0.0")

# Security and app secrets
SECRET_KEY = os.getenv("SECRET_KEY", "turnitin-paraphrase-super-secret-key-2026")
