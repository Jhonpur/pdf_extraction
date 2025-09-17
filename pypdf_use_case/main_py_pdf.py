from pypdf import PdfReader
import re



reader_dip_3 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")
reader_dip_6 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 06 - mese 01.2025.pdf")
reader_dip_5 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 05 - mese 01.2025.pdf")
reader_dip_10 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 10 - mese 01.2025.pdf")
reader_dip_22 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 22 - mese 01.2025.pdf")
# Iterate through all the pages in the PDF document

"""for i in reader_dip_3:
    # Extract and print the text content of each page
    print(i.extract_text())"""
 
    
   

dati = {}

#reader = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")
righe_estratte = []
for page in reader_dip_3.pages:
    text = page.extract_text()
    if text:
        for line in text.splitlines():
            righe_estratte.append(line)
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

   
           