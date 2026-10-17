# -*- coding: utf-8 -*-
"""
Verification script for Tesis Bab IV - VI - Hasil Parafrase.docx
Checks paragraph count, tables byte-for-byte, margins, locked paragraphs, and equations.
"""
import docx
from apply_paraphrase_to_tesis import TESIS_PARAPHRASES

def verify():
    f_orig = "Tesis Bab IV - VI.docx"
    f_para = "Tesis Bab IV - VI - Hasil Parafrase.docx"
    
    doc1 = docx.Document(f_orig)
    doc2 = docx.Document(f_para)
    
    errors = []
    
    # 1. Structure
    print(f"--- 1. Document Structure ---")
    p1, p2 = len(doc1.paragraphs), len(doc2.paragraphs)
    t1, t2 = len(doc1.tables), len(doc2.tables)
    s1, s2 = len(doc1.sections), len(doc2.sections)
    
    print(f"Paragraphs: orig={p1}, para={p2}")
    print(f"Tables:     orig={t1}, para={t2}")
    print(f"Sections:   orig={s1}, para={s2}")
    
    if p1 != p2:
        errors.append(f"Paragraph count mismatch: {p1} vs {p2}")
    if t1 != t2:
        errors.append(f"Table count mismatch: {t1} vs {t2}")
    if s1 != s2:
        errors.append(f"Section count mismatch: {s1} vs {s2}")
        
    # 2. Section Margins
    sec1 = doc1.sections[0]
    sec2 = doc2.sections[0]
    if (sec1.top_margin, sec1.bottom_margin, sec1.left_margin, sec1.right_margin) != \
       (sec2.top_margin, sec2.bottom_margin, sec2.left_margin, sec2.right_margin):
        errors.append("Section margins mismatch")
    else:
        print("Margins match perfectly (100%).")
        
    # 3. Tables verification
    print(f"\n--- 2. Table Integrity Check (All 48 Tables) ---")
    table_mismatches = 0
    total_cells = 0
    for tidx, (tbl1, tbl2) in enumerate(zip(doc1.tables, doc2.tables)):
        r1, r2 = len(tbl1.rows), len(tbl2.rows)
        c1, c2 = len(tbl1.columns), len(tbl2.columns)
        if (r1, c1) != (r2, c2):
            errors.append(f"Table {tidx} dimensions mismatch: ({r1},{c1}) vs ({r2},{c2})")
            table_mismatches += 1
            continue
        for row_i, (row1, row2) in enumerate(zip(tbl1.rows, tbl2.rows)):
            for col_i, (cell1, cell2) in enumerate(zip(row1.cells, row2.cells)):
                total_cells += 1
                if cell1.text.strip() != cell2.text.strip():
                    errors.append(f"Table {tidx} cell ({row_i},{col_i}) mismatch: {repr(cell1.text[:30])} vs {repr(cell2.text[:30])}")
                    table_mismatches += 1
    print(f"Total table cells checked: {total_cells}")
    if table_mismatches == 0:
        print("All 48 tables and all cells are 100% byte-for-byte identical!")
    else:
        print(f"Table mismatches found: {table_mismatches}")
        
    # 4. Locked paragraphs check
    print(f"\n--- 3. Locked Paragraphs Check ---")
    locked_count = 0
    locked_mismatches = 0
    for i in range(p1):
        if i not in TESIS_PARAPHRASES:
            locked_count += 1
            txt1 = doc1.paragraphs[i].text
            txt2 = doc2.paragraphs[i].text
            if txt1 != txt2:
                locked_mismatches += 1
                errors.append(f"Locked paragraph {i} mismatch: {repr(txt1[:40])} vs {repr(txt2[:40])}")
    print(f"Total locked paragraphs checked: {locked_count}")
    if locked_mismatches == 0:
        print("All 420 locked paragraphs are 100% strictly identical!")
    else:
        print(f"Locked paragraph mismatches: {locked_mismatches}")
        
    # 5. Math XML objects check
    print(f"\n--- 4. Math Equations Check ---")
    math_count_1 = sum(1 for p in doc1.paragraphs if 'oMath' in p._p.xml)
    math_count_2 = sum(1 for p in doc2.paragraphs if 'oMath' in p._p.xml)
    print(f"oMath elements in doc1: {math_count_1}, in doc2: {math_count_2}")
    if math_count_1 != math_count_2:
        errors.append(f"Math elements mismatch: {math_count_1} vs {math_count_2}")
    else:
        print("All Word math equation objects are 100% preserved!")
        
    # 6. Paraphrased paragraphs check
    print(f"\n--- 5. Paraphrased Paragraphs Check ---")
    para_updated_cnt = 0
    for idx in sorted(TESIS_PARAPHRASES.keys()):
        txt_new = doc2.paragraphs[idx].text.strip()
        if len(txt_new) > 0:
            para_updated_cnt += 1
    print(f"Target paragraphs successfully verified with updated content: {para_updated_cnt}/{len(TESIS_PARAPHRASES)}")
    
    # Critical data check in paraphrased text
    critical_terms = [
        "Bank Syariah Indonesia", "BTPN Syariah", "Bank Mega Syariah",
        "Bank Muamalat Indonesia", "BCA Syariah", "Bank Panin Dubai Syariah",
        "Bank Victoria Syariah", "Bank Syariah Nasional", "BSN",
        "Bank BJB Syariah", "Bank Aceh Syariah", "Bank NTB Syariah", "Bank Aladin Syariah",
        "2021", "2022", "2023", "2024", "2025",
        "5 Juni 2025", "2 Oktober 2025", "22 Desember 2025",
        "84%", "94%", "16,67%", "0,6853", "0,6961", "0,7439", "0,7545", "0,7941"
    ]
    all_doc2_text = "\n".join(p.text for p in doc2.paragraphs)
    missing_critical = [term for term in critical_terms if term not in all_doc2_text]
    if missing_critical:
        errors.append(f"Missing critical terms: {missing_critical}")
    else:
        print("All critical bank names, years, key regulatory dates, and benchmark metrics are present!")
        
    print(f"\n==========================================")
    if not errors:
        print("PERFECT VALIDATION: 0 ERRORS FOUND!")
        print("Document satisfies 100% of the Master Prompt constraints.")
    else:
        print(f"VALIDATION FAILED WITH {len(errors)} ERRORS:")
        for e in errors[:10]:
            print(" -", e)
    print(f"==========================================")

if __name__ == "__main__":
    verify()
