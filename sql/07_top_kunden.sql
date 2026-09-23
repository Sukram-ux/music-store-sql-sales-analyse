-- Top 10 Kunden nach Gesamtumsatz, mit Rangfolge
SELECT
    c.CustomerId,
    c.FirstName || ' ' || c.LastName AS kunde,
    c.Country AS land,
    SUM(i.Total) AS umsatz,
    RANK() OVER (ORDER BY SUM(i.Total) DESC) AS rang
FROM customers c
JOIN invoices i ON i.CustomerId = c.CustomerId
GROUP BY c.CustomerId, kunde, land
ORDER BY rang
LIMIT 10;

-- Erkenntnis: Die umsatzstärksten Einzelkunden kommen aus unterschiedlichen Ländern
-- (Helena Holy/Tschechien $49,62, Richard Cunningham/USA $47,62, Luis Rojas/Chile $46,62) -
-- die USA-Dominanz im Länderranking entsteht durch viele Kunden, nicht durch wenige Großkunden.
