================================================================================
  LIBRERIA FGC AREZZO — GUIDA AL PROGETTO
  Sito Hugo con tema Blowfish
================================================================================

COME AVVIARE IL SITO IN LOCALE
────────────────────────────────
  hugo serve

COME PUSHARE LE MODIFICHE SU GITHUB (branch dev)
──────────────────────────────────────────────────
  git add .
  git commit -m "descrizione"
  git push origin dev

  Per scaricare aggiornamenti dal remoto:
  git pull origin dev

================================================================================
  STRUTTURA DEI FILE IMPORTANTI
================================================================================

CSS GLOBALE (stile di tutto il sito)
────────────────────────────────────
  assets/css/custom.css
  → Colori, font, header, footer, navbar, card, mobile responsive
  → Classi condivise tra tutte le pagine: .page-wrap .page-hero .page-title
  → Qui si modificano colori principali (variabili --rosso, --bg, --testo, ecc.)

CONFIGURAZIONE SITO
────────────────────
  hugo.toml
  → Titolo sito, menu di navigazione, parametri tema Blowfish

IMMAGINI E FILE STATICI
────────────────────────
  static/images/         → loghi, immagini usate nel sito
  static/favicon.png     → icona tab browser

================================================================================
  LAYOUT DELLE PAGINE
================================================================================

HOMEPAGE (/)
  layouts/index.html
  → Hero con titolo/logo/bottoni, ticker, griglia libri in evidenza,
    sezione eventi, CTA "unisciti"

LIBRERIA (/libreria/)
  layouts/libreria/list.html
  → Tutto in un unico file: layout + CSS + JavaScript
  → La griglia di libri, i filtri, il modal di dettaglio e i placeholder SVG
    sono tutti generati via JS dalla variabile LIBRI (popolata da Hugo)

INIZIATIVE (/iniziative/)
  layouts/iniziative/list.html    → lista di tutte le iniziative
  layouts/iniziative/single.html  → pagina singola di una iniziativa

CINEFORUM (/cineforum/)
  layouts/cineforum/list.html
  → Lista proiezioni (al momento vuota)
  → Campi supportati nel frontmatter: data_proiezione, orario, regia,
    immagine, luogo

CALENDARIO (/calendario/)
  layouts/calendario/list.html
  → Vista lista cronologica + vista mensile a griglia
  → Aggrega automaticamente iniziative e cineforum

PAGINE SINGOLE DEFAULT (es. Unisciti)
  layouts/_default/single.html
  → Usato per tutte le pagine .md senza un layout specifico
  → Titolo + contenuto markdown

FOOTER
  layouts/partials/footer.html

FAVICON
  layouts/partials/favicons.html

================================================================================
  CONTENUTI MODIFICABILI
================================================================================

AGGIUNGERE/MODIFICARE UN LIBRO
  content/libreria/NNN-titolo-slug/index.md

  Campi frontmatter disponibili:
    title:          "Titolo del libro"
    autore:         "Nome Cognome"
    numero_catalogo: 001
    categoria:      "Teoria"       ← usato anche per il filtro
    disponibile:    true / false
    donatore:       "Nome"
    copertina:      "/images/copertina.jpg"   ← opzionale

AGGIUNGERE UN'INIZIATIVA
  content/iniziative/nome-evento.md

  Campi frontmatter disponibili:
    title:       "Titolo"
    date:        2026-03-15
    orario:      "18:00"
    luogo:       "Nome posto"
    immagine:    "/images/foto.jpg"
    instagram:   "https://instagram.com/..."
    sottotitolo: "Testo opzionale sotto il titolo"

AGGIUNGERE UNA PROIEZIONE CINEFORUM
  content/cineforum/nome-film.md

  Campi frontmatter disponibili:
    title:            "Titolo film"
    data_proiezione:  2026-04-20
    orario:           "21:00"
    luogo:            "Nome posto"
    regia:            "Nome regista"
    immagine:         "/images/locandina.jpg"

PAGINA UNISCITI
  content/unisciti.md
  → Testo libero in markdown

================================================================================
  PALETTE COLORI (da custom.css)
================================================================================

  Modalità chiara (default):
    --bg:      #EDE8DC   sfondo principale (carta da manifesto)
    --bg2:     #E0DACC   sfondo card
    --testo:   #0A0A0A   testo principale
    --rosso:   #CC1A1A   colore accento principale
    --muted:   #6B6560   testo secondario/grigio

  Modalità scura:
    --bg:      #0C0C0C
    --testo:   #EDE8DC
    --rosso:   #D92B2B

================================================================================
  FONT USATI
================================================================================

  Bebas Neue       → titoli di pagina, numeri grandi
  IBM Plex Mono    → etichette, badge, metadati, codice
  IBM Plex Sans    → testo corpo, descrizioni

================================================================================
  NOTE
================================================================================

  - La cartella public/ è il sito già compilato da Hugo.
    Va committata insieme alle modifiche perché è quella deployata.
    Dopo modifiche ai layout, ricompila con:  hugo

  - Il tema base è Blowfish (in themes/blowfish/).
    NON modificare i file dentro themes/ — usa i file in layouts/ per
    sovrascrivere solo quello che serve.

  - Il language switcher (IT/EN) è disabilitato. Per riabilitarlo:
    1. assets/css/custom.css → rimuovi la riga ".translation { display:none }"
    2. layouts/partials/header/components/translations.html → decommenta il codice
    3. Aggiungi sezione [languages] in hugo.toml

================================================================================
