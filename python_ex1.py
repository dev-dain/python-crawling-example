classic='The Great Gatsby'
print("문자열 내 문자 개수 :", len(classic)) #16 반환

'''
book=[classic, 'Le Petit Prince', 'Gut Gegen Nordwind', 'Principles', 'The Beginners', 'Money Ball']
print("배열 내 원소 개수 :", len(book)) #6 반환
'''
'''
book.append('The Big Short')
print("배열 내 원소 개수 :", len(book)) #7 반환
'''
'''
fp=open('test.txt', 'w', encoding='utf-8')
for title in book:
    fp.writelines(title+'\n')
fp.close()
'''
'''
fp=open('test.txt', 'r', encoding='utf-8')
book_list=[]
for line in fp.readlines():
    #line = line.strip('\n')
    book_list.append(line)
print(book_list)
'''
'''
wow = '---Wow! You\'re the best student ever!---'
print(wow.strip('-'))
print(wow.strip('-').split(' '))

print('tacocat'.replace('c', 'r'))
'''
'''
even_list = [x for x in range(10) if x%2==0]
print(even_list)
'''
'''
temp_list = ['My ', '', 'textbook ', '', '', 'is', 'quite', '', 'old']
temp_list = [tmp for tmp in temp_list if tmp]
print(temp_list)
'''
'''
temp_list = []
temp_list = [' ', '\n', 'espresso', ' ', '', 'strawberry juice ', '', 'cafe mocha', '', '\n']
print(temp_list)
temp_list = [tmp for tmp in temp_list if tmp]
print(temp_list)
tmp = ''
for line in temp_list:
    tmp += line
tmp = tmp.strip(' ')
tmp = tmp.replace('\n', '')
print(tmp)
'''