# Vertriebsanalyse Musik-Online-Shop (Chinook)

SQL-basierte Vertriebsanalyse eines fiktiven digitalen Musik-Online-Shops: Umsatztreiber nach Genre, Mitarbeiter-Performance, Zeitverlauf und wertvollste Kunden – mit datenbasierten Handlungsempfehlungen für das Sales-Management.

## Business-Kontext

Das Sales-Management möchte verstehen, welche Produkte, Mitarbeiter und Kunden den Vertriebserfolg treiben, um Ressourcen und Sortimentsentscheidungen datenbasiert zu steuern. Leitfragen:

1. Welche Genres und Künstler erzielen den meisten Umsatz?
2. Welche Mitarbeiter (Sales Support Agents) haben die beste Verkaufsperformance?
3. Wie entwickelt sich der Umsatz über Zeit und nach Land?
4. Wer sind die umsatzstärksten Kunden?

Details siehe [`docs/PROBLEM_STATEMENT.md`](docs/PROBLEM_STATEMENT.md).

## Daten

- **Quelle:** [Chinook-Datenbank](https://www.sqlitetutorial.net/sqlite-sample-database/) – eine frei verfügbare Beispieldatenbank eines digitalen Musikvertriebs, als SQLite-Datei (`data/chinook.db`)
- **Struktur:** 11 relational verknüpfte Tabellen (u. a. `customers`, `invoices`, `invoice_items`, `tracks`, `albums`, `artists`, `genres`, `employees`)
- **Umfang:** 59 Kunden, 412 Rechnungen, 2.240 Rechnungspositionen, 3.503 Titel
- **Zeitraum:** Januar 2009 – Dezember 2013

## Methodik

Alle Analysen wurden als dokumentierte SQL-Abfragen umgesetzt (Tool: [DB Browser for SQLite](https://sqlitebrowser.org/)), jede mit einem kurzen Erkenntnis-Kommentar versehen:

| Datei | Inhalt |
|---|---|
| [`sql/01_data_understanding.sql`](sql/01_data_understanding.sql) | Zeilenanzahlen und Stichproben der Kerntabellen |
| [`sql/02_umsatz_je_genre.sql`](sql/02_umsatz_je_genre.sql) | Umsatz je Genre (JOIN über 3 Tabellen) |
| [`sql/03_umsatzanteil_genre.sql`](sql/03_umsatzanteil_genre.sql) | Umsatzanteil je Genre in % (CTE + Window Function) |
| [`sql/04_umsatz_je_mitarbeiter.sql`](sql/04_umsatz_je_mitarbeiter.sql) | Umsatz je Vertriebsmitarbeiter (JOIN über 4 Tabellen) |
| [`sql/05_umsatz_zeitverlauf.sql`](sql/05_umsatz_zeitverlauf.sql) | Monatlicher Umsatzverlauf |
| [`sql/06_umsatz_je_land.sql`](sql/06_umsatz_je_land.sql) | Top 10 Länder nach Umsatz |
| [`sql/07_top_kunden.sql`](sql/07_top_kunden.sql) | Top 10 Kunden mit Rangfolge (Window Function `RANK()`) |
| [`sql/08_kumulierter_umsatz_genre.sql`](sql/08_kumulierter_umsatz_genre.sql) | Kumulierter Umsatzanteil je Genre (laufende Summe) |
| [`sql/09_durchschnittlicher_bestellwert.sql`](sql/09_durchschnittlicher_bestellwert.sql) | Durchschnittlicher Bestellwert (Subquery) |

## Wichtigste Erkenntnisse

- **Starkes Pareto-Muster bei Genres:** Nur 6 von ca. 25 Genres (Rock, Latin, Metal, Alternative & Punk, TV Shows, Jazz) erwirtschaften **80,9 %** des Gesamtumsatzes. Rock allein macht 35,5 % aus.
- **Ausgeglichene Mitarbeiter-Performance:** Die drei Sales Support Agents erzielen ähnliche Umsätze (833 $ / 775 $ / 720 $), ungefähr proportional zu ihrer Bestellanzahl – kein auffälliger Leistungsunterschied. Bei nur ~140 Bestellungen pro Person ist der Unterschied statistisch nicht belastbar genug für eine Handlungsempfehlung.
- **Länder-Dominanz durch Volumen, nicht durch Großkunden:** Die USA führen das Länderranking klar an, aber die umsatzstärksten *Einzelkunden* kommen aus unterschiedlichen Ländern (Tschechien, USA, Chile) – die USA-Führung entsteht durch viele Kunden, nicht durch wenige Großabnehmer.
- **Niedriger durchschnittlicher Bestellwert:** $5,65 pro Bestellung – Kunden kaufen im Schnitt nur wenige Einzeltitel pro Kauf.

## Handlungsempfehlungen

| # | Befund | Empfehlung | Messbares Ziel |
|---|---|---|---|
| 1 | 6 von ~25 Genres erwirtschaften 80,9 % des Umsatzes | Marketing-/Einkaufsbudget stärker auf Top-6-Genres fokussieren, Nischen-Genres aber beibehalten (digitale Lagerkosten ~0) | Umsatzanteil der Top-6-Genres um 3–5 Prozentpunkte in 2 Quartalen steigern |
| 2 | Durchschnittlicher Bestellwert nur $5,65 | Cross-Selling/Bundle-Angebote einführen (z. B. Rabatt ab 3 Titeln aus demselben Album/Genre) | Durchschnittlichen Bestellwert um ≥10 % (auf ca. $6,20) in 6 Monaten steigern |
| 3 | Umsatzstärkste Einzelkunden kommen aus kleineren Märkten (Tschechien, Chile) | Gezielte Testkampagne in 3–5 Märkten mit auffällig hohem Einzelkundenwert | Neukundenzahl in Testmärkten um definierten Zielwert (z. B. +20 %) in 6 Monaten steigern |

**Bewusst keine Empfehlung zu den Mitarbeitern:** Der kleine Unterschied zwischen den drei Sales-Support-Agents ist bei der geringen Fallzahl (~140 Bestellungen je Person) statistisch nicht von Zufallsstreuung zu unterscheiden – eine Empfehlung wäre hier nicht durch die Daten gedeckt.

## Projektstruktur

```
├── data/
│   └── chinook.db             # SQLite-Datenbank (11 verknüpfte Tabellen)
├── docs/
│   └── PROBLEM_STATEMENT.md   # Business-Kontext, Leitfragen, Scope
├── sql/                       # Dokumentierte SQL-Abfragen (01-09)
├── notebooks/                 # (optional, für weiterführende Auswertungen)
├── reports/                   # (optional, für Dashboard/Exporte)
└── README.md
```

## Setup & Reproduzierbarkeit

1. [DB Browser for SQLite](https://sqlitebrowser.org/) installieren (kostenlos)
2. `data/chinook.db` in DB Browser öffnen
3. Die Abfragen aus `sql/` im Tab "SQL ausführen" nacheinander (01 bis 09) ausführen

## Einschränkungen (Limitations)

- Die Mitarbeiter-Analyse basiert auf einer sehr kleinen Stichprobe (nur 3 Mitarbeiter) – Aussagen zur Performance sind entsprechend vorsichtig zu interpretieren.
- `Total` in `invoices` wird als gegebener Wert übernommen und nicht gegen die Summe der `invoice_items` validiert.
- Keine Kundensegmentierung (RFM) wie in meinem anderen Portfolio-Projekt (Kundenanalyse Online-Retail) – bewusst außerhalb des Scopes, Fokus liegt auf SQL-Technik und klassischen Vertriebskennzahlen.
- Keine Vorhersagemodelle/Machine Learning – bewusst außerhalb des Scopes.

## Tools

SQLite, DB Browser for SQLite, Git/GitHub.

## Autor

Markus Landwehr
