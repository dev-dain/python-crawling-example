from bs4 import BeautifulSoup

html = ''
fp = open('example.html', 'r', encoding='utf-8')
for line in fp:
    html += line
fp.close

soup = BeautifulSoup(html, "html.parser")