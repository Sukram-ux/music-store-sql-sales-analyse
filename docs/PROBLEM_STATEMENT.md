# Problem Statement: Vertriebsanalyse Musik-Online-Shop (Chinook)

## Kontext
Der fiktive Auftraggeber ist ein digitaler Musik-Online-Shop (Datenbasis: Chinook-Datensatz),
der Titel, Alben und Playlists an Kunden weltweit verkauft. Das Sales-Management möchte
verstehen, welche Produkte, Mitarbeiter und Kunden den Vertriebserfolg treiben, um
Ressourcen und Sortimentsentscheidungen datenbasiert zu steuern.

## Leitfragen (Guiding Questions)
1. Welche Genres und Künstler erzielen den meisten Umsatz?
2. Welche Mitarbeiter (Sales Support Agents) haben die beste Verkaufsperformance?
3. Wie entwickelt sich der Umsatz über Zeit und nach Land?
4. Wer sind die umsatzstärksten Kunden?

## Hypothesen (vor der Analyse, noch ungeprüft)
- Ein kleiner Teil der Genres/Künstler erzeugt einen überproportional großen Anteil
  des Umsatzes (ähnliches Pareto-Muster wie in Projekt 1 vermutet).
- Die USA sind vermutlich der umsatzstärkste Markt.
- Der Umsatz verteilt sich relativ gleichmäßig über die Mitarbeiter, da es sich um
  einen Digitalvertrieb ohne regionale Exklusivität handelt (unbestätigte Annahme).

## Scope – was gehört dazu
- SQL-basierte Analyse aller Leitfragen (JOINs, Aggregationen, Window Functions, CTEs)
- Dokumentation jeder Abfrage mit der jeweiligen Erkenntnis
- Handlungsempfehlungen für das Sales-Management
- Optional: Visualisierung ausgewählter Ergebnisse (Python oder einfaches Dashboard)

## Out of Scope – was bewusst NICHT gemacht wird
- Keine Vorhersagemodelle / Machine Learning
- Keine Schreiboperationen an der Datenbank (nur lesende SELECT-Abfragen)
- Keine RFM-Kundensegmentierung wie in Projekt 1 – Fokus liegt hier auf SQL-Technik
  und klassischen Vertriebskennzahlen

## Zielgruppe
- Sales-Management

## Erfolgskriterien
- Mindestens 8–10 dokumentierte SQL-Abfragen, die JOINs über mehrere Tabellen,
  Window Functions und/oder CTEs demonstrieren
- Jede Abfrage mit einer kurzen Erkenntnis (Kommentar) versehen
- Mindestens 3 konkrete, datenbasierte Handlungsempfehlungen
- Vollständig dokumentiertes, reproduzierbares GitHub-Repository
