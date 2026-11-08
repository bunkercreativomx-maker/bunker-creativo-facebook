import html, json, os, shutil, datetime as dt
from spec3 import pieces, WA
P = pieces(); e = html.escape
OUT = '/opt/data/hyperframes/bunker-fb/out'
DN = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
MN = ['', 'ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
TIPO = {'R': 'reel', 'V': 'feed', 'S': 'venta'}
os.makedirs('videos', exist_ok=True)
items = []
for n, p in enumerate(sorted(P, key=lambda p: (p['date'], p['hour'])), 1):
    f = dt.date.fromisoformat(p['date'])
    name = f"{n:02d}_{f.day:02d}{MN[f.month]}_{p['hour'].replace(':', '')}_{TIPO[p['slot']]}_{p['id']}"
    shutil.copy(f"{OUT}/{p['id']}.mp4", f"videos/{name}.mp4")
    shutil.copy(f"{OUT}/{p['id']}.png", f"videos/{name}.png")
    wk = (f - dt.date(2026, 11, 9)).days // 7 + 1
    items.append(dict(p, name=name, wk=min(wk, 4), lbl=f"{DN[f.weekday()]} {f.day} {MN[f.month]}",
                      capfull=p['cap'] + f"\n\n📲 WhatsApp {WA}"))
for f in os.listdir('videos'):
    if f.rsplit('.', 1)[0] not in {i['name'] for i in items}: os.remove('videos/' + f)
cards = []
for i in items:
    cards.append(f"""<article class="c w{i['wk']}"><div class=h><b>{i['lbl']} · {i['hour']}</b><span class="tag t{i['slot']}">{TIPO[i['slot']].upper()} {i['fmt'].replace('x', ':')}</span></div>
<video src="videos/{i['name']}.mp4" poster="videos/{i['name']}.png" controls playsinline preload="none"></video>
<p class=t>{e(i['title'])}</p><textarea readonly>{e(i['capfull'])}</textarea>
<div class=b><button onclick="cp(this)">Copiar caption</button><a href="videos/{i['name']}.mp4" download>Descargar MP4</a></div></article>""")
data = json.dumps([{'n': i['name'], 'w': i['wk'], 'c': i['capfull']} for i in items], ensure_ascii=False)
page = f"""<!doctype html><html lang=es><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Bunker Creativo · 75 videos listos</title>
<script src="https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js"></script>
<style>body{{margin:0;background:#0d1430;color:#f3f5ff;font:15px/1.5 system-ui,sans-serif}}main{{max-width:1200px;margin:auto;padding:24px 14px 80px}}h1 em{{color:#ff5b1f;font-style:normal}}.sub{{color:#b4bde3}}
.z{{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0 22px}}.z button,.b button,.b a{{background:#ff5b1f;color:#1f0800;border:0;border-radius:999px;padding:10px 16px;font-weight:800;cursor:pointer;text-decoration:none;font-size:14px}}.z button.s{{background:#c8ff2e;color:#10180a}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}}.c{{background:#111a3d;border-radius:14px;padding:12px}}.h{{display:flex;justify-content:space-between;align-items:center;gap:6px;font-size:13px}}
.tag{{border-radius:6px;padding:1px 7px;font-weight:800;font-size:11px}}.tR{{background:#c8ff2e;color:#10180a}}.tV{{background:#3a4a8f}}.tS{{background:#ff5b1f;color:#1f0800}}
video{{width:100%;border-radius:10px;background:#000;margin-top:8px;max-height:420px}}.t{{font-weight:800;margin:.4em 0}}textarea{{width:100%;box-sizing:border-box;height:84px;background:#0d1430;color:#dfe4ff;border:1px solid #24306a;border-radius:8px;font:13px/1.4 system-ui;padding:6px}}
.b{{display:flex;gap:8px;margin-top:8px}}.b button,.b a{{padding:7px 12px;font-size:13px}}.b a{{background:#24306a;color:#f3f5ff}}#st{{color:#c8ff2e;font-weight:700}}</style>
<main><h1>Bunker Creativo · <em>75 videos</em> listos</h1>
<p class=sub>Facebook + Instagram · 9 nov → 8 dic 2026 · Reels 08:00 (música F) · Feed 13:00 (música H) · Ventas 19:00 (música E). Los archivos van numerados en orden de publicación. El mismo MP4 sirve para FB y para IG (Reel).</p>
<div class=z><button onclick="zip(1)">ZIP semana 1</button><button onclick="zip(2)">ZIP semana 2</button><button onclick="zip(3)">ZIP semana 3</button><button onclick="zip(4)">ZIP semana 4</button><button class=s onclick="zip(0)">ZIP todo (~230 MB, mejor en compu)</button><span id=st></span></div>
<div class=g>{''.join(cards)}</div></main>
<script>const D={data};
function cp(b){{const t=b.closest('.c').querySelector('textarea');navigator.clipboard.writeText(t.value).then(()=>{{b.textContent='¡Copiado!';setTimeout(()=>b.textContent='Copiar caption',1500)}})}}
async function zip(w){{const st=document.getElementById('st');const L=D.filter(x=>!w||x.w==w);const z=new JSZip();let caps='';
for(let i=0;i<L.length;i++){{st.textContent=`Bajando ${{i+1}}/${{L.length}}…`;const r=await fetch('videos/'+L[i].n+'.mp4');z.file(L[i].n+'.mp4',await r.blob());caps+=L[i].n+'\\n'+L[i].c+'\\n\\n---\\n\\n'}}
z.file('captions.txt',caps);st.textContent='Armando ZIP…';const b=await z.generateAsync({{type:'blob'}});const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='bunker-creativo-'+(w?'semana'+w:'todo')+'.zip';a.click();st.textContent='Listo ✓'}}
</script></html>"""
os.makedirs('entrega', exist_ok=True)
open('entrega/index.html', 'w').write(page.replace('videos/', '../videos/'))
print('ok', len(items))
