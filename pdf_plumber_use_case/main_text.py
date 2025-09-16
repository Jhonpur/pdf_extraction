import pdfplumber
import re
import pandas  as pd


"""def riga_rilevante(riga):
    # Escludi righe vuote o troppo corte
    if len(riga.strip()) < 3:
        return False
    # Escludi righe con solo simboli o caratteri speciali
    if re.fullmatch(r"[\W_]+", riga.strip()):
        return False
    # Escludi righe che contengono pattern tipici di "sporcizia"
    if re.search(r"(//:p\*|\.d|z\.w|tth|ccu|^\W+$|\*{2,}|^\d+$)", riga):
        return False
    # Escludi righe con solo numeri separati da virgole o punti
    if re.fullmatch(r"[\d.,\s]+", riga.strip()):
        return False
    return True"""


loc_3 = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"
loc_5 = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 06 - mese 01.2025.pdf"
loc_5 = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 05 - mese 01.2025.pdf"
"""with pdfplumber.open(loc) as pdf:
    for i in range(2):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        print("-"*50)
        for line in text.split('\n'):
            print(line)"""


import pdfplumber

#loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"
"""with pdfplumber.open(loc) as pdf:
    for i in range(2):
        page = pdf.pages[i]
        words = page.extract_words()
        # Ordina prima per 'top' (riga), poi per 'x0' (colonna)
        words_sorted = sorted(words, key=lambda w: (round(w['top']), w['x0']))
        # Raggruppa per riga
        righe = {}
        for w in words_sorted:
            y = round(w['top'])
            righe.setdefault(y, []).append(w['text'])
        # Stampa le righe nell'ordine visivo
        for y in sorted(righe):
            print(' '.join(righe[y]))
        print("-"*50)"""



import pdfplumber

"""def trova_riga(y, righe, tolleranza=2):
    for y_riga in righe:
        if abs(y - y_riga) <= tolleranza:
            return y_riga
    return y"""

#loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"
"""with pdfplumber.open(loc) as pdf:
    for i in range(2):
        page = pdf.pages[i]
        words = page.extract_words()
        # Ordina prima per 'top' (riga), poi per 'x0' (colonna)
        words_sorted = sorted(words, key=lambda w: (w['top'], w['x0']))
        # Raggruppa per riga con tolleranza
        righe = {}
        for w in words_sorted:
            y = w['top']
            y_riga = trova_riga(y, righe, tolleranza=2)
            righe.setdefault(y_riga, []).append(w['text'])
        # Stampa le righe nell'ordine visivo
        for y in sorted(righe):
            print(' '.join(righe[y]))
        print("-"*50)"""


import pdfplumber

"""def trova_riga(y, righe, tolleranza=2):
    for y_riga in righe:
        if abs(y - y_riga) <= tolleranza:
            return y_riga
    return y"""

#loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"
"""with pdfplumber.open(loc_3) as pdf:
    for i, page in enumerate(pdf.pages):
        words = page.extract_words()
        # Ordina tutte le parole prima per 'top' (verticale), poi per 'x0' (orizzontale)
        words_sorted = sorted(words, key=lambda w: (w['top'], w['x0']))
        righe = {}
        for w in words_sorted:
            y = w['top']
            y_riga = trova_riga(y, righe, tolleranza=2)
            righe.setdefault(y_riga, []).append((w['x0'], w['text']))
        # Stampa le righe nell'ordine visivo, ordinando le parole da sinistra a destra
        print(f"--- Pagina {i+1} ---")
        for y in sorted(righe):
            riga = [t for _, t in sorted(righe[y], key=lambda x: x[0])]
            print(' '.join(riga))
        print("-" * 50) """       



"""def trova_colonna(x, colonne, tolleranza=2):
    for x_col in colonne:
        if abs(x - x_col) <= tolleranza:
            return x_col
    return x"""

#loc = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"
"""with pdfplumber.open(loc_3) as pdf:
    for i, page in enumerate(pdf.pages):
        words = page.extract_words()
        # Ordina tutte le parole prima per 'x0' (orizzontale), poi per 'top' (verticale)
        words_sorted = sorted(words, key=lambda w: (w['x0'], w['top']))
        colonne = {}
        for w in words_sorted:
            x = w['x0']
            x_col = trova_colonna(x, colonne, tolleranza=2)
            colonne.setdefault(x_col, []).append((w['top'], w['text']))
        print(f"--- Pagina {i+1} ---")
        for x in sorted(colonne):
            colonna = [t for _, t in sorted(colonne[x], key=lambda x: x[0])]
            print(' '.join(colonna))
        print("-" * 50)"""


def trova_riga(y, righe, tolleranza=2):
    for y_riga in righe:
        if abs(y - y_riga) <= tolleranza:
            return y_riga
    return y

with pdfplumber.open(loc_3) as pdf:
    for i, page in enumerate(pdf.pages):
        words = page.extract_words()
        # 1. Filtra via la scrittura laterale (ad esempio x0 < 50)
        parole_filtrate = [w for w in words if w['x0'] >= 20]
        # 2. Ordina per riga (top), poi per colonna (x0)
        words_sorted = sorted(parole_filtrate, key=lambda w: (w['top'], w['x0']))
        righe = {}
        for w in words_sorted:
            y = w['top']
            y_riga = trova_riga(y, righe, tolleranza=2)
            righe.setdefault(y_riga, []).append((w['x0'], w['text']))
        print(f"--- Pagina {i+1} ---")
        for y in sorted(righe):
            riga = [t for _, t in sorted(righe[y], key=lambda x: x[0])]
            print(' '.join(riga))
        print("-" * 50)
        