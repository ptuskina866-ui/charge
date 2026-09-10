from pathlib import Path
from html.parser import HTMLParser
import re,json
root=Path('dist')
class Validator(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.anchors=[];self.h1=0;self.images=0;self.errors=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if t=='h1':self.h1+=1
  for k in ['href','src','data-src','poster']:
   if a.get(k,'').startswith('/') and not a[k].startswith('//'):self.refs.append(a[k])
   if k=='href' and a.get(k,'').startswith('#') and len(a[k])>1:self.anchors.append(a[k][1:])
  if 'srcset' in a:self.refs.extend(x.strip().split(' ')[0] for x in a['srcset'].split(','))
  if t=='img':
   self.images+=1
   for k in ['alt','width','height']:
    if not a.get(k):self.errors.append(f'Missing image {k}: {a.get("src")}')
v=Validator();s=(root/'index.html').read_text(encoding='utf-8');v.feed(s)
assert v.h1==1, f'H1 count {v.h1}'
assert len(v.ids)==len(set(v.ids)), 'Duplicate IDs'
assert not v.errors,v.errors
assert not(set(v.anchors)-set(v.ids)), 'Broken anchors'
for ref in v.refs:assert (root/ref.lstrip('/')).is_file(),f'Missing {ref}'
for css in root.glob('*.css'):
 for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)',css.read_text()):
  if ref.startswith('/'):assert (root/ref.lstrip('/')).exists(),f'Missing {ref}'
for block in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):json.loads(block)
assert s.count('350 BYN')==4,'Price must be consistent in all four places'
assert '[ЦЕНА]' not in s,'Unreplaced price'
print(f'PASS: one H1, {v.images} labelled/sized images, {len(set(v.refs))} local assets, {len(v.anchors)} anchors, JSON-LD, consistent price.')
print('Public payload total:',sum(p.stat().st_size for p in root.rglob('*') if p.is_file()),'bytes')
