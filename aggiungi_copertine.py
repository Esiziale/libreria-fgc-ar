"""
Aggiunge copertine Open Library ai file .md della libreria.
Esegui dalla cartella fgc_ar:  python aggiungi_copertine.py
"""

import os, re, time, urllib.request, urllib.parse, json

CARTELLA = "content/libreria"
PAUSA    = 0.4   # secondi tra una richiesta e l'altra (rispetta i limiti API)

def cerca_copertina(titolo, autore):
    try:
        query = urllib.parse.urlencode({"title": titolo, "author": autore, "limit": 3, "fields": "cover_i,title"})
        url   = f"https://openlibrary.org/search.json?{query}"
        req   = urllib.request.Request(url, headers={"User-Agent": "FGC-Arezzo-Libreria/1.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read())
        for doc in data.get("docs", []):
            cid = doc.get("cover_i")
            if cid:
                return f"https://covers.openlibrary.org/b/id/{cid}-M.jpg"
    except Exception as e:
        print(f"  ⚠ errore API: {e}")
    return None

def leggi_frontmatter(testo):
    """Restituisce (frontmatter_dict_raw, body) come stringhe."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)", testo, re.DOTALL)
    if not m:
        return None, testo
    return m.group(1), m.group(2)

def ha_copertina(fm):
    return bool(re.search(r'^copertina:\s*"https?://', fm, re.MULTILINE))

def aggiungi_copertina(fm, url):
    # Sostituisce copertina: "" con copertina: "url"
    return re.sub(r'^(copertina:\s*)""', f'\\1"{url}"', fm, flags=re.MULTILINE)

# ─────────────────────────────────────────────
files = [f for f in os.listdir(CARTELLA) if f.endswith(".md") and f != "_index.md"]
print(f"Trovati {len(files)} libri. Avvio ricerca copertine…\n")

trovate = 0
non_trovate = 0
saltate = 0

for nome in sorted(files):
    path = os.path.join(CARTELLA, nome)
    with open(path, encoding="utf-8") as f:
        testo = f.read()

    fm, body = leggi_frontmatter(testo)
    if fm is None:
        print(f"  ⚠ {nome}: frontmatter non trovato, salto")
        saltate += 1
        continue

    if ha_copertina(fm):
        saltate += 1
        continue

    # Estrae titolo e autore dal frontmatter
    titolo_m = re.search(r'^title:\s*"(.+)"', fm, re.MULTILINE)
    autore_m = re.search(r'^autore:\s*"(.+)"', fm, re.MULTILINE)
    if not titolo_m:
        saltate += 1
        continue

    titolo = titolo_m.group(1)
    autore = autore_m.group(1) if autore_m else ""

    print(f"  🔍 {titolo[:45]:<45} ", end="", flush=True)
    url = cerca_copertina(titolo, autore)

    if url:
        nuovo_fm = aggiungi_copertina(fm, url)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"---\n{nuovo_fm}\n---\n{body}")
        print(f"✅ trovata")
        trovate += 1
    else:
        print(f"— non trovata")
        non_trovate += 1

    time.sleep(PAUSA)

print(f"""
──────────────────────────────
✅ Copertine trovate:    {trovate}
— Non trovate:           {non_trovate}
⏭ Saltate (già ok):     {saltate}
──────────────────────────────
Ora fai:
  git add .
  git commit -m "aggiunta copertine open library"
  git push origin main
""")
