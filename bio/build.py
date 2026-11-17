"""Bina bio/preview.html dan bio/TAMPAL-custom-html.html (dipadatkan, < 16k aksara untuk had klik.vip)
dari bio/bio-pro.html. Guna: python3 bio/build.py"""
import re, subprocess, sys
src = open('bio/bio-pro.html').read()
sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
open('bio/preview.html', 'w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bio Sir Dharma</title></head><body style="margin:0;background:#f4ede1">' + src.replace('IMG/', '../') + '</body></html>')
s = src.replace('IMG/', f'https://raw.githubusercontent.com/dhsfikri/website-sales/{sha}/')
head, rest = s.split('<style>', 1); css, body = rest.split('</style>', 1)
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
css = re.sub(r'\s+', ' ', css)
css = re.sub(r'\s*([{}:;,>])\s*', r'\1', css).replace(';}', '}')
css = css.replace('font-weight:700', 'font-weight:800')
body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
body = re.sub(r'<noscript>.*?</noscript>', '', body, flags=re.S)
body = re.sub(r'>\s+<', '><', body)
head = re.sub(r'<!--.*?-->', '', head).strip().replace('wght@500;600;700;800;900', 'wght@500;600;800;900')
out = '<!-- BIO SIR DHARMA -->' + head + '<style>' + css.strip() + '</style>' + body.strip()
for old, new in [('--green2', '--g2'), ('--cream', '--cr'), ('--sand', '--sa'), ('--green', '--gr'), ('--gold', '--go'), ('--soft', '--so'), ('--card2', '--k2'), ('--card', '--k')]:
    out = out.replace(old + ')', new + ')').replace(old + ':', new + ':')
assert 'q-' not in out
out = out.replace('sd-', 'q-')
open('bio/TAMPAL-custom-html.html', 'w').write(out)
print('TAMPAL:', len(out), 'aksara')
if len(out) > 15800:
    sys.exit('AMARAN: terlalu panjang untuk klik.vip (had ~16,200)')
