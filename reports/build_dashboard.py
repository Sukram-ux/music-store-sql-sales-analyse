"""Erzeugt reports/dashboard.html aus data/chinook.db (reine Standardbibliothek).

Aufruf (im Projektordner):  python reports/build_dashboard.py
"""
import sqlite3
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "chinook.db"
OUT = ROOT / "reports" / "dashboard.html"

ACCENT = "#2563eb"
MUTED = "#cbd5e1"


def q(con, sql):
    return con.execute(sql).fetchall()


def usd(v, d=0):
    s = f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"${s}"


def hbar(rows, w=400, label_w=115, bar_h=22, gap=8, highlight=None):
    """Horizontale Balken; rows = [(label, value)]. highlight = Anzahl akzentuierter Balken."""
    mx = max(v for _, v in rows)
    plot_w = w - label_w - 70
    h = len(rows) * (bar_h + gap)
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" width="100%">']
    for i, (lab, v) in enumerate(rows):
        y = i * (bar_h + gap)
        bw = max(2, plot_w * v / mx)
        fill = ACCENT if highlight is None or i < highlight else MUTED
        out.append(
            f'<text x="{label_w - 8}" y="{y + bar_h / 2 + 4}" text-anchor="end" class="lbl">{escape(lab)}</text>'
            f'<rect x="{label_w}" y="{y}" width="{bw:.1f}" height="{bar_h}" rx="3" fill="{fill}"/>'
            f'<text x="{label_w + bw + 6}" y="{y + bar_h / 2 + 4}" class="val">{usd(v)}</text>'
        )
    out.append("</svg>")
    return "".join(out)


def line_chart(points, w=1040, h=260):
    """points = [(label 'YYYY-MM', value)]."""
    ml, mr, mt, mb = 48, 16, 12, 28
    mx = max(v for _, v in points)
    top = (int(mx / 20) + 1) * 20
    n = len(points)
    px = lambda i: ml + (w - ml - mr) * i / (n - 1)
    py = lambda v: mt + (h - mt - mb) * (1 - v / top)
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" width="100%">']
    for t in range(0, top + 1, 20):
        out.append(
            f'<line x1="{ml}" x2="{w - mr}" y1="{py(t):.1f}" y2="{py(t):.1f}" class="grid"/>'
            f'<text x="{ml - 8}" y="{py(t) + 4:.1f}" text-anchor="end" class="lbl">{t}</text>'
        )
    for i, (lab, _) in enumerate(points):
        if lab.endswith("-01"):
            out.append(f'<text x="{px(i):.1f}" y="{h - 8}" text-anchor="middle" class="lbl">{lab[:4]}</text>')
    d = " ".join(f"{'M' if i == 0 else 'L'}{px(i):.1f},{py(v):.1f}" for i, (_, v) in enumerate(points))
    out.append(f'<path d="{d}" fill="none" stroke="{ACCENT}" stroke-width="2" stroke-linejoin="round"/>')
    out.append("</svg>")
    return "".join(out)


def pareto(rows, w=1040, h=280, top_n=15):
    """Balken je Genre + kumulierte Linie (%)."""
    total = sum(v for _, v in rows)
    rows = rows[:top_n]
    ml, mr, mt, mb = 48, 44, 12, 70
    n = len(rows)
    mx = max(v for _, v in rows)
    slot = (w - ml - mr) / n
    ph = h - mt - mb
    out = [f'<svg viewBox="0 0 {w} {h}" role="img" width="100%">']
    for p in (0, 25, 50, 75, 100):
        y = mt + ph * (1 - p / 100)
        out.append(
            f'<line x1="{ml}" x2="{w - mr}" y1="{y:.1f}" y2="{y:.1f}" class="grid"/>'
            f'<text x="{w - mr + 6}" y="{y + 4:.1f}" class="lbl">{p} %</text>'
        )
    cum, pts = 0, []
    for i, (lab, v) in enumerate(rows):
        cum += v
        x = ml + slot * i
        bh = ph * v / (mx * 1.0)
        fill = ACCENT if i < 6 else MUTED
        out.append(f'<rect x="{x + 6:.1f}" y="{mt + ph - bh:.1f}" width="{slot - 12:.1f}" height="{bh:.1f}" rx="3" fill="{fill}"/>')
        out.append(
            f'<text transform="translate({x + slot / 2:.1f},{h - mb + 12}) rotate(-40)" text-anchor="end" class="lbl">{escape(lab)}</text>'
        )
        pts.append((x + slot / 2, mt + ph * (1 - cum / total)))
    d = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f},{y:.1f}" for i, (x, y) in enumerate(pts))
    out.append(f'<path d="{d}" fill="none" stroke="currentColor" stroke-width="2"/>')
    for x, y in pts:
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="currentColor"/>')
    out.append("</svg>")
    return "".join(out)


