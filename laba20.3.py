from urllib.parse import quote
s1 = quote("Строка", encoding="cp1251")
s2 = quote("Строка", encoding="utf-8")
s3 = quote("/~nik/"), quote("/~nik/", safe="")
s4 = quote("/~nik/", safe="/~")
print(s1,s2,s3,s4)