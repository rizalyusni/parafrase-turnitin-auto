# -*- coding: utf-8 -*-
"""
Database session and connection management with resilient PostgreSQL & SQLite fallback.
Guarantees zero-downtime boots on Railway.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config import DATABASE_URL, BASE_DIR
from database.models import Base

def create_app_engine(db_url: str):
    if db_url.startswith("sqlite"):
        return create_engine(
            db_url,
            connect_args={"check_same_thread": False}
        )
    return create_engine(
        db_url,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10
    )

# Resilient initialization: try target database, fallback to SQLite if unreachable
try:
    engine = create_app_engine(DATABASE_URL)
except Exception as e:
    print(f"[DB Warning] Initial engine setup failed: {e}. Falling back to SQLite.")
    fallback_url = f"sqlite:///{BASE_DIR}/turnitin_paraphrase.db"
    engine = create_app_engine(fallback_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency for FastAPI endpoints providing database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initializes schema and tables with graceful fallback."""
    global engine, SessionLocal
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"[DB Warning] Table creation failed on primary engine: {e}. Switching to SQLite...")
        fallback_url = f"sqlite:///{BASE_DIR}/turnitin_paraphrase.db"
        engine = create_app_engine(fallback_url)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)
