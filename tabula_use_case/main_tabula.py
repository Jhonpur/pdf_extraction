import tabula

pdf_path = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf"

#dfs = tabula.read_pdf(pdf_path, pages="all", output_format =None)
dfs = tabula.read_pdf(pdf_path, stream=True,pages="all",output_format =None)
print(dfs)