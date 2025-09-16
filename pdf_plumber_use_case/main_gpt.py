import pdfplumber
import pandas as pd
import json

# Percorso del tuo file PDF
loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"

estrazione = {"testo": [], "tabelle": []}

with pdfplumber.open(loc) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        # --- Estrazione del testo ---
        text = page.extract_text()
        if text:
            estrazione["testo"].append({
                "pagina": page_num,
                "contenuto": text
            })

        # --- Estrazione delle tabelle ---
        tables = page.extract_tables()
        for i, table in enumerate(tables, start=1):
            df = pd.DataFrame(table)
            estrazione["tabelle"].append({
                "pagina": page_num,
                "tabella_num": i,
                "contenuto": df.to_dict(orient="records")
            })

# Salvataggio in JSON
with open("busta_paga_estratta.json", "w", encoding="utf-8") as f:
    json.dump(estrazione, f, indent=4, ensure_ascii=False)

print("✅ Estrazione completata! File salvato come busta_paga_estratta.json")
