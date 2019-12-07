text = soup.find('p', class_='c') #가장 먼저 검색태는 태그 1개 반환
print(text)
print(text.get_text())

text = []
text = soup.find_all('p', 'c') 
#text = soup.find_all('p', {'class': 'c'})
#이 태그에 해당되는 태그 리스트들 반환
#기본적으로, 이 리스트의 원소는 '태그'들이다.
print(text)
# print(text.get_text) 태그 리스트들은 get_text할 수 없다.
for txt in text:
    print("[ ]: "+txt.get_text().strip('\n'))