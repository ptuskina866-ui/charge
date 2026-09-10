from pathlib import Path
from html.parser import HTMLParser
import json,re

root=Path('dist')
page=root/'index.html'
html=page.read_text(encoding='utf-8-sig')
class FAQParser(HTMLParser):
 def __init__(self):
  super().__init__();self.in_faq=False;self.summary=False;self.para=False;self.q='';self.a='';self.items=[]
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if tag=='details':self.in_faq=True;self.q='';self.a=''
  if self.in_faq and tag=='summary':self.summary=True
  if self.in_faq and tag=='p':self.para=True
 def handle_endtag(self,tag):
  if tag=='summary':self.summary=False
  if tag=='p':self.para=False
  if tag=='details':
   self.items.append({'@type':'Question','name':self.q.strip(),'acceptedAnswer':{'@type':'Answer','text':self.a.strip()}});self.in_faq=False
 def handle_data(self,data):
  if self.summary:self.q+=data
  if self.para:self.a+=data
p=FAQParser();p.feed(html)
schema=[{'@context':'https://schema.org','@type':'FAQPage','mainEntity':p.items},{'@context':'https://schema.org','@type':'Product','name':'Портативная зарядка Teschev Type 2','brand':{'@type':'Brand','name':'Teschev'},'description':'Портативное зарядное устройство Type 2 до 3,5 кВт. Однофазная сеть 220 В, регулируемый ток 8/10/13/16 А, LCD-дисплей и отложенный запуск.','image':'https://teschev-charge.uladzimirchubatsiuk.chatgpt.site/assets/hero-1440.webp','offers':{'@type':'Offer','price':'350.00','priceCurrency':'BYN','url':'https://teschev-charge.uladzimirchubatsiuk.chatgpt.site/'}}]
html=re.sub(r'<script type="application/ld\+json" id="structured-data">.*?</script>\n?', '',html,flags=re.S)
html=html.replace('</head>','<script type="application/ld+json" id="structured-data">'+json.dumps(schema,ensure_ascii=False,separators=(',',':'))+'</script>\n</head>')
page.write_text(html,encoding='utf-8')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://teschev-charge.uladzimirchubatsiuk.chatgpt.site/sitemap.xml\n',encoding='utf-8')
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://teschev-charge.uladzimirchubatsiuk.chatgpt.site/</loc></url></urlset>',encoding='utf-8')
print('SEO: 1 product,',len(p.items),'visible FAQ entries, canonical and sitemap.')
