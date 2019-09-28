from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'http://www.duksung.ac.kr/diet/schedule.do?menuId=1151'
html = requests.get(url, headers = headers).text #<class 'str'>

out_fp = open("before_js_page.html", "w", encoding="utf-8")
out_fp.write(html)
out_fp.close()
