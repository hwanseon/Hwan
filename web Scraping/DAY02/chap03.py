from bs4 import BeautifulSoup

html_text = '<span class = "red"> Heavens! what a virulent attack! </span>'
soup = BeautifulSoup(html_text, "html.parser")

object_tag = soup.find("span")

print("object_tag: ", object_tag)
print("attrs: ", object_tag.attrs)
print("value: ", object_tag.attrs["class"])
print("text: ", object_tag.text)

# CSS 속성을 이용한 검색
from urllib.request import urlopen

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, "html.parser")

# 등장인물의 이름 : 녹색
name_list = soup.find_all("span", {"class":"green"})
for name in name_list:
    print(name.string)

# 특정 단어 찾기
prince_list = soup.find_all(string = "the prince")
print(prince_list)
print("the prince count : ", len(prince_list))

# 트리이동 : 자식과 자손
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, "html.parser")

table_tag = soup.find("table", {"id":"giftList"})
print("children의 개수 : ", len(list(table_tag.children)))

index = 0
for child in table_tag.children :
    index += 1
    print(f"[{index}]: {child}")
    print("-"*40)

# 트리이동 : 자손 descendants
desc = soup.find("table", {"id":"giftList"}).descendants
list_desc = list(desc)
print("descendants 개수 : ", len(list_desc))

for tag in list_desc:
    print(tag)

# 트리이동 : 형제 siblings
for sibling in soup.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)
    print("-"*30)

# 선택된 행 이전의 항목들을 선택 : previous_siblings
print("previous_siblings")
for sibling in soup.find("tr", {"id":"gift2"}).previous_siblings:
    print(sibling)

# 문자열 마지막에 whitespace("\n" or "\r")이 있는 경우
sibling2 = soup.find("tr", {"id":"gift3"}).next_sibling.next_sibling
print(sibling2)

# tree 이동 : parent 사용
style_tag = soup.style
print(style_tag.parent)

img1 = soup.find("img", {"src":	'../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)

# ---------------------------------------------------------------------------------------------------
## 정규 표현식 객체 사용 compile
import re

m = re.match("[a-z]+", "Python") # 첫글자가 대문자라서 아예 검사를 안하고 넘어가서 None
print(m)
print(re.match("[a-z]+", "pythoN")) # N 전까지 찾아줌 (소문자만)
print(re.search("apple", "I like apple!"))

p = re.compile("[a-z]+")
m = p.match("python")
print(m)
print(p.search("I like apple 123"))

# match(): 문자열의 처음부터 검사
print(re.match('[a-z]+', 'regex python'))
print(re.match('[a-z]+', ' regexpython')) # 문자열 처음에 공백을 포함해서 None

print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN')) # None -> $ : 문자열의 마지막에 소문자가 1회 이상 있으면 리턴

print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))
print(re.match('[a-z]+$', 'regexPYthon')) # None -> $ : 마지막에 소문자가 존재하지만 문자 자체에 대문자가 있기에
print(re.match('[a-z]+$', 'regexPY thon'))

# fineall() 함수 : 일치하는 모든 문자열을 리스트로 리턴
p = re.compile("[a-z]+")
print(p.findall) # 첫글자가 대문자면 글자 중에서 대문자를 제외하고 출력

# search() 함수 : 일치하는 첫번째 문자열만 리턴
result = p.search("I like apple 123")
print(result)

result = p.findall("I like apple 123")
print(result)

tel_checker = re.compile(r"^(\d{2,3})-(\d{3,4})-(\d{4})$")

print(tel_checker.match("02-123-4567"))
match_groups = tel_checker.match('02-123-4567').group()
match_groups = tel_checker.match('02-123-4567').groups()
print(match_groups)

print(tel_checker.match("053-950-45678"))
print(tel_checker.match("053950-4567"))

# 전화번호에서 dash(-) 제거하고 검사하기
tel_number = '053-950-4567'
tel_number = tel_number.replace('-', '')
print(tel_number)
tel_checker1 = re.compile(r'^(\d{2,3})(\d{3,4})(\d{4})$')
print(tel_checker1.match(tel_number))
print(tel_checker1.match('0239501234'))

tel_checker	= re.compile('^(\d{2,3})-(\d{3,4})-(\d{4})$')
m =	tel_checker.match('02-123-4567')
print(m.groups())
print('group():	', m.group())
print('group(0): ',	m.group(0))
print('group(1): ',	m.group(1))
print('group(2,3): ', m.group(2,3))
print('start(): ', m.start())	
print('end(): ', m.end())           # 매칭된 문자열의 마지막 인덱스 + 1 => 끝 위치를 반환하기 때문에 
                                    # 위치 반환이라서 인덱스 + 1을 해줘야함

# 휴대전화 번호
cell_phone = re.compile("^(01(?:0|1|[6-9]))-(\d{3,4})-(\d{4})$")

print(cell_phone.match('010-123-4567'))
print(cell_phone.match('019-1234-5678'))
print(cell_phone.match('001-123-4567'))  # None
print(cell_phone.match('010-1234567'))  # None

# 전방탐색 lookahead
lookhead1 = re.search(".+(?=won)", "1000 won")
if (lookhead1 != None):
    print(lookhead1.group())
else :
    print("None")

lookhead2 = re.search(".+(?=am)", "2023-01-26 am 10:00:01")
print(lookhead2)

# 전방 부정
lookhead3 = re.search("\d{4}(?!-)", "010-1234-5678") # 4자리 정수가 있고 뒤에 -가 없는 문자를 반환
print(lookhead3)

# 후방 탐색: lookbehind
lookbehind1 = re.search("(?<=am).+", "2023-01-26 am 11:10:01")
print(lookbehind1)

lookbehind2 = re.search("(?<=:).+", "USD: $51")
print(lookbehind2)

# 후방부정
lookbehind4 = re.search(r"\b(?<!\$)\d+\b", "I paid $30 for 100 apples.")
print(lookbehind4)

# image 소스들 화면 출력
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

img_tag	= re.compile('/img/gifts/img.*.jpg')
images = soup.find_all('img', {'src': img_tag})

for image in images :
    print(image, end = " -> ['scr'] 속성값 : ")
    print(image["src"])

# 대소문자 구분 없이 특정단어 검색
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs	= BeautifulSoup(html, 'html.parser')
princeList = bs.find_all(string='the prince')
print('the	prince	count: ', len(princeList))
prince_list = bs.find_all(string=re.compile('[T|t]{1}he prince'))
print('T|the prince count:', len(prince_list))

# -------------------------------------------------------------------------------
## Wikipedia page 가져오기
from urllib.request import urlopen

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, "html.parser")
for link in bs.find_all("a") :
    if "href" in link.attrs:
        print(link.attrs["href"])