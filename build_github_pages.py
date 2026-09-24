"""Prepare the static site for its GitHub Pages project URL."""

from pathlib import Path
from shutil import copytree


source = Path(__file__).parent / "dist"
destination = Path(__file__).parent / ".github-pages-build"
base_path = "/charge"
old_origin = "https://teschev-charge.uladzimirchubatsiuk.chatgpt.site"
new_origin = "https://ptuskina866-ui.github.io" + base_path
github_origin = new_origin.removesuffix(base_path)

copytree(source, destination, dirs_exist_ok=True)

for path in destination.rglob("*"):
    if path.suffix not in {".html", ".css", ".js", ".xml", ".txt"}:
        continue
    content = path.read_text(encoding="utf-8")
    content = content.replace("/assets/", base_path + "/assets/")
    for filename in ("styles.css", "sections.css", "layout-final.css", "motion.css", "config.js", "app.js"):
        content = content.replace('"/' + filename, '"' + base_path + '/' + filename)
    content = content.replace(old_origin, github_origin)
    # Asset URLs already contain /charge; add it to links to the site root.
    content = content.replace(github_origin + '/"', new_origin + '/"')
    content = content.replace(github_origin + '/<', new_origin + '/<')
    content = content.replace(github_origin + '/sitemap.xml', new_origin + '/sitemap.xml')
    path.write_text(content, encoding="utf-8")
