import pdfplumber
import re
import pandas  as pd

loc_3 = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"

"""with pdfplumber.open(loc) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

    for line in text.split('\n'):
        print(line)
"""

tables = []
with pdfplumber.open(loc_3) as pdf:
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
    print(pd.DataFrame(table['data']))