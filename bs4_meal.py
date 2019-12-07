from bs4 import BeautifulSoup

html = ''
fp = open('after_js_page.html', 'r', encoding='utf-8')
for line in fp:
    html += line
fp.close

soup = BeautifulSoup(html, "html.parser")

yoil = soup.find_all('th', {'scope':'col'})
for yo in yoil:
    print(yo.get_text('\n'))

meal = soup.find_all('tbody')
stu_meal = soup.find('tr')

for stu in stu_meal:
    print(stu.get_text('\n'))

print(len(stu_meal))