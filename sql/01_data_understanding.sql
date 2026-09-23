-- Zeilenanzahl der wichtigsten Tabellen auf einen Blick
SELECT 'customers' AS tabelle, COUNT(*) AS anzahl FROM customers
UNION ALL
SELECT 'invoices', COUNT(*) FROM invoices
UNION ALL
SELECT 'invoice_items', COUNT(*) FROM invoice_items
UNION ALL
SELECT 'tracks', COUNT(*) FROM tracks
UNION ALL
SELECT 'albums', COUNT(*) FROM albums
UNION ALL
SELECT 'artists', COUNT(*) FROM artists
UNION ALL
SELECT 'employees', COUNT(*) FROM employees
UNION ALL
SELECT 'genres', COUNT(*) FROM genres;

-- Erkenntnis: customers 59, invoices 412, invoice_items 2240, tracks 3503
-- (Standard-Chinook-Datensatz, bestätigt)

-- Beispieldaten der zentralen Tabellen
SELECT * FROM customers LIMIT 5;
SELECT * FROM invoices LIMIT 5;
SELECT * FROM invoice_items LIMIT 5;
SELECT * FROM tracks LIMIT 5;
