-- Kumulierter Umsatzanteil je Genre (absteigend sortiert) - beantwortet:
-- wie viele Genres braucht man für 80% des Umsatzes?
WITH umsatz_je_genre AS (
    SELECT
        g.Name AS genre,
        SUM(ii.UnitPrice * ii.Quantity) AS umsatz
    FROM invoice_items ii
    JOIN tracks t ON ii.TrackId = t.TrackId
    JOIN genres g ON t.GenreId = g.GenreId
    GROUP BY g.Name
)
SELECT
    genre,
    umsatz,
    ROUND(100.0 * umsatz / SUM(umsatz) OVER (), 1) AS anteil_prozent,
    ROUND(
        100.0 * SUM(umsatz) OVER (ORDER BY umsatz DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
        / SUM(umsatz) OVER (), 1
    ) AS kumulierter_anteil_prozent
FROM umsatz_je_genre
ORDER BY umsatz DESC;

-- Erkenntnis: Bereits nach 6 von ca. 25 Genres (Rock, Latin, Metal, Alternative & Punk,
-- TV Shows, Jazz) sind 80,9% des Gesamtumsatzes erreicht - starkes Pareto-Muster.
