from urllib.parse import urljoin
s1 = urljoin('http://www.admin.ru/fl/f2/test.html', 'file.html')
'http://www.admin.ru/fl/f2/file.html'
s2 = urljoin('http://www.admin.ru/f1/f2/test.html', 'f3/file.html')
'http://www.admin.ru/f1/f2/f3/file.html'
s3 = urljoin('http://www.admin.ru/f1/f2/test.html', '/file.html')
'http://www.admin.ru/file.html'
s4 = urljoin('http://www.admin.ru/f1/f2/test.html', './file.html')
'http://www.admin.ru/f1/f2/file.html'
s5 = urljoin('http://www.admin.ru/f1/f2/test.html', '../file.html')
'http://www.admin.ru/f1/file.html'
s6 = urljoin('http://www.admin.ru/f1/f2/test.html', '../../file.html')
'http://www.admin.ru/file.html'
s7 = urljoin('http://www.admin.ru/f1/f2/test.html', '../../../file.html')
'http://www.admin.ru/../file.html'

print(s1,s2,s3,s4,s5,s6,s7)