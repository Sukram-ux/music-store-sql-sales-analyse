-- Durchschnittlicher Bestellwert über alle Rechnungen
SELECT
    ROUND(AVG(rechnungssumme), 2) AS durchschnittlicher_bestellwert
FROM (
    SELECT InvoiceId, SUM(UnitPrice * Quantity) AS rechnungssumme
    FROM invoice_items
    GROUP BY InvoiceId
);

-- Erkenntnis: Durchschnittlicher Bestellwert liegt bei nur $5,65 - Kunden kaufen im
-- Schnitt wenige Einzeltitel pro Bestellung. Ansatzpunkt für Cross-Selling.
