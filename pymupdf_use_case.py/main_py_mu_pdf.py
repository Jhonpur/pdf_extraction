
# Import PyMuPDF
import fitz  

# Open a PDF file
pdf_document_dip_3 = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"
doc = fitz.open(pdf_document_dip_3)

# Initialize an empty string to store extracted text
extracted_text = ""

# Iterate through each page and extract text
for page_num in range(doc.page_count):
    page = doc[page_num]
    extracted_text += page.get_text()
    
# Close the PDF document
doc.close()

# Perform text analysis (e.g., count words)
word_count = len(extracted_text.split())
print(f"The Extracted text is as follows:\n{extracted_text}")
print(f"Total words in the document: {word_count}")