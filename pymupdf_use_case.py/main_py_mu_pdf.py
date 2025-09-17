
# Import PyMuPDF
import fitz  

# Open a PDF file
pdf_document_dip_3 = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"
doc = fitz.open(pdf_document_dip_3)
#________________________________--estrae pagina intere per pagina ___________________________________
# Initialize an empty string to store extracted text
extracted_text = ""
# Iterate through each page and extract text
"""for page_num in range(doc.page_count):
    page = doc[page_num]
    extracted_text += page.get_text() 
# Close the PDF document
doc.close()

# Perform text analysis (e.g., count words)
word_count = len(extracted_text.split())
print(f"The Extracted text is as follows:\n{extracted_text}")
print(f"Total words in the document: {word_count}")
"""


#________________________________estrae riga per riga____________________________________________
righe_estratte = []

for page_num in range(doc.page_count):
    page = doc[page_num]
    text = page.get_text("text")  # "text" mode: restituisce il testo riga per riga
    for line in text.splitlines():
        if line.strip():  # esclude righe vuote
            righe_estratte.append(line.strip())

doc.close()

# Ora righe_estratte è una lista di stringhe, una per ogni riga del PDF
print("Esempio di righe estratte:")
for riga in righe_estratte:  # stampa le prime 10 righe
    print(riga)