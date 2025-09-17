import fitz  # PyMuPDF

# Apri il PDF
doc = fitz.open(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")

for page_num in range(len(doc)):
    page = doc[page_num]

    # Estrazione con spazi "grezzi" (layout-based)
    text = page.get_text("text", flags=1+2+8)
    print("=== PAGINA", page_num + 1, "===")
    print(text)
