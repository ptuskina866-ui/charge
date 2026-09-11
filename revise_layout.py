from pathlib import Path
import re
p=Path('dist/index.html');s=p.read_text(encoding='utf-8')
s=s.replace('<p class="eyebrow"><span class="status-dot"></span> ПОРТАТИВНАЯ ЗАРЯДКА · TYPE 2</p>','')
s=s.replace('<link rel="stylesheet" href="/sections.css">','<link rel="stylesheet" href="/sections.css">\n<link rel="stylesheet" href="/refinements.css">')
s=s.replace('<div class="current-visual"><img src="/assets/portrait-800.webp" width="896" height="1200" loading="lazy" alt="Крупный план блока Teschev с LCD-дисплеем и кнопкой выбора режима">','<div class="current-visual"><picture><source media="(max-width: 767px)" srcset="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="><img src="/assets/current-macro-1200.webp" srcset="/assets/current-macro-800.webp 800w, /assets/current-macro-1200.webp 838w" sizes="50vw" width="838" height="1122" loading="lazy" alt="Крупный план дисплея Teschev и кнопки настройки тока"></picture>')
display='''<section class="display-section section wrap" id="display">
<div class="display-heading"><p class="eyebrow">03 / ВИДЕТЬ ГЛАВНОЕ</p><h2>Всё под<br>контролем.</h2><p class="section-intro">Основные параметры зарядки —<br>на одном LCD-дисплее.</p></div>
<div class="display-stage">
<div class="display-media"><video id="display-video" muted playsinline loop preload="none" poster="/assets/display-poster.webp" width="600" height="754" aria-label="Медленное приближение к LCD-дисплею Teschev" data-src="/assets/display-loop.mp4"></video></div>
<div class="display-callout callout-current" data-display-step="0"><span>01</span><strong>Ток</strong><i aria-hidden="true"></i></div>
<div class="display-callout callout-voltage" data-display-step="1"><span>02</span><strong>Напряжение</strong><i aria-hidden="true"></i></div>
<div class="display-callout callout-power" data-display-step="2"><span>03</span><strong>Мощность</strong><i aria-hidden="true"></i></div>
<div class="display-callout callout-time" data-display-step="3"><span>04</span><strong>Время</strong><i aria-hidden="true"></i></div>
<button id="display-motion" class="motion-button" aria-label="Включить анимацию" aria-pressed="false"><span aria-hidden="true">▷</span> <span class="motion-label">Включить анимацию</span></button>
</div>
</section>'''
s,n=re.subn(r'<section class="display-section.*?</section>',lambda _:display,s,flags=re.S);assert n==1
s,n=re.subn(r'<section class="portable section".*?</section>\n?', '',s,flags=re.S);assert n==1
s,n=re.subn(r'<section class="offer dark".*?</section>\n?', '',s,flags=re.S);assert n==1
s,n=re.subn(r'<div class="product-film">.*?</video></div>', '',s,flags=re.S);assert n==1
s=s.replace('<p class="fine-print">Поможем проверить разъём вашего автомобиля.</p>','')
s=s.replace('<img src="/assets/connector-1440.webp" width="720" height="720" loading="lazy" alt="Зарядный коннектор Type 2 крупным планом">','<img src="/assets/type2-closeup-1200.webp" srcset="/assets/type2-closeup-480.webp 480w, /assets/type2-closeup-800.webp 800w, /assets/type2-closeup-1200.webp 1200w" sizes="(max-width:767px) 100vw, 50vw" width="1200" height="896" loading="lazy" alt="Крупный план коннектора Type 2 с семью контактами">')
s=s.replace('id="specifications"><div>','id="specifications"><div class="spec-heading">')
for old,new in [('06 / ВАШ','05 / ВАШ'),('07 / В ДЕТАЛЯХ','06 / В ДЕТАЛЯХ'),('08 / ПРОДУМАНО','07 / ПРОДУМАНО'),('09 / ПЕРЕД','08 / ПЕРЕД')]:s=s.replace(old,new)
p.write_text(s,encoding='utf-8')

p=Path('dist/app.js');s=p.read_text(encoding='utf-8')
s,n=re.subn(r"const track = .*?(?=const leadDialog)",'',s,flags=re.S);assert n==1
s,n=re.subn(r"const video=\$\('#product-video'\);.*?(?=\$\('#year'\))",'',s,flags=re.S);assert n==1
p.write_text(s,encoding='utf-8')

p=Path('validate_site.py');s=p.read_text().replace("s.count('350 BYN')==4","s.count('350 BYN')==3").replace('all four places','all three places');p.write_text(s)
