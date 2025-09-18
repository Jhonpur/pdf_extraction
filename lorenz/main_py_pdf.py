from PyPDF2 import PdfReader
import re
from mainpur import anonymize_text


reader_dip_3 = PdfReader(r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")
reader_dip_6 = PdfReader(r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction\Azienda 200 dip 06 - mese 01.2025.pdf")
reader_dip_5 = PdfReader(r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction\Azienda 200 dip 05 - mese 01.2025.pdf")
reader_dip_10 = PdfReader(r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction\Azienda 200 dip 10 - mese 01.2025.pdf")
reader_dip_22 = PdfReader(r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction\Azienda 200 dip 22 - mese 01.2025.pdf")
# Iterate through all the pages in the PDF document

"""for i in reader.pages:
    # Extract and print the text content of each page
    print(i.extract_text())
"""  

dati = {}

#reader = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")
righe_estratte = []
for page in reader_dip_22.pages:
    text = page.extract_text()
    if text:
        for line in text.splitlines():
            righe_estratte.append(line)
            clean_line = anonymize_text(line)
            print(line) 

print("============================================================================================================================")
lista_pattern = [r"^PAGA BASE$",r"^SCATTI N\.9,00$",r"^CONTING\.$",r"^3'ELEMEN\.$",r"^S\.MINIMO$",r"^SUP\.ASS\.$",
                 r"^Imp\. INPS$",r"^Imp\. INAIL$",r"^Imp\. IRPEF$",r"^IRPEF pagata$",
                 r"^F\.do 31/12$",r"^Rivalutaz\.$",r"^Imp\.rival\.$",r"^Quota anno$"]
for i, riga in enumerate(righe_estratte[:-1]):
    for pattern in lista_pattern:
        # Cerca una riga che sembra un nome di campo (tutto maiuscolo, niente numeri)
        if re.match(pattern, riga.strip()):
            valore = righe_estratte[i+1].strip()
            # Se la riga successiva è un valore numerico
            if re.match(r"^[\d.,]+$", valore):
                chiave = riga.strip().replace(" ", "_").lower()
                dati[chiave] = valore


print(dati)
print("--------------------------------------------------------------------")

# extract_columns_pdfplumber.py
import pdfplumber

pdf_path = "Azienda 200 dip 22 - mese 01.2025.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        print(f"\n--- Pagina {page_number} ---")
        words = page.extract_words(
            use_text_flow=False,   # non forza l'ordine, lascia posizioni reali
            keep_blank_chars=False
        )
        for w in words:
            text = w["text"]
            x0, x1 = w["x0"], w["x1"]
            top, bottom = w["top"], w["bottom"]
            print(f"{text:20s}  x0={x0:.1f}  x1={x1:.1f}  top={top:.1f}  bottom={bottom:.1f}")


from aspose.pdf.facades import PdfContentEditor
import os

base_path = r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction"
input_file = os.path.join(base_path, "Azienda 200 dip 22 - mese 01.2025.pdf")
#output_file = os.path.join(base_path, "Azienda 200 dip 22 - mese 01.2025_clean_all.pdf")

editor = PdfContentEditor()
editor.bind_pdf(input_file)

# iteriamo su tutte le pagine e sostituiamo
num_pages = editor.document.pages.count
for i in range(1, 3):
    editor.replace_text("STAMPA DI CONTROLLO", "", i)

#editor.save(output_file)
print("Filigrana rimossa da tutte le pagine:")
