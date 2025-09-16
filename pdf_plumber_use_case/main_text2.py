import pdfplumber

loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"

def trova_riga(y, righe, tolleranza=2):
    for y_riga in righe:
        if abs(y - y_riga) <= tolleranza:
            return y_riga
    return y

with pdfplumber.open(loc) as pdf:
    for i, page in enumerate(pdf.pages):
        words = page.extract_words()
        parole_filtrate = [w for w in words if w['x0'] >= 20]
        words_sorted = sorted(parole_filtrate, key=lambda w: (w['top'], w['x0']))
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
                        if gap > 1:
                            riga_str += " " * int(gap // 3)
                    riga_str += w['text']
                    last_x1 = w['x1']
                righe_estratte.append(riga_str)
            print(righe_estratte)

#print(righe_estratte)
