from xml.sax.saxutils import unescape
s = '&amp;&lt;&gt;&quot;&nbsp;'
a1 = unescape(s)
a2 = unescape(s, {"quot;":"","&nbps":""})
print(a1, a2)