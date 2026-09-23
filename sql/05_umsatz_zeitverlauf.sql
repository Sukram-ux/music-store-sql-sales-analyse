-- Monatlicher Umsatz über den gesamten Datenzeitraum
SELECT
    strftime('%Y-%m', InvoiceDate) AS jahr_monat,
    SUM(Total) AS umsatz,
    COUNT(*) AS anzahl_bestellungen
FROM invoices
GROUP BY jahr_monat
ORDER BY jahr_monat;

-- Erkenntnis: Datensatz deckt 2009-01 bis 2013-12 ab (5 Jahre).
