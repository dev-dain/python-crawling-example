text = soup.find_all('p') 

print(text)
# print(text.get_text) 태그 리스트들은 get_text할 수 없다.
for txt in text:
    print("[ ]: "+txt.get_text().strip('\n'))
print(text[0].get_text())