-- Umsatz und Bestellanzahl je Vertriebsmitarbeiter (über zugewiesene Kunden)
SELECT
    e.EmployeeId,
    e.FirstName || ' ' || e.LastName AS mitarbeiter,
    e.Title AS position,
    COUNT(DISTINCT i.InvoiceId) AS anzahl_bestellungen,
    SUM(ii.UnitPrice * ii.Quantity) AS umsatz
FROM employees e
JOIN customers c ON c.SupportRepId = e.EmployeeId
JOIN invoices i ON i.CustomerId = c.CustomerId
JOIN invoice_items ii ON ii.InvoiceId = i.InvoiceId
GROUP BY e.EmployeeId, mitarbeiter, position
ORDER BY umsatz DESC;

-- Erkenntnis: Nur 3 Mitarbeiter haben die Rolle "Sales Support Agent" und damit
-- zugewiesene Kunden. Umsatz relativ ausgeglichen (Jane Peacock $833,04 / 146 Bestellungen,
-- Margaret Park $775,40 / 140, Steve Johnson $720,16 / 126) - kein auffälliger
-- Leistungsunterschied, Verteilung folgt ungefähr der Bestellanzahl.
