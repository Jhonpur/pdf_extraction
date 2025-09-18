import pdfplumber

loc = r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction\Azienda 200 dip 22 - mese 01.2025_clean_all.pdf"

#stampa le righe da sinistra adestra conservando gli spazi tra le stringhe come nel documento pdf.

def trova_riga(y, righe, tolleranza=2):
    for y_riga in righe:
        if abs(y - y_riga) <= tolleranza:
            return y_riga
    return y

with pdfplumber.open(loc) as pdf:
    for i, page in enumerate(pdf.pages):
        #pagina sulla quale voglio fare l'estrazione : pagina 2
        if page.page_number == 2:
            #delimito la zona dove fare l'estrazione : zona delle voci variabili 
            page =page.crop(bbox=(28, 645, 590, 670))
            #estrazione di parole 
            words = page.extract_words(x_tolerance = 1, keep_blank_chars=True)
            #filtro le parole in base alla loro cordinata X0
            #parole_filtrate = [w for w in words if w['x0'] >= 20]
            words_sorted = sorted(words, key=lambda w: (w['top'], w['x0']))
            righe = {}
            for w in words_sorted:
                y = w['top']
                y_riga = trova_riga(y, righe, tolleranza=2)
                righe.setdefault(y_riga, []).append(w)
            
                righe_estratte = []
                for y in sorted(righe):
                    riga = sorted(righe[y], key=lambda w: w['x0'])
                    riga_str = ""
                    last_x1 = None
                    for w in riga:
                        if last_x1 is not None:
                            gap = w['x0'] - last_x1
                            if gap > 2:
                                riga_str += " " * int(gap // 4.56)
                        riga_str += w['text']
                        last_x1 = w['x1']
                    righe_estratte.append(riga_str)
    for riga in righe_estratte:
        print(riga)           

#print(righe_estratte)