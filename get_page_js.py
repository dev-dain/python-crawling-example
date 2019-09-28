# 이 스크립트는 html 소스 코드를 긁어서 저장한다.
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.implicitly_wait(100)
driver.get('http://www.duksung.ac.kr/diet/schedule.do?menuId=1151')
driver.implicitly_wait(100)

html = driver.page_source
out_fp = open("after_js_page.html", "w", encoding="utf-8")
out_fp.write(html)

out_fp.close()
driver.close()
