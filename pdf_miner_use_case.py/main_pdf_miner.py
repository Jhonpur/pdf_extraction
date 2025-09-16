# Import extract_text function from the pdfminer.six library
from pdfminer.high_level import extract_text

# Specify the PDF file you want to extract text from
pdf_file_dip_3 = r'C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf'

# Extract text from the PDF
text = extract_text(pdf_file_dip_3)

# Removing any empty lines in the document
# Split the text into lines and filter out empty lines
lines = [line.strip() for line in text.splitlines() if line.strip()]

# Join the non-empty lines back together with newline characters
cleaned_text = '\n'.join(lines)

# Print the cleaned text
print(cleaned_text)

#print(text)