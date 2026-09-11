from pathlib import Path
p=Path('dist/index.html');s=p.read_text(encoding='utf-8')
old='<source media="(max-width: 767px)" srcset="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="><img src="/assets/current-macro-1200.webp" srcset="/assets/current-macro-800.webp 800w, /assets/current-macro-1200.webp 838w" sizes="50vw"'
new='<source media="(min-width: 768px)" srcset="/assets/current-macro-800.webp 800w, /assets/current-macro-1200.webp 838w" sizes="50vw"><img src="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="'
assert old in s
p.write_text(s.replace(old,new),encoding='utf-8')
