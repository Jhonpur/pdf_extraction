import pdfplumber

loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"

"""delimitiamo la zona corrispondenete solo alle voci variabili per fare un 'estrazione piu efficiente"""
with pdfplumber.open(loc) as pdf:
    #print(pdf.metadata)
    #print("===========================================================================")
    for page in pdf.pages:
      print(f"---------------pagina{page.page_number}------------------------")
      #text = page.extract_text_lines(layout=False, strip=True, return_chars=True)
      #print(text)
      if page.page_number == 2:
        page =page.crop(bbox=(35, 270.9,230.3,600))
        #im.draw_rects(page.extract_text_lines())
        #im.show()
        print(page.extract_text())
        print("====================================================================")