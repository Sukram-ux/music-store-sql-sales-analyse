-- Umsatzanteil je Genre in Prozent vom Gesamtumsatz
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
    ROUND(100.0 * umsatz / SUM(umsatz) OVER (), 1) AS anteil_prozent
FROM umsatz_je_genre
ORDER BY umsatz DESC;

-- Erkenntnis: Rock allein macht 35,5% des Gesamtumsatzes aus.
-- Die Top 4 Genres (Rock, Latin, Metal, Alternative & Punk) zusammen: 73,5%.
