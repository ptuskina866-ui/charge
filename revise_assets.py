from pathlib import Path
from PIL import Image
import subprocess
out=Path('dist/assets')
for name,source in {
 'current-macro':'C:/Users/Honor/AppData/Local/Temp/codex-clipboard-37956bf1-3b48-42ea-a17b-2cc8d35da0d6.png',
 'type2-closeup':'C:/Users/Honor/Downloads/EV_charger_product_image_20260911105129.jpeg',
}.items():
 im=Image.open(source).convert('RGB')
 for w in [480,800,1200]:
  dest=im.copy();dest.thumbnail((w,1800));dest.save(out/f'{name}-{w}.webp',quality=88,method=6)
 print(name,im.size)
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss','4.4','-i','C:/Users/Honor/Downloads/Animate_charger_source_image_1080p_20260911104215.mp4','-vf','crop=860:1080:500:0,scale=600:-2','-frames:v','1',str(out/'display-poster.webp')],check=True)
