import pymupdf

doc = pymupdf.open(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")

print(doc.metadata)

print("========================================================================================================================================================")

for i in range(len(doc)):
    page = doc[i]
    find = page.find_tables()
    for j,tab  in enumerate(find):
        print(f"table{j}")
        table1 = find.tables[j]
        print(table1.extract())