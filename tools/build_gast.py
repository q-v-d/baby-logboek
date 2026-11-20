"""Maakt gast/index.html uit index.html: zelfde app, neutrale naam en icoon, GUEST aan."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
s = (root / "index.html").read_text()
def rep(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)
rep("<title>Mauro’s logboek</title>", "<title>Baby logboek</title>")
rep('<meta name="apple-mobile-web-app-title" content="Mauro">', '<meta name="apple-mobile-web-app-title" content="Logboek">')
rep('<link rel="manifest" href="manifest.json">\n', "")
s, n = re.subn(r'<meta property="og:[^>]*>\n|<meta name="twitter:card"[^>]*>\n', "", s); assert n == 8, n
rep("<h1>Mauro’s logboek</h1>", "<h1>Baby logboek</h1>")
rep("const GUEST = false;", "const GUEST = true;")
rep("<head>\n", '<head>\n<meta name="robots" content="noindex">\n<meta name="referrer" content="no-referrer">\n')
(root / "gast").mkdir(exist_ok=True)
(root / "gast" / "index.html").write_text(s)
print("gast/index.html geschreven")
