import pdfplumber
import re
import pandas  as pd

loc = r"C:\Users\lorenzo.pourpour\OneDrive - AGM Solutions\Desktop\pdf_extraction\Azienda 200 dip 22 - mese 01.2025_clean_all.pdf"

"""with pdfplumber.open(loc) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

    for line in text.split('\n'):
        print(line)
"""

"""tables = []
with pdfplumber.open(loc) as pdf:
    for page in pdf.pages:
        tables_on_page = page.extract_tables({
            'vertical_strategy':'text',
            'horizontal_strategy':'text',
            'intersection_x_tolerance':10,
            'intersection_y_tolerance':10,
        })

        if tables_on_page:
            for table in tables_on_page:
                if table:
                    tables.append({
                        'page':pdf.pages.index(page) + 1,
                        'data':table

                    })

for table in tables:
    print('page:',table['page'])
    print(pd.DataFrame(table['data']))"""



# Dizionario risultati. con questo script si va ad estrare in modo efficiente : netto al mese, totale competenze e totale trattenute nella busta paga
estratti = {
    "nome": None,
    "periodo": None,
    "paga_base": None,
    "totale_competenze": None,
    "totale_trattenute": None,
    "netto_mese": None,
    "tfr": None
}

with pdfplumber.open(loc) as pdf:
    for page in pdf.pages:
        text = page.extract_text()

        if not text:
            continue

        # Nome dipendente
        if not estratti["nome"]:
            match_nome = re.search(r"\d{6,}\s+([A-Z]+\s+[A-Z]+)", text)
            if match_nome:
                estratti["nome"] = match_nome.group(1).title()

        # Periodo di riferimento
        if not estratti["periodo"]:
            match_periodo = re.search(r"(Gennaio|Febbraio|Marzo|Aprile|Maggio|Giugno|Luglio|Agosto|Settembre|Ottobre|Novembre|Dicembre)\s+\d{4}", text)
            if match_periodo:
                estratti["periodo"] = match_periodo.group(0)

        # Paga base
        if not estratti["paga_base"]:
            match_paga = re.search(r"PAGA BASE\s+([\d.,]+)", text)
            if match_paga:
                estratti["paga_base"] = match_paga.group(1)

        # Totale competenze
        match_comp = re.search(r"TOTALE.?COMPETENZE\s+([\d.,]+)", text)
        if match_comp:
            estratti["totale_competenze"] = match_comp.group(1)

        # Totale trattenute
        match_tratt = re.search(r"TOTALE.?TRATTENUTE\s+([\d.,]+)", text)
        if match_tratt:
            estratti["totale_trattenute"] = match_tratt.group(1)

        # Netto mese
        match_netto = re.search(r"NETTO.?DEL.?MESE\s+([\d.,]+)", text)
        if match_netto:
            estratti["netto_mese"] = match_netto.group(1)

        # TFR
        match_tfr = re.search(r"T\.?F\.?R\.?\s+([\d.,]+)", text)
        if match_tfr:
            estratti["tfr"] = match_tfr.group(1)

print("📄 Dati estratti dalla busta paga:")
for k, v in estratti.items():
    print(f"{k}: {v}")

