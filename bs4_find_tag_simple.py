text = soup.p #이것은 text = soup.find('p')와 같다.
print(text['class']) #이 태그의 class 확인
print(text['id']) #이 태그의 id 확인
print(text.attrs) #이 태그의 속성과 값 확인 (딕셔너리 형태)

text = soup.select('body span') #이것은 text = soup.find_all('span')과 같다.
print(text)
text = soup.select('body span')[0] #이것은 text = soup.find_all('span')[0]과 같다.
print(text)