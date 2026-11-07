import html, json, os, collections, datetime as dt
from spec3 import pieces
P = pieces(); e = html.escape
DN = ['Lun','Mar','Mié','Jue','Vie','Sáb','Dom']
SLOT = {'R': ('Reel', 'Jab · valor'), 'V': ('Feed', 'Jab · comunidad/prueba'), 'S': ('Venta', 'Right hook')}
PILOT = [x for x in ['d01r', 'd01v', 'd01s', 'd04v'] if os.path.exists(f'pilot/{x}.mp4')]
VO = json.load(open('voices.json'))
VN = {'es-MX-JorgeNeural': 'Voz H (Jorge)', 'es-MX-DaliaNeural': 'Voz M (Dalia)'}
cnt = collections.Counter(p['svc'] for p in P); sl = collections.Counter(p['slot'] for p in P)
json.dump(P, open('calendar3.json', 'w'), ensure_ascii=False, indent=1)
rows = []; det = []
for p in P:
    f = dt.date.fromisoformat(p['date']); lbl = f"{DN[f.weekday()]} {f.day}/{f.month}"
    s = SLOT[p['slot']]
    rows.append(f"<tr class='s{p['slot']}'><td>{p['day']}</td><td>{lbl}</td><td>{p['hour']}</td><td><span class='tag t{p['slot']}'>{s[0]}</span></td><td>{p['fmt'].replace('x', ':')}</td><td>{e(p['svc'])}</td><td><a href='#{p['id']}'><b>{e(p['title'])}</b></a></td><td>{e(p['price']) or '—'}</td></tr>")
    vis = p['scene']
    vis = ('Captura real del sitio ' + vis[5:].replace('web-', '').replace('.webp', '')) if vis.startswith('SITE:') else ('Foto de portafolio ' + vis[6:]) if vis.startswith('PHOTO:') else ('Mosaico de posts reales (CONFIRMAR clientes)') if vis.startswith('MOSAIC') else 'Foto nueva: ' + vis
    det.append(f"""<details id="{p['id']}"><summary><b>{p['id'].upper()}</b> · {lbl} {p['hour']} · {s[0]} {p['fmt'].replace('x', ':')} · {e(p['svc'])} — {e(p['title'])}</summary>
<div class=g><div><h4>En pantalla</h4><p class=t>{e(p['title'])}</p><p>{e(p['sup'])}</p><p><b>{e(p['price'])}</b> CTA: {e(p['cta'])}</p><h4>Visual</h4><p>{e(vis)}</p></div>
<div><h4>Voz</h4><p class=vo>“{e(' '.join(p['vo']))}”</p><h4>Caption FB/IG</h4><pre>{e(p['cap'])}\n\n📲 WhatsApp 656 682 5587</pre></div></div></details>""")
pil = ''.join(f"""<figure><video src="pilot/{x}.mp4?v=1" poster="pilot/{x}.png?v=1" controls playsinline preload="none"></video>
<figcaption><b>{x.upper()}</b> · {SLOT[next(p for p in P if p['id']==x)['slot']][0]} {next(p for p in P if p['id']==x)['fmt'].replace('x', ':')} · {VN.get(VO.get(x), '')}<br><a href="pilot/{x}.mp4" download>Descargar MP4</a></figcaption></figure>""" for x in PILOT)
page = f"""<!doctype html><html lang=es><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Bunker Creativo · 75 piezas FB + IG</title>
<style>body{{margin:0;background:#0d1430;color:#f3f5ff;font:16px/1.55 system-ui,sans-serif}}main{{max-width:1150px;margin:auto;padding:28px 16px 80px}}
h1{{font-size:2rem;margin:.2em 0;letter-spacing:-.02em}}h1 em{{color:#ff5b1f;font-style:normal}}.sub{{color:#b4bde3}}h2{{margin-top:2em}}
.box{{background:#111a3d;border:1px solid #24306a;border-radius:14px;padding:16px 18px;margin:18px 0}}.box b{{color:#c8ff2e}}
table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{padding:7px 6px;border-bottom:1px solid #24306a;text-align:left;vertical-align:top}}th{{color:#8e98c4}}td a{{color:inherit;text-decoration:none}}
.tag{{border-radius:6px;padding:1px 7px;font-weight:700;font-size:12px}}.tR{{background:#c8ff2e;color:#10180a}}.tV{{background:#3a4a8f}}.tS{{background:#ff5b1f;color:#1f0800}}.tw{{overflow-x:auto}}
details{{background:#111a3d;border-radius:12px;margin:8px 0;padding:10px 14px}}summary{{cursor:pointer}}.g{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}@media(max-width:700px){{.g{{grid-template-columns:1fr}}}}
h4{{margin:12px 0 4px;color:#8e98c4;font-size:12px;text-transform:uppercase;letter-spacing:.08em}}.t{{font-size:1.2rem;font-weight:800}}.vo{{color:#c8ff2e}}pre{{white-space:pre-wrap;font:inherit;background:#0d1430;padding:10px;border-radius:8px;margin:0}}
.pil{{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start}}figure{{margin:0;width:260px}}video{{width:100%;border-radius:12px;background:#000}}figcaption{{font-size:13px;color:#b4bde3;margin-top:6px}}figcaption a{{color:#c8ff2e}}
</style><main><p class=sub>Plan para aprobación · v3 (Gary Vee + Hormozi + algoritmo Meta 2026)</p><h1>Bunker Creativo · <em>75 piezas</em> en 30 días</h1>
<p class=sub>Facebook + Instagram · 9 nov → 8 dic 2026 · español MX · todas son video HyperFrames con voz, música y subtítulos (Reels)</p>
<h2>Piloto · día 1 completo + un caso real ({len(PILOT)} videos)</h2><p class=sub>Decide aquí la voz (H o M) y el estilo antes de producir las otras {len(P)-len(PILOT)}.</p><div class=pil>{pil or '<p>Renderizando…</p>'}</div>
<div class=box><b>Cadencia diaria (Gary Vee: jab, jab, jab, right hook):</b><br>
· <b>08:00 Reel 9:16</b> (30) — tip, detrás de cámaras, educación. Cierra con “comenta / guárdalo / mándaselo a alguien”.<br>
· <b>13:00 Feed 4:5 / 1:1</b> (30) — preguntas a la comunidad, casos reales del portafolio, mitos, imprenta.<br>
· <b>19:00 Venta</b> (15, días impares) — oferta apilada estilo Hormozi, precio al final.<br>
<b>Reparto:</b> {', '.join(f'{k} {v}' for k, v in cnt.most_common())} · {sl['R']} Reels · {sl['V']} feed · {sl['S']} venta (≈80% valor / 20% venta).<br>
<b>Algoritmo 2026:</b> se premian comentarios y compartidos por mensaje (no likes) → cada pieza pide comentar o mandar; Reels con subtítulos para verse sin sonido; contenido original (nada reciclado); constancia diaria.<br>
<b>Andromeda (anuncios):</b> 8 casos reales + ofertas distintas = ideas diferentes, no variantes de una foto. Los Reels/ventas que mejor jalen se convierten en anuncios.<br>
<b>Datos:</b> precios y promesas salen de bunkercreativomx.com (Pack $5,900, redes $1,200/$1,800/$2,900/$4,500, invitaciones $1,490, coroplast desde $380). Sin garantías ni resultados inventados.</div>
<h2>Calendario</h2><div class=tw><table><tr><th>Día</th><th>Fecha</th><th>Hora</th><th>Tipo</th><th>Formato</th><th>Servicio</th><th>Texto en pantalla</th><th>Precio</th></tr>{''.join(rows)}</table></div>
<h2>Detalle por pieza (voz + caption)</h2>{''.join(det)}</main></html>"""
open('index.html', 'w').write(page); print('ok', len(P), len(PILOT), dict(cnt))
