# -*- coding: utf-8 -*-
"""
Script to apply paraphrases to Tesis Bab IV - VI.docx
and save as Tesis Bab IV - VI - Hasil Parafrase.docx
"""
import re
import docx
from docx.shared import Pt

from para_part1 import PART1_PARAPHRASES
from para_part2 import PART2_PARAPHRASES
from para_part3 import PART3_PARAPHRASES
from para_part4 import PART4_PARAPHRASES
from para_part5 import PART5_PARAPHRASES

# Combine all 207 paraphrases
TESIS_PARAPHRASES = {}
TESIS_PARAPHRASES.update(PART1_PARAPHRASES)
TESIS_PARAPHRASES.update(PART2_PARAPHRASES)
TESIS_PARAPHRASES.update(PART3_PARAPHRASES)
TESIS_PARAPHRASES.update(PART4_PARAPHRASES)
TESIS_PARAPHRASES.update(PART5_PARAPHRASES)

# Key academic/foreign/transliterated terms to italicize
ITALIC_TERMS = [
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

pattern_str = "(" + "|".join(ITALIC_TERMS) + ")"
pattern = re.compile(pattern_str, re.IGNORECASE)

def update_paragraph(paragraph, text):
    """
    Safely updates text in paragraph, preserving paragraph properties and style,
    applying Times New Roman font (12pt) and italics to specified terms.
    """
    p_elem = paragraph._p
    
    # Remove existing runs, preserving any drawings or math objects if present
    for r in list(p_elem.xpath('./w:r')):
        if r.xpath('./w:drawing') or r.xpath('./w:m'):
            continue
        p_elem.remove(r)
        
    # Split text by italic patterns and append runs
    tokens = pattern.split(text)
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

def main():
    source_filename = "Tesis Bab IV - VI.docx"
    output_filename = "Tesis Bab IV - VI - Hasil Parafrase.docx"
    
    print(f"Loading {source_filename}...")
    doc = docx.Document(source_filename)
    orig_p_count = len(doc.paragraphs)
    orig_t_count = len(doc.tables)
    print(f"Loaded: {orig_p_count} paragraphs, {orig_t_count} tables, {len(doc.sections)} sections.")
    
    updated_count = 0
    for idx, new_text in sorted(TESIS_PARAPHRASES.items()):
        if idx < orig_p_count:
            p = doc.paragraphs[idx]
            update_paragraph(p, new_text)
            updated_count += 1
        else:
            print(f"Warning: Index {idx} out of range!")
            
    print(f"Total paragraphs successfully updated: {updated_count}")
    
    doc.save(output_filename)
    print(f"Saved paraphrased document as: {output_filename}")

if __name__ == "__main__":
    main()
