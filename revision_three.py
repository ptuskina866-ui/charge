from pathlib import Path
from PIL import Image
import re

root=Path('dist')
for name,filename in {
 'connection-new':'EV_charger_plugged_into_car_20260911112828.jpeg',
 'peace-new':'EV_charger_connected_to_car_20260911113356.jpeg',
 'connector-new':'EV_charger_product_image_20260911113602.jpeg',
}.items():
 source=Path('C:/Users/Honor/Downloads')/filename
 im=Image.open(source).convert('RGB')
 for width in [480,800,1200]:
  resized=im.copy();resized.thumbnail((width,1500));resized.save(root/'assets'/f'{name}-{width}.webp',quality=88,method=6)
 print(name,im.size)

page=root/'index.html';s=page.read_text(encoding='utf-8')
s,n=re.subn(r'<p class="trust-line">.*?</p>','',s,flags=re.S);assert n==1
s,n=re.subn(r'<div class="hero-bottom">.*?</div>','',s,flags=re.S);assert n==1
s,n=re.subn(r'<div class="image-label">.*?</div>','',s,flags=re.S);assert n==1
# Only the connection section gets the new image.
start=s.index('<section class="simple');end=s.index('</section>',start)
part=s[start:end].replace('/assets/home-','/assets/connection-new-').replace('connection-new-1440','connection-new-1200')
s=s[:start]+part+s[end:]

display='''<section class="display-section section wrap" id="display">
<div class="display-heading"><p class="eyebrow">03 / ВИДЕТЬ ГЛАВНОЕ</p><h2>Всё под<br>контролем.</h2><p class="section-intro">Основные параметры зарядки —<br>на одном LCD-дисплее.</p>
<dl class="display-readings"><div><dt><span>01</span> Ток</dt><dd>Выбранный режим</dd></div><div><dt><span>02</span> Напряжение</dt><dd>Параметры сети</dd></div><div><dt><span>03</span> Мощность</dt><dd>Процесс зарядки</dd></div><div><dt><span>04</span> Время</dt><dd>Длительность сеанса</dd></div></dl></div>
<figure class="display-still"><img src="/assets/current-macro-1200.webp" srcset="/assets/current-macro-480.webp 480w, /assets/current-macro-800.webp 800w, /assets/current-macro-1200.webp 838w" sizes="(max-width:767px) 100vw, 55vw" width="838" height="1122" loading="lazy" alt="Крупный статичный план LCD-дисплея зарядки Teschev"></figure>
</section>'''
s,n=re.subn(r'<section class="display-section.*?</section>',lambda _:display,s,flags=re.S);assert n==1
start=s.index('<section class="peace');end=s.index('</section>',start)
part=s[start:end].replace('/assets/garage-','/assets/peace-new-').replace('peace-new-1440','peace-new-1200').replace('height="896"','height="675"')
part=part.replace('Автомобиль<br>заряжается.<br>Вечер — ваш.','Автомобиль заряжается.<br>Вечер — ваш.')
s=s[:start]+part+s[end:]

compat='''<section class="compatibility wrap" id="compatibility">
<div class="compat-visual"><img src="/assets/connector-new-1200.webp" srcset="/assets/connector-new-480.webp 480w, /assets/connector-new-800.webp 800w, /assets/connector-new-1200.webp 1200w" sizes="(max-width:767px) 100vw, 58vw" width="1200" height="675" loading="lazy" alt="Крупный коннектор Type 2 с семью контактами"><span class="connector-tag">TYPE 2 <span>7 КОНТАКТОВ</span></span></div>
<div class="compat-copy"><p class="eyebrow">05 / ВАШ АВТОМОБИЛЬ</p><h2>Подойдёт<br>к вашему<br>автомобилю?</h2><p class="section-intro">Версия Type 2 предназначена для автомобилей с соответствующим зарядным портом.</p><button class="button" data-form="compatibility">Проверить совместимость <span aria-hidden="true">↗</span></button></div>
<div class="compat-brands"><div class="brand-list" aria-label="Примеры марок с отдельными версиями автомобилей Type 2"><span>Tesla</span><span>Volkswagen</span><span>BMW</span><span>Mercedes-Benz</span><span>Volvo</span><span>Kia</span><span>Hyundai</span><span>Renault</span></div><p class="fine-print">Марки приведены как примеры. Совместимость зависит от версии автомобиля и установленного зарядного разъёма.</p></div>
</section>'''
s,n=re.subn(r'<section class="compatibility.*?</section>',lambda _:compat,s,flags=re.S);assert n==1
s=s.replace('<h2>Характеристики.</h2>','<h2>Характеристики</h2>').replace('Teschev / портативная версия Type 2','Портативная версия Type 2')
s,n=re.subn(r'<section class="kit section.*?</section>\n?','',s,flags=re.S);assert n==1
s=s.replace('id="faq"><div>','id="faq"><div class="faq-heading">').replace('08 / ПЕРЕД ЗАКАЗОМ','07 / ПЕРЕД ЗАКАЗОМ').replace('<h2>Хорошие<br>вопросы.</h2>','<h2>Вопросы и ответы</h2>')
page.write_text(s,encoding='utf-8')
p=root/'app.js';s=p.read_text(encoding='utf-8');s,n=re.subn(r"const displayStage = .*?(?=// Optional agent access)",'',s,flags=re.S);assert n==1;p.write_text(s,encoding='utf-8')