def main():
    con = sqlite3.connect(DB)
    total, orders = q(con, "SELECT SUM(Total), COUNT(*) FROM invoices")[0]
    customers = q(con, "SELECT COUNT(DISTINCT CustomerId) FROM invoices")[0][0]
    avg_order = q(
        con,
        "SELECT AVG(s) FROM (SELECT SUM(UnitPrice*Quantity) s FROM invoice_items GROUP BY InvoiceId)",
    )[0][0]
    genres = q(
        con,
        """SELECT g.Name, SUM(ii.UnitPrice*ii.Quantity) u FROM invoice_items ii
           JOIN tracks t ON t.TrackId=ii.TrackId JOIN genres g ON g.GenreId=t.GenreId
           GROUP BY g.Name ORDER BY u DESC""",
    )
    months = q(con, "SELECT strftime('%Y-%m',InvoiceDate), SUM(Total) FROM invoices GROUP BY 1 ORDER BY 1")
    countries = q(
        con, "SELECT BillingCountry, SUM(Total) u FROM invoices GROUP BY 1 ORDER BY u DESC LIMIT 10"
    )
    customers_top = q(
        con,
        """SELECT c.FirstName||' '||c.LastName||' ('||c.Country||')', SUM(i.Total) u
           FROM customers c JOIN invoices i ON i.CustomerId=c.CustomerId
           GROUP BY c.CustomerId ORDER BY u DESC LIMIT 10""",
    )
    reps = q(
        con,
        """SELECT e.FirstName||' '||e.LastName, SUM(ii.UnitPrice*ii.Quantity) u
           FROM employees e JOIN customers c ON c.SupportRepId=e.EmployeeId
           JOIN invoices i ON i.CustomerId=c.CustomerId JOIN invoice_items ii ON ii.InvoiceId=i.InvoiceId
           GROUP BY e.EmployeeId ORDER BY u DESC""",
    )
    first, last = months[0][0], months[-1][0]
    gtotal = sum(v for _, v in genres)
    top6 = sum(v for _, v in genres[:6]) / gtotal * 100

    kpis = [
        ("Gesamtumsatz", usd(total, 2)),
        ("Bestellungen", f"{orders:,}".replace(",", ".")),
        ("Ø Bestellwert", usd(avg_order, 2)),
        ("Kunden", str(customers)),
        ("Top-6-Genres", f"{top6:.1f} %".replace(".", ",")),
    ]
    kpi_html = "".join(f'<div class="kpi"><span>{k}</span><b>{v}</b></div>' for k, v in kpis)

    html = f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Vertriebsdashboard Musik-Online-Shop</title>
<style>
:root{{--bg:#f8fafc;--card:#fff;--ink:#0f172a;--mut:#64748b;--line:#e2e8f0}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0b1220;--card:#131c2e;--ink:#e2e8f0;--mut:#94a3b8;--line:#243049}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,sans-serif}}
main{{max-width:1120px;margin:0 auto;padding:24px 16px 40px}}
h1{{font-size:24px;margin:0}}.sub{{color:var(--mut);margin:4px 0 20px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:16px}}
.kpi,.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px}}
.kpi span{{display:block;color:var(--mut);font-size:13px}}.kpi b{{font-size:24px}}
.grid2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:16px;margin-top:16px}}
.card h2{{font-size:15px;margin:0 0 2px}}.card p{{color:var(--mut);font-size:13px;margin:0 0 10px}}
.lbl{{font-size:11px;fill:var(--mut)}}.val{{font-size:11px;fill:var(--ink)}}.grid{{stroke:var(--line)}}
footer{{color:var(--mut);font-size:12px;margin-top:20px}}
</style></head><body><main>
<h1>Vertriebsdashboard Musik-Online-Shop</h1>
<p class="sub">Chinook-Datenbank · {first} bis {last} · Umsätze in USD</p>
<div class="kpis">{kpi_html}</div>
<div class="card"><h2>Umsatz je Genre mit kumuliertem Anteil</h2>
<p>Die 6 blau markierten Genres erwirtschaften {top6:.1f} % des Umsatzes (Linie = kumulierter Anteil, rechte Achse).</p>{pareto(genres)}</div>
<div class="card" style="margin-top:16px"><h2>Monatlicher Umsatz</h2><p>Kein klarer Trend, Schwankung zwischen den Monaten.</p>{line_chart(months)}</div>
<div class="grid2">
<div class="card"><h2>Top 10 Länder</h2><p>USA führt vor Kanada und Frankreich.</p>{hbar(countries, highlight=3)}</div>
<div class="card"><h2>Top 10 Kunden</h2><p>Spitzenkunden kommen aus verschiedenen Ländern.</p>{hbar(customers_top, label_w=185, highlight=3)}</div>
<div class="card"><h2>Umsatz je Sales Support Agent</h2><p>Ausgeglichen, bei ca. 140 Bestellungen je Person nicht belastbar unterscheidbar.</p>{hbar(reps)}</div>
</div>
<footer>Erzeugt mit reports/build_dashboard.py aus data/chinook.db · Abfragen siehe sql/</footer>
</main></body></html>"""
    OUT.write_text(html, encoding="utf-8")
    print("geschrieben:", OUT)


if __name__ == "__main__":
    main()
