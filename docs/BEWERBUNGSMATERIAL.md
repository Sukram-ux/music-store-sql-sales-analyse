# Bewerbungsmaterial: Vertriebsanalyse Musik-Online-Shop (Chinook)

Persönliches Referenzdokument für Bewerbungen, LinkedIn und Vorstellungsgespräche zu diesem Projekt. Nicht Teil der technischen Projektdokumentation (siehe [`README.md`](../README.md)).

## Für den Lebenslauf (kurz, 3–4 Zeilen)

> **Vertriebsanalyse Musik-Online-Shop (Privates Portfolio-Projekt)**
> SQL (SQLite) | github.com/Sukram-ux/music-store-sql-sales-analyse
> SQL-basierte Analyse einer relationalen Datenbank (11 verknüpfte Tabellen) mit JOINs, CTEs und Window Functions; identifizierte, dass 6 von 25 Produktgenres 81 % des Umsatzes erwirtschaften. 9 dokumentierte SQL-Abfragen und 3 datenbasierte Handlungsempfehlungen für das Sales-Management entwickelt.

## Für LinkedIn / Portfolio-Website (ausführlicher)

> **Vertriebsanalyse mit SQL: Welche Produkte, Kunden und Märkte treiben den Umsatz?**
>
> In diesem Projekt habe ich eine relationale Datenbank eines fiktiven digitalen Musik-Online-Shops (11 verknüpfte Tabellen: Kunden, Rechnungen, Titel, Alben, Künstler, Mitarbeiter) rein mit SQL analysiert – bewusst als Gegenstück zu meinem ersten Portfolio-Projekt, das auf Python/pandas und Power BI setzte. Über mehrstufige JOINs, Common Table Expressions (CTEs) und Window Functions (u. a. `RANK()` und laufende Summen) habe ich Umsatztreiber nach Genre, Mitarbeiter-Performance, Zeitverlauf und Kundenwert herausgearbeitet. Zentrale Erkenntnis: Nur 6 von rund 25 Musik-Genres erwirtschaften über 80 % des Gesamtumsatzes – ein starkes Pareto-Muster, das sich bei der Mitarbeiter-Performance interessanterweise **nicht** zeigt. Aus den Ergebnissen habe ich drei konkrete, messbare Handlungsempfehlungen für das Sales-Management abgeleitet.
>
> **Tech-Stack:** SQL, SQLite, DB Browser for SQLite, Git/GitHub

## Für ein Anschreiben (1–2 Sätze als Baustein)

> In einem eigenständigen SQL-Projekt habe ich eine relationale Datenbank mit mehrstufigen JOINs, CTEs und Window Functions analysiert, um konkrete Vertriebskennzahlen und Handlungsempfehlungen abzuleiten – bewusst ohne den Umweg über Python, um meine SQL-Kenntnisse direkt zu zeigen.

### Wie und wo Links im Anschreiben platzieren

Nicht in den Fließtext einstreuen – wirkt schnell wie eine Linkliste. Stattdessen:

1. **Im Kontaktdaten-Block oben (Briefkopf)**, neben Adresse/Telefon/E-Mail, das GitHub-**Profil** verlinken (nicht einzelne Repos):
   ```
   Markus Landwehr
   [Adresse]
   [Telefon] · [E-Mail]
   GitHub: github.com/Sukram-ux
   ```
2. **Im Fließtext** beim Erwähnen des Projekts keinen rohen Link setzen, sondern sprachlich darauf verweisen: *"...Details dazu finden Sie auf meinem GitHub-Profil."*
3. **Ausnahme, wenn beide Projekte (dieses und das Online-Retail-Projekt) genannt werden sollen:** kurz vor der Grußformel eine kompakte Referenzzeile:
   > Beispiele meiner Arbeit: github.com/Sukram-ux/online-retail-customer-analyse · github.com/Sukram-ux/music-store-sql-sales-analyse

---

## Kernaussagen für Vorstellungsgespräche (ehrlich, aber überzeugend)

### Elevator-Pitch / STAR-Antwort

> "Nach meinem ersten Portfolio-Projekt mit Python und Power BI wollte ich gezielt zeigen, dass ich auch direkt in SQL arbeiten kann – ohne den Umweg über pandas. Ich habe mir dafür eine echte relationale Datenbank vorgenommen, die Chinook-Datenbank eines digitalen Musikvertriebs mit 11 verknüpften Tabellen. Ich habe neun dokumentierte SQL-Abfragen geschrieben – von einfachen JOINs bis zu Common Table Expressions und Window Functions für laufende Summen und Rankings. Die wichtigste Erkenntnis: Nur 6 von rund 25 Genres erwirtschaften über 80 % des Umsatzes. Interessant war aber auch, was ich *nicht* gefunden habe – bei der Mitarbeiter-Performance gab es keinen auffälligen Unterschied, und ich habe bewusst keine Handlungsempfehlung dazu formuliert, weil die Datenmenge dafür zu klein war."

