# -*- coding: utf-8 -*-
"""
Paragraph Classifier & Element Protector for Turnitin Documents.
Classifies paragraphs into NARRATIVE, HEADING, TABLE_DATA, FORMULA, EMPTY, etc.
Detects typos on locked elements without altering them.
"""
import re
import docx

FORMULA_PATTERNS = [
    re.compile(r'^(Rumus|r\s*=|d\s*=|d\s+max|d\s+min|di\s*=|w\s*=|FPIi\s*=|r=|di=)', re.IGNORECASE),
    re.compile(r'^\s*-\s+Benefit\s+criterion', re.IGNORECASE),
    re.compile(r'^\s*-\s+Cost\s+criterion', re.IGNORECASE),
    re.compile(r'^\s*-\s+Target\s+criterion', re.IGNORECASE),
    re.compile(r'^\s*-\s+Equal\s+weighting', re.IGNORECASE),
    re.compile(r'^\s*Bobot\s+indikator', re.IGNORECASE),
    re.compile(r'^\s*Nilai\s+target', re.IGNORECASE),
    re.compile(r'^\s*Nilai\s+minimum', re.IGNORECASE),
    re.compile(r'^\s*Nilai\s+maksimum', re.IGNORECASE),
]

TABLE_PATTERNS = [
    re.compile(r'^Tabel\s+[0-9IVXLCDM]+', re.IGNORECASE),
    re.compile(r'^Sumber\s*:', re.IGNORECASE),
    re.compile(r'^(Data\s+Tabel|Data\s+Matriks|Data\s+Normalisasi|Tabel\s+Normalisasi|Tabel\s+Data|Matriks\s+Normalisasi|Matriks\s+Keputusan)', re.IGNORECASE),
    re.compile(r'^(Perkembangan\s+Peringkat|Peringkat\s+Falah|Peringkat\s+FPI|Peringkat\s+Kinerja)', re.IGNORECASE),
    re.compile(r'^Bank\s+Umum\s+Syariah\s+yang\s+Menjadi\s+Sampel', re.IGNORECASE),
    re.compile(r'^Data\s+Tahun\s+\d{4}', re.IGNORECASE),
    re.compile(r'^Data\s+(Return On Equity|Beban Operasional|Financing to Deposit|Zakat Performance)', re.IGNORECASE),
]

HEADING_PATTERNS = [
    re.compile(r'^BAB\s+[IVXLCDM]+', re.IGNORECASE),
    re.compile(r'^(HASIL\s+PENELITIAN|ANALISIS\s+DAN\s+PEMBAHASAN|PEMBAHASAN|PENUTUP|KESIMPULAN)', re.IGNORECASE),
    re.compile(r'^[A-Z]\.\s+'),
    re.compile(r'^\d+\.\s+'),
    re.compile(r'^[a-z]\.\s+'),
    re.compile(r'^Normalisasi\s+(CAR|ROA|ROE|BOPO|FDR|ZPR|Tahun)', re.IGNORECASE),
    re.compile(r'^Perkembangan\s+(Capital Adequacy|Return On Asset|Return On Equity|Beban Operasional|Financing to Deposit|Zakat Performance|Biaya Operasional|Kinerja Bank)', re.IGNORECASE),
    re.compile(r'^Peringkat\s+Tahun\s+\d{4}', re.IGNORECASE),
]

KNOWN_LOCKED_HEADINGS = {
    'deskripsi objek penelitian', 'penyajian data', 'capital adequacy ratio (car)',
    'return on asset (roa)', 'return on equity (roe)', 'beban operasional terhadap pendapatan operasional  (bopo)',
    'financing to deposit ratio (fdr)', 'zakat performance ratio (zpr)',
    'analisis data', 'penyusunan matriks keputusan', 'normalisasi matriks keputusan',
    'pembahasan', 'perkembangan return on equity (roa)',
    'peringkat tahun 2021', 'peringkat tahun 2022', 'peringkat tahun 2023', 'peringkat tahun 2024', 'peringkat tahun 2025',
    'dinamika peringkat selama periode 20212025', 'dinamika peringkat selama periode 2021-2025',
    'falah dalam aspek ketahanan dan keberlanjutan keuangan',
    'falah dalam aspek produktivitas dan profitabilitas',
    'falah dalam aspek efisiensi pengelolaan sumber daya',
    'falah dalam fungsi intermediasi dan kemaslahatan ekonomi',
    'falah dalam dimensi sosial melalui zakat',
    'keseimbangan kinerja sebagai cerminan falah',
    'makna perbedaan nilai fpi terhadap pencapaian falah',
    'sintesis pencapaian prinsip falah',
    'penyusunan matriks keputusan 2023',
    'penyusunan matriks keputusan fpi 2025',
    'normalisasi retrun on asset (roa)',
    'normalisasi return on equity (roe)',
    'normalisasi financial to deposit ratio (fdr) 2021',
}

