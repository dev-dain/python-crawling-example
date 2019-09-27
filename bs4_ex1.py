from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://www.melon.com/chart/'
html = requests.get(url, headers = headers).text #<class 'str'>
'''
이 주석을 해제하면, 웹페이지의 소스 코드를 텍스트 파일로 저장할 수 있다.
out_fp = open("page.html", "w", encoding="utf-8")
out_fp.write(html)
out_fp.close()
'''
soup = BeautifulSoup(html, 'html.parser') #<class 'bs4.BeautifulSoup'>
titles = soup.find_all("div", {"class": "ellipsis rank01"}) #<class 'bs4.element.ResultSet'>
songs = soup.find_all("div", {"class": "ellipsis rank02"}) #<class 'bs4.element.ResultSet'>
#'bs4.element.ResultSet은 text로 변환(.text)이 불가능하지만, print는 가능하다.
#이는 ResultSet이 list 형태이기 때문이다.
#print(titles)

rank = 100
title = []
song = []

for t in titles:
    #하지만 ResultSet 안의 개별 요소들인 Tag들은 text로 변환이 가능하다.
    #print(type(t)) <class 'bs4.element.Tag'>
    title.append(t.find('a').text)

for s in songs:
    song.append(s.find('span', {"class": "checkEllipsis"}).text)
'''
for i in range(rank):
    print(str(i+1)+"위 : "+song[i]+" - "+title[i])
'''