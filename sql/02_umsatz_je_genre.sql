-- Umsatz und Bestellanzahl je Musik-Genre
SELECT
    g.Name AS genre,
    SUM(ii.UnitPrice * ii.Quantity) AS umsatz,
    COUNT(DISTINCT ii.InvoiceId) AS anzahl_bestellungen
FROM invoice_items ii
JOIN tracks t ON ii.TrackId = t.TrackId
JOIN genres g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY umsatz DESC;

-- Erkenntnis: Rock dominiert mit $826,65 klar vor Latin ($382,14) und Metal ($261,36).
