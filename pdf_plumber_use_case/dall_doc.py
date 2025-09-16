import pdfplumber

loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"

with pdfplumber.open(loc) as pdf:
    for i, page in enumerate(pdf.pages):
      print(f"---------------pagina{i}------------------------")
      text = page.extract_text_lines(layout=False, strip=True, return_chars=True)
      print(text)