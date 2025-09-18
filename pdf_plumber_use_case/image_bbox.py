import pdfplumber

loc = r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction\Azienda 200 dip 22 - mese 01.2025_clean_all.pdf"

"""delimitiamo la zona corrispondenete solo alle voci variabili per fare un 'estrazione piu efficiente
lo usiamo per determinare i limiti dei diversi bbox(sezioni) del pdf per l'estrazione."""
with pdfplumber.open(loc) as pdf:
    #print(pdf.metadata)
    #print("===========================================================================")
    for page in pdf.pages:
      print(f"---------------pagina{page.page_number}------------------------")
      #text = page.extract_text_lines(layout=False, strip=True, return_chars=True)
      #print(text)
      if page.page_number == 2:
        im =page.crop(bbox=(36, 270, 590, 600)).to_image()
        im.draw_rects(page.extract_text_lines())
        im.show()
        #print(page.extract_text(x_tolerance=1, y_tolerance=3))
        #print("====================================================================")