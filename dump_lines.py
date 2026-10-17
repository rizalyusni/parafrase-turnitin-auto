import docx

doc = docx.Document('Tesis Bab IV - VI.docx')

with open('inspect_all_lines.txt', 'w', encoding='utf-8') as f:
    for i, p in enumerate(doc.paragraphs):
        txt = p.text.strip()
        if txt:
            f.write(f"[{i}] ({p.style.name}) {txt}\n")

print("Dumped inspect_all_lines.txt")
