import pdfplumber
import re
import pandas  as pd


import re

def pulisci_testo(text):
    # Rimuovi caratteri non stampabili
    text = re.sub(r'[^\x20-\x7EàèéìòùÀÈÉÌÒÙçÇ°€\n]', '', text)
    # Rimuovi righe vuote o troppo corte
    righe = [r.strip() for r in text.split('\n') if len(r.strip()) > 2]
    # Unisci righe spezzate (opzionale, dipende dalla struttura)
    testo_pulito = '\n'.join(righe)
    return testo_pulito

"""# Esempio d'uso
testo_estratto = "...il tuo testo qui..."
testo_pulito = pulisci_testo(testo_estratto)
print(testo_pulito)"""

loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"
loc2 = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.docx"

with pdfplumber.open(loc2) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    text_pulito = pulisci_testo(text)
    for line in text_pulito.split(' \n'):
        print(line)


