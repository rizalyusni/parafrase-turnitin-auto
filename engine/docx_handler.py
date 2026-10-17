# -*- coding: utf-8 -*-
"""
Word Document (.docx) Format Preserver and Upgrader.
Replaces paragraph runs while strictly locking styles, alignments,
line spacings, tables, equations, and section page setups.
"""
import re
import docx
from docx.shared import Pt
from pathlib import Path

DEFAULT_ITALIC_TERMS = [
    r"Capital Adequacy Ratio",
    r"Return on Assets",
    r"Return On Assets",
    r"Return on Equity",
    r"Return On Equity",
    r"Financing to Deposit Ratio",
    r"Zakat Performance Ratio",
    r"Falah Performance Index",
    r"min-max normalization",
    r"equal weighting",
    r"benefit criterion",
    r"benefit criteria",
    r"cost criterion",
    r"cost criteria",
    r"target criterion",
    r"target criteria",
    r"under-financing",
    r"over-financing",
    r"under-intermediation",
    r"purposive sampling",
    r"runner-up",
    r"maqashid al-syari'ah",
    r"maqashid syariah",
    r"tahdzib al-fard",
    r"iqamah al-'adl",
    r"jalb al-maslahah",
    r"hifz al-mal",
    r"hifz al-Mal",
    r"istimrar al-maslahah",
    r"israf",
    r"tabdzir",
    r"mustahik",
    r"nazhir",
    r"wakif",
    r"wasilah",
    r"falah",
]

pattern_str = "(" + "|".join(DEFAULT_ITALIC_TERMS) + ")"
pattern = re.compile(pattern_str, re.IGNORECASE)

def update_paragraph_runs(paragraph: docx.text.paragraph.Paragraph, new_text: str):
    """
    Safely clears text runs without affecting paragraph XML properties,
    re-populates with new text, sets font to Times New Roman 12pt,
    and applies italics to designated academic and foreign terms.
    """
    p_elem = paragraph._p

    # Remove text runs while leaving drawing or math intact
    for r in list(p_elem.xpath('./w:r')):
        if r.xpath('./w:drawing') or r.xpath('./w:m'):
            continue
        p_elem.remove(r)

    tokens = pattern.split(new_text)
    for token in tokens:
        if not token:
            continue
        run = paragraph.add_run(token)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        if pattern.fullmatch(token.strip()):
            run.italic = True
        else:
            run.italic = False

def process_and_save_docx(input_path: str, output_path: str, paraphrases: dict[int, str]) -> dict:
    """
    Loads input_path docx, updates specified paragraph indices,
    leaves all tables, equations, and locked paragraphs intact,
    and saves to output_path.
    Returns audit statistics.
    """
    doc = docx.Document(input_path)
    total_paragraphs = len(doc.paragraphs)
    total_tables = len(doc.tables)
    total_sections = len(doc.sections)

    updated_count = 0
    for idx, new_text in paraphrases.items():
        if idx < total_paragraphs:
            update_paragraph_runs(doc.paragraphs[idx], new_text)
            updated_count += 1

    doc.save(output_path)

    return {
        "total_paragraphs": total_paragraphs,
        "total_tables": total_tables,
        "total_sections": total_sections,
        "updated_count": updated_count,
        "output_path": output_path
    }
