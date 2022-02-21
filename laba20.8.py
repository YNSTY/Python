from urllib.parse import unquote_plus
s1 = unquote_plus("%D1%F2%FO%EE%EA%%EO+2", encoding="cp1251")
s2 = unquote_plus("%D1%F2%FO%EE%EA%%EO%202", encoding="cp1251")
print(s1, s2)