FORMULA_LEAD_INS = {
    'karena semua indikator diberi bobot sama, yaitu:',
    'maka nilai fpi dihitung dengan:',
    'untuk contoh bank syariah indonesia:',
    'karena car/kpmm merupakan kriteria benefit, normalisasi dilakukan menggunakan rumus:',
    'setelah seluruh jarak dihitung, nilai jarak diperlakukan sebagai kriteria cost dan dinormalisasi menggunakan rumus:',
    'maka normalisasi fdr bank syariah indonesia:',
    'pada tahun 2021 diperoleh:',
    'untuk tahun 2021, contoh pada bank syariah indonesia dengan fdr sebesar 73,39%:',
    'untuk memperjelas perubahan posisi masing-masing bank, hasil pemeringkatan selama periode penelitian dapat diringkas sebagai berikut.'
}

def classify_paragraph(p: docx.text.paragraph.Paragraph, idx: int):
    """
    Classifies a paragraph object and returns (classification, is_locked).
    """
    txt = p.text.strip()
    txt_lower = txt.lower()

    if not txt:
        return "EMPTY", True

    # Check for Word equation XML objects (oMathPara, oMath)
    if 'oMath' in p._p.xml:
        return "FORMULA", True

    if any(pat.search(txt) for pat in FORMULA_PATTERNS):
        return "FORMULA", True

    if txt_lower in FORMULA_LEAD_INS:
        return "FORMULA", True

    if txt_lower.startswith('hasil normalisasi') and txt_lower.endswith('sebagai berikut:'):
        return "TABLE_LABEL", True

    if any(pat.match(txt) for pat in TABLE_PATTERNS):
        return "TABLE_LABEL", True

    if p.style.name.startswith('Heading'):
        return "HEADING", True

    if txt_lower in KNOWN_LOCKED_HEADINGS:
        return "HEADING", True

    if any(pat.match(txt) for pat in HEADING_PATTERNS) and len(txt) < 130:
        return "HEADING", True

    if p.style.name == 'List Paragraph' and len(txt) < 80:
        return "HEADING", True

    if any(r.bold for r in p.runs) and len(txt) < 80:
        return "HEADING", True

    # If it reached here and has meaningful content, it is eligible narrative text
    return "NARRATIVE", False


def audit_locked_typos(paragraphs: list[str]) -> list[dict]:
    """
    Detects typos in headings or locked elements to generate the Typo Audit Report
    without mutating the original locked text.
    """
    findings = []
    typo_rules = [
        (re.compile(r'Perkembangan Return On Equity \(ROA\)', re.IGNORECASE), "Perkembangan Return On Equity (ROE)", "Singkatan salah: tertulis (ROA), semestinya (ROE)"),
        (re.compile(r'Normalisasi Retrun On Asset', re.IGNORECASE), "Normalisasi Return On Assets", "Typo kata 'Retrun' semestinya 'Return'"),
        (re.compile(r'Normalisasi Financial to Deposit Ratio', re.IGNORECASE), "Normalisasi Financing to Deposit Ratio", "Nomenklatur salah: tertulis 'Financial', semestinya 'Financing'"),
        (re.compile(r'normalis000000asi', re.IGNORECASE), "normalisasi", "Typo slip angka nol pada kata 'normalis000000asi'"),
    ]

    for idx, txt in enumerate(paragraphs):
        for pattern, correction, note in typo_rules:
            if pattern.search(txt):
                findings.append({
                    "paragraph_index": idx,
                    "typo_found": pattern.pattern,
                    "saran_perbaikan": correction,
                    "catatan": note
                })
    return findings
