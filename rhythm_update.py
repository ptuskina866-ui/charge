from pathlib import Path
import re
p=Path('dist/index.html');s=p.read_text(encoding='utf-8')
note='Марки приведены как примеры. Совместимость зависит от версии автомобиля и установленного зарядного разъёма.'
intro='<p class="section-intro">Версия Type 2 предназначена для автомобилей с соответствующим зарядным портом.</p>'
assert s.count(intro)==1
s=s.replace(intro,intro+'<p class="compat-disclaimer fine-print">'+note+'</p>')
brands=['Tesla','Volkswagen','BMW','Mercedes-Benz','Volvo','Kia','Hyundai','Renault']
group=''.join('<span>'+b+'</span>' for b in brands)
marquee='<div class="compat-brands brand-marquee" aria-label="Примеры марок автомобилей"><div class="marquee-window"><div class="marquee-track"><div class="marquee-group">'+group+'</div><div class="marquee-group" aria-hidden="true">'+group+'</div></div></div><button class="marquee-toggle" type="button" aria-label="Остановить бегущую строку" aria-pressed="false"><span aria-hidden="true">Ⅱ</span></button></div>'
s,n=re.subn(r'<div class="compat-brands">.*?</div>\s*</section>',lambda _:marquee+'\n</section>',s,flags=re.S);assert n==1
p.write_text(s,encoding='utf-8')
