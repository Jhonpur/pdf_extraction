# hash_sensitive.py
import re
import hashlib

def hash_value(s: str) -> str:
    """Calcola l'hash SHA256 di una stringa e restituisce l'esadecimale."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def anonymize_text(text: str) -> str:
    """Anonimizza i dati sensibili presenti in una stringa con hashing."""
    if not text:
        return text

    original = text

    # Codice fiscale italiano (16 caratteri alfanumerici)
    text = re.sub(
        r'\b([A-Za-z]{6}[0-9]{2}[A-Za-z][0-9]{2}[A-Za-z][0-9]{3}[A-Za-z])\b',
        lambda m: hash_value(m.group(1).upper()),
        text
    )

    # P.A.T. INAIL (es. 025054178/60)
    text = re.sub(
        r'\b(\d{3,9}/\d{1,4})\b',
        lambda m: hash_value(m.group(1)),
        text
    )

    # Posizione INPS (8-12 cifre)
    text = re.sub(
        r'\b(\d{8,12})\b',
        lambda m: hash_value(m.group(1)),
        text
    )

    # Date di nascita (formato gg-mm-aaaa o gg/mm/aaaa)
    text = re.sub(
        r'\b(\d{2}[-/]\d{2}[-/]\d{4})\b',
        lambda m: hash_value(m.group(1)),
        text
    )

    # Ragione sociale (se contiene SRL, SPA, ecc. → hash intera riga)
    if re.search(r'\b(srl|spa|snc|sas|sapa)\b', original, re.IGNORECASE):
        return hash_value(original)

    # Indirizzi (via, viale, piazza, corso, strada → hash intera riga)
    if re.search(r'\b(via|viale|piazza|corso|strada)\b', original, re.IGNORECASE):
        return hash_value(original)

    return text

# -------------------------------
# Esempio d'uso
# -------------------------------
if __name__ == "__main__":
    esempi = [
        "MDCLSE74R68F704I",                            # Codice fiscale
        "P.A.T. INAIL: 025054178/60",                 # PAT INAIL
        "Posizione INPS 4932021881",                  # Posizione INPS
        "Data di nascita 28-10-1974",                 # Data
        "G. MARIANI SRL",                             # Ragione sociale
        "VIA VITTORIO EMANUELE 6, MONZA (MB)"         # Indirizzo
    ]
    for e in esempi:
        print(e, "→", anonymize_text(e))
