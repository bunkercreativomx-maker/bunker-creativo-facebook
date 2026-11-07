import datetime as dt, html, json
from spec import DAYS, START
d0=dt.date.fromisoformat(START); dn=['Lun','Mar','Mié','Jue','Vie','Sáb','Dom']
rows=[];cards=[]
for i,d in enumerate(DAYS):
    f=d0+dt.timedelta(days=i); d['date']=f.isoformat(); d['n']=i+1
    e=lambda s: html.escape(s)
    lbl=f"{dn[f.weekday()]} {f.day}/{f.month}"
    rows.append(f"<tr><td>{i+1}</td><td>{lbl}</td><td><span class='fmt'>{d['fmt']}</span></td><td>{e(d['pilar'])}</td><td><b>{e(d['title'])}</b></td><td>{e(d['price']) or '—'}</td><td>{e(d['cta'])}</td></tr>")
    vo=' '.join(d['vo'])
    cards.append(f"""<details id="d{i+1}"><summary><b>Día {i+1} · {lbl}</b> · {d['fmt']} · {e(d['pilar'])} — {e(d['title'])}</summary>
<div class=g><div><h4>En pantalla</h4><p class=t>{e(d['title'])}</p><p>{e(d['support'])}</p><p><b>{e(d['price'])}</b> {('· ' if d['price'] else '')}CTA: {e(d['cta'])}</p>
<h4>A quién / qué vendemos</h4><p>{e(d['aud'])}</p><h4>Visual</h4><p>{e(d['visual'])}</p></div>
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
</style><main><p class=sub>Plan para aprobación · borrador</p><h1>Bunker Creativo · <em>30 días</em> de video con voz</h1>
<p class=sub>Facebook + Instagram · 9 nov → 8 dic 2026 · español MX · 1 video HyperFrames por día (~15–20 s)</p>
<div class=box><b>Cómo es cada pieza:</b> foto real distinta por día (o captura real de un sitio del portafolio) + texto animado con la marca (navy, naranja, verde lima, Cabinet Grotesk) + voz en off + música de fondo + CTA WhatsApp 656 682 5587. Se entrega MP4 y una imagen fija (último frame).<br>
<b>Formatos:</b> 15 en 4:5 (días impares) + 15 en 1:1 (días pares). Mismo MP4 para FB e IG (en IG se publica como Reel).<br>
<b>Mezcla:</b> 8 dolor/educación · 10 servicios (7 con precio real del sitio) · 4 casos reales del portafolio · 4 engagement · 4 marca/confianza/cierre. Digital primero; imprenta/coroplast solo 3 días.<br>
<b>Datos:</b> todos los precios salen de bunkercreativomx.com (Pack Despegue $5,900, paquetes $1,200 / $1,800 / $2,900, invitaciones $790 / $1,490, coroplast desde $380). Nada inventado: sin % de resultados ni testimonios.</div>
<div class=tw><table><tr><th>#</th><th>Fecha</th><th>Formato</th><th>Pilar</th><th>Texto en pantalla</th><th>Precio</th><th>CTA</th></tr>{''.join(rows)}</table></div>
<h2>Detalle por día (voz + caption)</h2>{''.join(cards)}</main></html>"""
open('index.html','w').write(page); print('ok')
