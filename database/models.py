# -*- coding: utf-8 -*-
"""
Database Models for Turnitin Paraphrase Automation Tool.
PostgreSQL and SQLite compatible via SQLAlchemy.
"""
import uuid
from datetime import datetime
from sqlalchemy import (
    Column, String, Text, Integer, Boolean, DateTime, Float, ForeignKey, Index
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class PadananKata(Base):
    """
    Permanent dictionary for vocabulary substitutions and preferred academic diction.
    Prevents mechanical/awkward synonyms and enforces scholarly Indonesian expressions.
    """
    __tablename__ = "dictionary_padanan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    kata_asal = Column(String(255), nullable=False, index=True)
    padanan_disukai = Column(Text, nullable=False) # Preferred academic terms (comma separated or single)
    padanan_terlarang = Column(Text, nullable=True) # Mechanical synonyms that must be avoided
    konteks = Column(String(255), nullable=True) # e.g. Metodologi, Statistik, Pembahasan, Umum
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        Index("idx_kata_asal_active", "kata_asal", "is_active"),
    )


class IstilahTerkunci(Base):
    """
    Protected entities, regulatory terms, variables, equations, and proper nouns
    that must NEVER be altered under any circumstances.
    """
    __tablename__ = "locked_terms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    istilah = Column(String(255), nullable=False, unique=True, index=True)
    kategori = Column(String(100), nullable=False, default="Umum") # Entitas, Regulasi, Variabel, Teori, Formula
    deskripsi = Column(Text, nullable=True)
    case_sensitive = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class ParaphraseJob(Base):
    """
    Records each paraphrase execution job, file states, and validation metrics.
    """
    __tablename__ = "paraphrase_jobs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = Column(String(255), nullable=False)
    original_size = Column(Integer, default=0)
    total_paragraphs = Column(Integer, default=0)
    narrative_count = Column(Integer, default=0)
    locked_count = Column(Integer, default=0)
    status = Column(String(50), default="pending", index=True) # pending, analyzing, paraphrasing, validating, completed, failed
    progress = Column(Integer, default=0) # 0 to 100%
    validation_score = Column(Float, default=100.0) # Percentage compliance
    file_path = Column(Text, nullable=True)
    result_path = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

    paragraphs = relationship("JobParagraph", back_populates="job", cascade="all, delete-orphan")
    typos = relationship("TypoReport", back_populates="job", cascade="all, delete-orphan")


class JobParagraph(Base):
    """
    Stores paragraph-by-paragraph audit trail (original vs paraphrased) for verification.
    """
    __tablename__ = "job_paragraphs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(String(36), ForeignKey("paraphrase_jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    paragraph_index = Column(Integer, nullable=False)
    style_name = Column(String(100), nullable=True)
    classification = Column(String(50), nullable=False) # NARRATIVE, HEADING, TABLE_DATA, FORMULA, CITATION, EMPTY
    is_locked = Column(Boolean, default=False)
    original_text = Column(Text, nullable=False)
    paraphrased_text = Column(Text, nullable=True)
    audit_notes = Column(Text, nullable=True)

    job = relationship("ParaphraseJob", back_populates="paragraphs")


class TypoReport(Base):
    """
    Captures typos detected on LOCKED elements (headings, table headers, formula annotations)
    without modifying them, adhering strictly to Turnitin framework audit rules.
    """
    __tablename__ = "job_typo_reports"

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(String(36), ForeignKey("paraphrase_jobs.id", ondelete="CASCADE"), nullable=False, index=True)
    paragraph_index = Column(Integer, nullable=False)
    typo_found = Column(String(255), nullable=False)
    saran_perbaikan = Column(String(255), nullable=True)
    catatan = Column(Text, nullable=True)

    job = relationship("ParaphraseJob", back_populates="typos")


class SystemSetting(Base):
    """
    Stores system runtime settings, active prompt overrides, and API configurations.
    """
    __tablename__ = "system_settings"

    key = Column(String(100), primary_key=True)
    value = Column(Text, nullable=False)
    description = Column(String(255), nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
