#coding:utf-8
import urllib2
import logging
import gzip, StringIO
import zlib
from bs4 import BeautifulSoup

url = 'http://stocks.sina.cn/us/?code=BIDU&vt=4'
request = urllib2.Request(url)
request.add_header('Accept-encoding', 'gzip')
opener = urllib2.build_opener()
response = opener.open(request)
html = response.read()
gzipped = response.headers.get('Content-Encoding')
if gzipped:
    html = zlib.decompress(html, 16+zlib.MAX_WBITS)

soup = BeautifulSoup(html, from_encoding='utf-8')
spans = soup.find_all("span")
status = 0
value = 0
for sp in spans:
	if status == 0:
		if sp.text == u'市值':
			status = 1
			pass
	elif status == 1:
		value = sp.text
		break
print value