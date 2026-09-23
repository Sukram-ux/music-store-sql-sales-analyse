-- Top 10 Länder nach Umsatz
SELECT
    BillingCountry AS land,
    SUM(Total) AS umsatz,
    COUNT(*) AS anzahl_bestellungen
FROM invoices
GROUP BY BillingCountry
ORDER BY umsatz DESC
LIMIT 10;

-- Erkenntnis: USA führt klar vor Kanada und Frankreich
-- (USA $523,06/91 Bestellungen, Canada $303,96/56, France $195,10/35).
