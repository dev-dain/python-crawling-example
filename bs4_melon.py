from bs4 import BeautifulSoup
import requests

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (like Gecko) Chrome/63.0.3239.132 Safari/537.36'} #headers= 부터 여기까지 한 줄임
url = 'https://www.melon.com/chart/'
html = requests.get(url, headers = header).text

soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all('div', {'class':'ellipsis rank01'})
artists = soup.find_all('span', 'checkEllipsis')

print(len(artists))
for a in artists:
    print(a.get_text())
print(len(artists))

'''
title = []
for t in titles:
    title.append(t)

artist = []
for a in artists:
    artist.append(a)

for i in range(100):
    print(str(i+1)+"위: "+title[i]+"- "+artist[i])
'''