from pypdf import PdfReader



reader_dip_3 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")
reader_dip_6 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 06 - mese 01.2025.pdf")
reader_dip_5 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 05 - mese 01.2025.pdf")
reader_dip_10 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 10 - mese 01.2025.pdf")
reader_dip_22 = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 22 - mese 01.2025.pdf")
# Iterate through all the pages in the PDF document

"""for i in reader.pages:
    # Extract and print the text content of each page
    print(i.extract_text())
"""   
    
   



#reader = PdfReader(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")

for page in reader_dip_22.pages:
    text = page.extract_text()
    if text:
        for line in text.splitlines():
            print(line)

           