from urllib.parse import parse_qs
s = "str=%D1%F2%F0%EE%EA%E0%&v=10&v=20&vt="
s1 = parse_qs(s, encoding="cp1251")
s2 = parse_qs(s, keep_blank_values=True,encoding="cp1251")
print(s1,s2)