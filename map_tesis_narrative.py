import docx
import re

doc = docx.Document('Tesis Bab IV - VI.docx')

# Let's inspect all paragraphs with length > 40 that are NOT table captions or headings or formulas
narrative_paras = []
formula_re = re.compile(r'^(Rumus|r\s*=|d\s*=|d\s+max|d\s+min|di\s*=|w\s*=|FPIi\s*=)', re.IGNORECASE)

for i, p in enumerate(doc.paragraphs):
    txt = p.text.strip()
    if not txt:
        continue
    if len(txt) < 35:
        continue
    if txt.startswith('Tabel ') or txt.startswith('Tabel\t') or txt.startswith('Sumber :') or txt.startswith('Sumber:'):
        continue
    if txt.startswith('Data Tabel') or txt.startswith('Data Matriks') or txt.startswith('Data Normalisasi') or txt.startswith('Tabel Normalisasi') or txt.startswith('Tabel Data Normalisasi') or txt.startswith('Matriks Normalisasi') or txt.startswith('Perkembangan Peringkat'):
        continue
    if txt.startswith('Peringkat Falah Performance Index') or txt.startswith('Peringkat FPI'):
        continue
    if formula_re.match(txt):
        continue
    # Headings
    if txt.startswith('Perkembangan Kinerja Bank') and len(txt) < 120:
        continue
    if txt.startswith('Hasil Pengukuran Kinerja') and len(txt) < 120:
        continue
    if txt.startswith('Peringkat Kinerja Bank') and len(txt) < 120:
        continue
    if txt.startswith('Pencapaian Prinsip Falah') and len(txt) < 130:
        continue
    
    narrative_paras.append((i, p.style.name, txt))

print(f"Total identified narrative paragraphs: {len(narrative_paras)}")
with open('tesis_narrative_identified.txt', 'w', encoding='utf-8') as f:
    for idx, st, t in narrative_paras:
        f.write(f"[{idx}] ({st}) {t}\n\n")

print("Saved tesis_narrative_identified.txt")
