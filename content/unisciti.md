---
title: "Unisciti al FGC"
draft: false
---

<style>
.unisciti-wrap{max-width:680px;margin:0 auto;padding:0 0 4rem}
.unisciti-eyebrow{font-family:'IBM Plex Mono',monospace;font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--rosso);margin-bottom:.5rem}
.unisciti-title{font-family:'Bebas Neue',sans-serif;font-size:3rem;line-height:1;color:var(--testo);margin:0 0 1rem;border-bottom:3px solid var(--rosso);padding-bottom:.75rem}
.unisciti-desc{font-family:'IBM Plex Sans',sans-serif;font-size:.95rem;color:var(--testo2);line-height:1.7;margin-bottom:2rem}
.form-group{display:flex;flex-direction:column;gap:.4rem;margin-bottom:1.25rem}
.form-label{font-family:'IBM Plex Mono',monospace;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.form-input,.form-select,.form-textarea{
  background:var(--bg2);
  border:1px solid var(--bordo);
  color:var(--testo);
  font-family:'IBM Plex Sans',sans-serif;
  font-size:.9rem;
  padding:.7rem 1rem;
  outline:none;
  transition:border-color .2s;
  width:100%;
}
.form-input:focus,.form-select:focus,.form-textarea:focus{border-color:var(--rosso)}
.form-textarea{resize:vertical;min-height:100px}
.form-submit{
  background:var(--rosso);
  color:#EDE8DC;
  border:none;
  font-family:'IBM Plex Mono',monospace;
  font-size:.8rem;
  letter-spacing:.12em;
  text-transform:uppercase;
  padding:.85rem 2rem;
  cursor:pointer;
  transition:background .2s;
  margin-top:.5rem;
}
.form-submit:hover{background:var(--rosso-h)}
.form-nota{font-family:'IBM Plex Mono',monospace;font-size:.65rem;color:var(--muted);margin-top:1rem;line-height:1.6}
</style>

<div class="unisciti-wrap">
  <p class="unisciti-eyebrow">Fronte della Gioventù Comunista di Arezzo</p>
  <h1 class="unisciti-title">Unisciti al FGC</h1>
  <p class="unisciti-desc">
    Il FGC è l'organizzazione dei giovani che lottano per un futuro diverso — studenti, lavoratori, precari, abitanti delle periferie. Se vuoi partecipare alle nostre attività, militare con noi o semplicemente saperne di più, scrivici.
  </p>

  <form name="unisciti" method="POST" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="unisciti">
    <p style="display:none"><input name="bot-field"></p>

    <div class="form-group">
      <label class="form-label" for="nome">Nome e cognome *</label>
      <input class="form-input" type="text" id="nome" name="nome" required placeholder="Mario Rossi">
    </div>

    <div class="form-group">
      <label class="form-label" for="eta">Età *</label>
      <input class="form-input" type="number" id="eta" name="eta" required min="14" max="35" placeholder="es. 19">
    </div>

    <div class="form-group">
      <label class="form-label" for="citta">Città / Zona *</label>
      <input class="form-input" type="text" id="citta" name="citta" required placeholder="es. Arezzo, Valdarno…">
    </div>

    <div class="form-group">
      <label class="form-label" for="contatto">Come ti contattare *</label>
      <input class="form-input" type="text" id="contatto" name="contatto" required placeholder="Email o numero di telefono">
    </div>

    <div class="form-group">
      <label class="form-label" for="situazione">Sei studente, lavoratore/a o altro?</label>
      <select class="form-select" id="situazione" name="situazione">
        <option value="">— seleziona —</option>
        <option>Studente scuola superiore</option>
        <option>Studente universitario</option>
        <option>Lavoratore/lavoratrice</option>
        <option>Disoccupato/a o precario/a</option>
        <option>Altro</option>
      </select>
    </div>

    <div class="form-group">
      <label class="form-label" for="messaggio">Vuoi aggiungere qualcosa?</label>
      <textarea class="form-textarea" id="messaggio" name="messaggio" placeholder="Come hai conosciuto il FGC, cosa ti interessa fare, domande…"></textarea>
    </div>

    <button class="form-submit" type="submit">Invia →</button>

    <p class="form-nota">
      I dati inviati vengono usati esclusivamente per ricontattarti. Non vengono ceduti a terzi né usati per altri scopi.
    </p>
  </form>
</div>