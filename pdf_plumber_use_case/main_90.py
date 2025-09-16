import pdfplumber

loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"

with pdfplumber.open(loc) as pdf:
    for page in pdf.pages:
        words = page.extract_words()
        # Filtra solo le parole che iniziano dopo una certa coordinata x (es: x0 > 50)
        filtered_words = [w for w in words if w['x0'] > 5]
        # Ricostruisci il testo filtrato
        testo_filtrato = ' '.join([w['text'] for w in filtered_words])
        print(testo_filtrato)