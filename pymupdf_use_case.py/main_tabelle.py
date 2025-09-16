# import package PyMuPDF
import fitz  

# Open some document, for example a PDF (could also be EPUB, XPS, etc.)
doc = fitz.open(r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf")

# Load a desired page. This works via 0-based numbers
page = doc[0]

# Look for tables on this page and display the table count
tabs = page.find_tables()
print(f"{len(tabs.tables)} table(s) on {page}")

# Select the first table
tab = tabs[0]

df = tab.to_pandas()
print("Table:")
print(df)