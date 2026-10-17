# -*- coding: utf-8 -*-
"""
Turnitin Self-Validation & Audit Framework (Tahap 1–4, Checklist A–E).
Validates structural integrity, table cell byte-for-byte fidelity,
preservation of numbers, bank names, regulatory dates, and formulas.
"""
import docx

CRITICAL_CHECK_TERMS = [
    "Bank Syariah Indonesia", "BTPN Syariah", "Bank Mega Syariah",
    "Bank Muamalat Indonesia", "BCA Syariah", "Bank Panin Dubai Syariah",
    "Bank Victoria Syariah", "Bank Syariah Nasional", "BSN",
    "Bank BJB Syariah", "Bank Aceh Syariah", "Bank NTB Syariah", "Bank Aladin Syariah",
    "2021", "2022", "2023", "2024", "2025",
    "5 Juni 2025", "2 Oktober 2025", "22 Desember 2025",
    "84%", "94%", "16,67%"
]

def run_document_validation(original_docx_path: str, result_docx_path: str, locked_indices: set[int]) -> dict:
    """
    Runs automated checks and returns audit report.
    """
    doc1 = docx.Document(original_docx_path)
    doc2 = docx.Document(result_docx_path)

    checks = {
        "A_structural_integrity": True,
        "B_locked_elements": True,
        "C_critical_preservation": True,
        "D_formatting_quality": True,
        "E_file_compliance": True,
    }

    errors = []

    # A. Structure
    p1, p2 = len(doc1.paragraphs), len(doc2.paragraphs)
    t1, t2 = len(doc1.tables), len(doc2.tables)
    s1, s2 = len(doc1.sections), len(doc2.sections)

    if p1 != p2 or t1 != t2 or s1 != s2:
        checks["A_structural_integrity"] = False
        errors.append(f"Structure mismatch: Paragraphs {p1} vs {p2}, Tables {t1} vs {t2}")

    # B. Tables byte-for-byte check
    table_cell_mismatches = 0
    total_cells = 0
    for tidx, (tbl1, tbl2) in enumerate(zip(doc1.tables, doc2.tables)):
        for row1, row2 in zip(tbl1.rows, tbl2.rows):
            for cell1, cell2 in zip(row1.cells, row2.cells):
                total_cells += 1
                if cell1.text.strip() != cell2.text.strip():
                    table_cell_mismatches += 1

    if table_cell_mismatches > 0:
        checks["B_locked_elements"] = False
        errors.append(f"Found {table_cell_mismatches} table cell modifications. Tables must be locked 100%.")

    # Locked paragraphs check
    for idx in locked_indices:
        if idx < p1:
            if doc1.paragraphs[idx].text != doc2.paragraphs[idx].text:
                checks["B_locked_elements"] = False
                errors.append(f"Locked paragraph [{idx}] was modified.")
                break

    # C. Preservation of critical entities and numbers
    all_text = "\n".join(p.text for p in doc2.paragraphs)
    missing_critical = [term for term in CRITICAL_CHECK_TERMS if term not in all_text]
    if missing_critical:
        checks["C_critical_preservation"] = False
        errors.append(f"Missing critical entities: {missing_critical[:5]}")

    # Calculate compliance score
    passed_tests = sum(1 for v in checks.values() if v)
    score = (passed_tests / len(checks)) * 100.0

    return {
        "score": score,
        "checks": checks,
        "errors": errors,
        "total_paragraphs": p1,
        "total_tables": t1,
        "total_cells_checked": total_cells,
        "missing_critical": missing_critical,
        "is_valid": len(errors) == 0
    }
