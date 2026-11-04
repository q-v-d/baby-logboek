# Baby Logboek

Gedeeld logboek voor pampers, voedingen (met borstvoedingstimer links/rechts), slaap, gewicht, temperatuur en medicatie. Eén HTML-bestand, geen backend: de data staat als JSON-bestandjes in een eigen GitHub-repo.

## Opzet (twee repo's)

| Repo | Zichtbaarheid | Inhoud |
|---|---|---|
| `baby-logboek` (deze) | publiek, GitHub Pages aan | `index.html`, deze README |
| `baby-logboek-data` | **privé** | `settings.json`, `data/2026-11.json`, `data/2026-12.json`, … |

GitHub Pages op een gratis account werkt alleen op publieke repo's, daarom staat de code apart van de data. De data-repo wordt nooit gepubliceerd; de app leest en schrijft erin via de GitHub-API met een token dat alleen op jullie telefoons staat.

## Installatie

1. Maak de privé-repo `baby-logboek-data` en zet er de bestanden uit `seed/` in (de historiek vanaf 1 november staat er al in).
2. Maak een **fine-grained personal access token**: GitHub → Settings → Developer settings → Personal access tokens → Fine-grained. Kies *Only select repositories* → `baby-logboek-data`, en bij Permissions → Repository permissions → **Contents: Read and write**. Zet de vervaldatum op 1 jaar.
3. Zet GitHub Pages aan op deze repo (Settings → Pages → Branch `main`, map `/`). De app staat dan op `https://<gebruiker>.github.io/baby-logboek/`; een eigen domein kan via Settings → Pages → Custom domain.
4. Open de app op elke telefoon, vul naam, gebruiker, data-repo en token in. Voeg de pagina toe aan het beginscherm.

Het token staat in de browseropslag van de telefoon (localStorage). Wie het token heeft kan de data-repo lezen en schrijven, dus deel het alleen met je partner en via een veilig kanaal.

## Hoe de data eruitziet

Eén bestand per maand, `data/JJJJ-MM.json`:

```json
{ "events": [
  { "id": "…", "type": "pamper", "sub": "vuil", "kleur": "geel", "ts": "2026-11-04T10:45:00.000Z", "day": "2026-11-04", "by": "Quinten", "note": "" },
  { "id": "…", "type": "voeding", "sub": "borst", "l": 720, "r": 480, "firstSide": "L", "lastSide": "R", "ts": "…", "end": "…", "day": "…" },
  { "id": "…", "type": "voeding", "sub": "fles", "ml": 120, "ts": "…", "day": "…" },
  { "id": "…", "type": "slaap", "ts": "…", "end": "…", "day": "…" },
  { "id": "…", "type": "gewicht", "g": 3510, "ts": "…", "day": "…" },
  { "id": "…", "type": "temp", "c": 37.3, "ts": "…", "day": "…" },
  { "id": "…", "type": "medicatie", "naam": "Vitamine D", "dosis": "1 druppel", "ts": "…", "day": "…" }
] }
```

- `ts` en `end` zijn UTC (ISO 8601); `day` is de lokale dag en bepaalt in welk maandbestand een invoer staat.
- Een lopende borstvoeding heeft `end: null`, `running: "L"|"R"|null` en `runSince`; de app telt de tijd zelf bij. Een lopend dutje heeft `end: null`.
- `l` en `r` zijn seconden per borst. `lastSide` bepaalt met welke borst de volgende voeding start.

Elke wijziging is een commit in de data-repo, dus de geschiedenis is altijd terug te vinden. De app ververst om de 30 seconden en bij het openen van het scherm; twee telefoons die tegelijk schrijven worden samengevoegd (de API weigert een verouderde versie, de app leest opnieuw en probeert opnieuw).
