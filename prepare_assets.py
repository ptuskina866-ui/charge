from pathlib import Path
from PIL import Image
import subprocess

out=Path('dist/assets')
sources={
 'hero':'61ff73f2-67e0-4458-aa36-5663652485c6',
 'product':'53e4add8-a80e-4b38-9a01-28b2c409dbb2',
 'connector':'fa98661c-5cdb-42ce-9bb0-e16034ce35ff',
 'portrait':'59d40f9c-727c-4236-a74d-0c1fa5ad890e',
 'studio':'857b1cf2-b672-4b20-8a2c-136d38104de9',
 'home':'f1394870-9f4f-4199-9192-061e1c9edca1',
 'garage':'f4750d93-0c8f-4966-b0e6-fac26e87aca8',
 'weekend':'9e0b043c-ca7b-4d73-85a7-a4621575b6b5',
 'kit':'4bbc69f7-d7b3-4e87-b885-3fc163d6c8c7',
}
for name,uid in sources.items():
 im=Image.open(Path('C:/Users/Honor/AppData/Local/Temp')/f'codex-clipboard-{uid}.png').convert('RGB')
 for width in [480,800,1440]:
  if width==1440 or width<im.width:
   copy=im.copy();copy.thumbnail((width,2000));copy.save(out/f'{name}-{width}.webp',quality=86,method=6)
 print(name, im.size)
for i,suffix in enumerate(['','(1)','(2)','(3)']):
 src=Path('C:/Users/Honor/Downloads')/f'Creating_commercial_product_shot_202609091651{suffix}.mp4'
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss','2','-i',str(src),'-frames:v','1',f'video-frame-{i}.jpg'],check=True)