### Einzelne Kernaussagen (belastbar, mit Zahlen)

- "Ich habe eine relationale Datenbank mit 11 Tabellen analysiert und dabei mehrstufige JOINs über bis zu vier Tabellen hinweg geschrieben."
- "Ich beherrsche Window Functions praktisch – sowohl für Rankings (`RANK() OVER`) als auch für laufende Summen (kumulierte Prozentanteile), nicht nur für einfache Aggregationen."
- "Meine Analyse hat gezeigt, dass 6 von ca. 25 Genres 81 % des Umsatzes erwirtschaften – ein deutliches Pareto-Muster, ähnlich wie in meinem anderen Projekt zur Kundensegmentierung."
- "Ich unterscheide bewusst zwischen Mustern, die ich gefunden habe, und solchen, die ich *nicht* gefunden habe – bei der Mitarbeiter-Performance war der Unterschied zu klein, um daraus eine Empfehlung abzuleiten."

### Ehrliche Einschränkungen, wenn kritisch nachgefragt wird

- "Ich habe die `Total`-Spalte der Rechnungstabelle direkt übernommen, statt sie gegen die Summe der Einzelpositionen zu validieren – in einem echten Projekt würde ich diese Datenqualitätsprüfung ergänzen."
- "Die Datenbank ist mit ca. 400 Rechnungen recht klein – bei einer echten, viel größeren Datenbank würde ich zusätzlich auf Indizes und Abfrageperformance achten, was hier noch keine Rolle gespielt hat."
- "Meine Handlungsempfehlungen sind Vorschläge mit messbaren Zielen, keine bewiesenen Erfolgsrezepte – das müsste man im echten Betrieb testen."

---

## Mögliche Interviewfragen zu diesem Projekt

### SQL-Technik
- **"Erklär mir den Unterschied zwischen einer CTE und einer Subquery."** → Inhaltlich austauschbar, CTE (`WITH ... AS`) ist meist lesbarer, besonders bei Wiederverwendung oder mehreren Schritten; du hast beides im Projekt genutzt (CTE in Abfrage 3/8, Subquery in Abfrage 9).
- **"Was macht eine Window Function anders als GROUP BY?"** → `GROUP BY` fasst Zeilen zu einer zusammen, eine Window Function (`OVER (...)`) berechnet einen aggregierten Wert, behält aber jede einzelne Zeile bei. Kannst du an deinem Beispiel (Umsatzanteil je Genre) konkret zeigen.
- **"Wie berechnet man eine laufende Summe / ein Ranking in SQL?"** → `SUM() OVER (ORDER BY ... ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)` bzw. `RANK() OVER (ORDER BY ...)` – beide hast du selbst geschrieben, nicht nur kopiert.
- **"Warum musst du bei GROUP BY alle SELECT-Spalten mit angeben?"** → SQL-Grundregel: nicht-aggregierte Spalten müssen im GROUP BY stehen, sonst ist unklar, welcher Wert pro Gruppe angezeigt werden soll.

### Datenmodell / relationales Denken
- **"Wie bist du vorgegangen, um den richtigen JOIN-Pfad zwischen Mitarbeiter und Umsatz zu finden?"** → Über die Fremdschlüssel-Kette `employees → customers (SupportRepId) → invoices → invoice_items` – zeigt, dass du das Datenmodell verstanden hast, nicht nur Syntax auswendig kennst.

### Business-Verständnis / kritisches Denken
- **"Warum hast du keine Handlungsempfehlung zu den Mitarbeitern gegeben, obwohl es Unterschiede im Umsatz gab?"** → Bewusste Entscheidung: bei nur 3 Mitarbeitern und ~140 Bestellungen pro Person ist der Unterschied statistisch nicht von Zufall zu unterscheiden – eine Empfehlung wäre nicht durch die Daten gedeckt.
- **"Was ist der Unterschied zwischen dem Länder-Ranking und dem Kunden-Ranking, und warum widersprechen sie sich scheinbar nicht?"** → USA führt durch viele Kunden (Volumen), aber die umsatzstärksten Einzelkunden kommen aus verschiedenen Ländern – zwei unterschiedliche Blickwinkel auf dieselben Daten, kein Widerspruch.
