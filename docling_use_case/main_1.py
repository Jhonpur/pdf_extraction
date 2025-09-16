from docling.document_converter import DocumentConverter
import json

source = r"C:\Users\ange.kadjafomekon\OneDrive - AGM Solutions\Desktop\git_locale\pdf_extraction\Azienda 200 dip 03 - mese 01.2025.pdf" # document per local path or URL
"""converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_dict())  # output: "## Docling Technical Report[...]"
"""


#from docling.document_converter import DocumentConverter
#import json

"""# Inizializza il converter
converter = DocumentConverter()

# Converte il documento
result = converter.convert(source)

# Estrae il contenuto strutturato in dizionario
doc_dict = result.document.export_to_dict()

# Stampa il JSON formattato
print(json.dumps(doc_dict, indent=2, ensure_ascii=False))

# (Opzionale) Salva su file JSON
output_path = "estrazione.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(doc_dict, f, indent=2, ensure_ascii=False)

print(f"✅ Dati salvati in {output_path}")


"""

# Inizializza il converter
converter = DocumentConverter()

# Converte il documento in JSON
result = converter.convert(source)

# Ottieni il contenuto JSON come stringa
json_content = result.model_dump_json(indent=2)

# Stampa il JSON
print(json_content)