import pdfplumber
import pandas as pd

loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"

# Estrazione di tutto il testo
all_text = []
with pdfplumber.open(loc) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            all_text.append(f"--- Pagina {i+1} ---\n{text}")

with open("testo_estratto.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(all_text))

print("✅ Testo estratto salvato in testo_estratto.txt")

# Estrazione di tutte le tabelle
tables = []
with pdfplumber.open(loc) as pdf:
    for i, page in enumerate(pdf.pages):
        page_tables = page.extract_tables()
        for table in page_tables:
            if table:
                df = pd.DataFrame(table)
                df.to_csv(f"tabella_pagina_{i+1}.csv", index=False, header=False)
                print(f"✅ Tabella trovata a pagina {i+1} salvata in tabella_pagina_{i+1}.csv")