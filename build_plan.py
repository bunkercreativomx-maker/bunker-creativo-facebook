import datetime as dt, html, json
from spec import DAYS, START
d0=dt.date.fromisoformat(START); dn=['Lun','Mar','Mié','Jue','Vie','Sáb','Dom']
rows=[];cards=[]
for i,d in enumerate(DAYS):
    f=d0+dt.timedelta(days=i); d['date']=f.isoformat(); d['n']=i+1
    e=lambda s: html.escape(s)
    lbl=f"{dn[f.weekday()]} {f.day}/{f.month}"
    rows.append(f"<tr><td>{i+1}</td><td>{lbl}</td><td><span class='fmt'>{d['fmt']}</span></td><td>{e(d['svc'])}</td><td>{e(d['pilar'])}<br><small style='color:#c8ff2e'>{e(d['palanca'])}</small></td><td><b>{e(d['title'])}</b></td><td>{e(d['price']) or '—'}</td><td>{e(d['cta'])}</td></tr>")
    vo=' '.join(d['vo'])
    cards.append(f"""<details id="d{i+1}"><summary><b>Día {i+1} · {lbl}</b> · {d['fmt']} · {e(d['pilar'])} — {e(d['title'])}</summary>
<div class=g><div><h4>En pantalla</h4><p class=t>{e(d['title'])}</p><p>{e(d['support'])}</p><p><b>{e(d['price'])}</b> {('· ' if d['price'] else '')}CTA: {e(d['cta'])}</p>
<h4>Palanca de valor</h4><p>{e(d['palanca'])}</p><h4>A quién / qué vendemos</h4><p>{e(d['aud'])}</p><h4>Visual</h4><p>{e(d['visual'])}</p></div>
<div><h4>Voz (~{round(len(vo.split())/2.6)} s)</h4><p class=vo>“{e(vo)}”</p><h4>Caption FB/IG</h4><pre>{e(d['cap'])}</pre></div></div></details>""")
json.dump(DAYS,open('calendar.json','w'),ensure_ascii=False,indent=1)
page=f"""<!doctype html><html lang=es><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Bunker Creativo · Calendario 30 días FB + IG</title>
<style>body{{margin:0;background:#0d1430;color:#f3f5ff;font:16px/1.55 system-ui,sans-serif}}main{{max-width:1100px;margin:auto;padding:28px 18px 80px}}
h1{{font-size:2rem;margin:.2em 0;letter-spacing:-.02em}}h1 em{{color:#ff5b1f;font-style:normal}}.sub{{color:#b4bde3}}
.box{{background:#111a3d;border:1px solid #24306a;border-radius:14px;padding:16px 18px;margin:18px 0}}.box b{{color:#c8ff2e}}
table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{padding:8px 6px;border-bottom:1px solid #24306a;text-align:left;vertical-align:top}}th{{color:#8e98c4;font-weight:600}}
.fmt{{background:#ff5b1f;color:#1f0800;border-radius:6px;padding:1px 6px;font-weight:700;font-size:12px}}.tw{{overflow-x:auto}}
details{{background:#111a3d;border-radius:12px;margin:8px 0;padding:10px 14px}}summary{{cursor:pointer}}.g{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}@media(max-width:700px){{.g{{grid-template-columns:1fr}}}}
h4{{margin:12px 0 4px;color:#8e98c4;font-size:12px;text-transform:uppercase;letter-spacing:.08em}}.t{{font-size:1.25rem;font-weight:800}}.vo{{color:#c8ff2e}}pre{{white-space:pre-wrap;font:inherit;background:#0d1430;padding:10px;border-radius:8px;margin:0}}
</style><main><p class=sub>Plan para aprobación · v2 (web + redes, valor Hormozi)</p><h1>Bunker Creativo · <em>30 días</em> de video con voz</h1>
<p class=sub>Facebook + Instagram · 9 nov → 8 dic 2026 · español MX · 1 video HyperFrames por día (~15–20 s)</p>
<div class=box><b>Enfoque v2:</b> solo <b>páginas web (15)</b> y <b>diseño para redes (15)</b>. Fuera imprenta, coroplast e invitaciones.<br>
<b>Copy con la ecuación de valor de Hormozi:</b> Valor = (Resultado soñado × Probabilidad de lograrlo) ÷ (Tiempo de espera × Esfuerzo). Cada día ataca una palanca:<br>
· <b>Resultado soñado</b>: clientes que hoy se lleva la competencia, vender a las 11 pm, verse establecido.<br>
· <b>Probabilidad ↑</b>: 6 casos reales (Solace, Empire, Tlaloc, Mugan + diseños de redes).<br>
· <b>Tiempo ↓</b>: en línea en 72 horas. · <b>Esfuerzo ↓</b>: “tú mandas fotos por WhatsApp, nosotros hacemos todo”, apruebas por WhatsApp.<br>
· <b>Riesgo ↓</b>: sin contratos, cancelas con 5 días, sin contraseñas, pago único, la web es 100% tuya.<br>
· <b>Oferta apilada</b>: todo lo que incluye primero, precio al final (Pack $8,500 → $5,900; redes ≈ $40 al día).<br>
· <b>Costo de no actuar</b>: “cada día sin web le regalas clientes”, “¿$5,900 es caro? compáralo con lo que pierdes”.<br>
<b>Pieza:</b> foto real distinta por día o captura real del sitio + texto animado de marca + voz en off + música + CTA WhatsApp 656 682 5587. 15 en 4:5 + 15 en 1:1; mismo MP4 en FB e IG (Reel).<br>
<b>Datos:</b> precios y promesas salen de bunkercreativomx.com. Sin garantías ni resultados inventados.</div>
<div class=tw><table><tr><th>#</th><th>Fecha</th><th>Formato</th><th>Servicio</th><th>Ángulo · palanca Hormozi</th><th>Texto en pantalla</th><th>Precio</th><th>CTA</th></tr>{''.join(rows)}</table></div>
<h2>Detalle por día (voz + caption)</h2>{''.join(cards)}</main></html>"""
open('index.html','w').write(page); print('ok')
