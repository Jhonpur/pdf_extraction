import pdfplumber

loc = r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction\Azienda 200 dip 22 - mese 01.2025_clean_all.pdf"

#cerchiamo le coordinate di una data parola nel pdf

with pdfplumber.open(loc) as pdf:
    for i, page in enumerate(pdf.pages):
        #pagina sulla quale voglio fare l'estrazione : pagina 2
        if page.page_number == 2:
            #delimito la zona dove fare l'estrazione : zona delle voci variabili 
            #page =page.crop(bbox=(36, 527.01,590.3,600))
            #estrazione di parole 
            words = page.extract_words(keep_blank_chars=True)
            for i in words:
                if i['text'] == "128,50":
                    print(i)
                #else : print("non trovato")    
            #filtro le parole in base alla loro cordinata X0
            #parole_filtrate = [w for w in words if w['x0'] >= 20]
            #words_sorted = sorted(words, key=lambda w: (w['top'], w['x0']))
            #print(words)    