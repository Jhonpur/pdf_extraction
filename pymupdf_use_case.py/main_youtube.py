import pymupdf

doc = pymupdf.open(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")

print(doc.metadata)

print("========================================================================================================================================================")

page_one = doc[0]

find = page_one.find_tables()

table1 = find.tables[0]

print(table1.extract())