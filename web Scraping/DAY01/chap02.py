from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.daangn.com/hot_articles')
bs = BeautifulSoup(html.read(), "html.parser")

print(bs.h1)
print(bs.h1.string.strip())

html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
    <span class="red">BeautifulSoup Library Examples!</span>
    <div id="link">
        <a class="external_link" href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link" href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link" href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

soup = BeautifulSoup(html_example, "html.parser")

print(soup.title)
print(soup.title.string)
print(soup.title.get_text())

# 해당 태그를 포함하고 있는 부모
print(soup.title.parent)

print(soup.body)

print(soup.h1)
print(soup.h1.string)

print(soup.a)
print(soup.a.string)
print(soup.a["href"])
print(soup.a.get("href"))
print(soup.a["class"])
print(soup.a.get("class"))

# find 함수
print(soup.find("div"))

print(soup.find("div", {"id":"text_id2"}))
# 추출된 요소에서 텍스트만 가져오기
div_text = soup.find("div", {"id":"text_id2"})
print(div_text.text)
print(div_text.string) # <p>g</p>가 있어서 인식이 잘 안됨 
                       # text 쓰는 것을 지향

## 문자열이 이상하면 디버깅 할 것 
href_link = soup.find("a", {"class":"internal_link"})
href_link = soup.find("a", class_ = "internal_link") # class_ 를 사용하는 이유 : class는 파이썬 예약어

print(href_link)
print(href_link["href"])
print(href_link.get("href"))
print(href_link.text)
print(href_link["class"])

# find 함수에서 <a> 태그 내부의 모든 속성 가져오기 
# => attrs 
print("href_link.attrs : ", href_link.attrs)
print("class 속성값 : ", href_link["class"])

print("values(): ", href_link.attrs.values())

values = list(href_link.attrs.values())
print(f"values[0]: {values[0]}, values[1]: {values[1]}")

href_value = soup.find(attrs = {"href":"www.google.com"})
href_value = soup.find("a", attrs = {"href":"www.google.com"})

print("href_value: ", href_value)
print(href_value["href"])
print(href_value.string)

span_tag = soup.find("span")

print("span tag: ", span_tag)
print("attrs: ", span_tag.attrs)
print("value: ", span_tag.attrs["class"])
print("text: ", span_tag.text)

print("class의 속성값 : ", href_link["class"])

div_tags = soup.find_all("div")
print("div_tags length: ", len(div_tags))

for div in div_tags:
    print("-"*25)
    print(div)

links = soup.find_all("a")

for alink in links:
    print(alink)
    print(f"url: {alink['href']}, text : {alink.string}")
    print()

# 특정 태그 중 여러 속성값을 한 번에 검색
link_tag = soup.find_all("a", {"class":["external_link", "internal_link"]})
print(link_tag)

p_tags = soup.find_all("p", {"id":["first", "third"]})
for p in p_tags:
    print(p)

# -------------------------------------------------------------------------------

# select 함수 = find_all과 유사함 (즉, 다 찾아줌)
# select_one() 함수 : 조건에 맞는 첫번째 태그만 리턴
# select_one()
head = soup.select_one("head")
print(head)
print("head.text: ", head.text.strip())

h1 = soup.select_one("h1")
print(h1)

# id 검색 : #id
footer = soup.select_one("h1#footer")
print(footer)

# class 검색 : 태그.class_name
#  <a	class=“internal_link”	herf=“/pages/page1.html>Page1</a> 검색
class_link = soup.select_one("a.internal_link")
print(class_link)

print(class_link.string)
print(class_link["href"])

# 계층적 하위 태그 접근
# 부모태그 > 자식태그 형식으로 접근 : 태그가 단계적으로 존재할 때
link1 = soup.select_one("div#link > a.external_link")
print(link1)

link_find = soup.find("div", {"id":"link"})

external_link = link_find.find("a", {"class":"external_link"})
print("find external_link: ", external_link)

# 공백으로 하위 태그 선언 
link2 = soup.select_one("div#class1 p#second")
print(link2)
print(link2.string)

third_tag = soup.select_one("div#link a.internal_link")
print(third_tag["href"])
print(third_tag.text)

# select 함수
h1_all = soup.select("h1")
print("h1_all: ", h1_all)

url_links = soup.select("a")
for link in url_links :
    print(link["href"])

# 자식 관계로 접근 
div_urls = soup.select("div#class1 > a")
print(div_urls)
print(div_urls[0]["href"])

# 자손관계로 접근
div_urls2 = soup.select("div#class1 a")

print(div_urls2)

# select에서 여러 항목 검색하기 : ,로 나열
h1 = soup.select("#heading, #footer")
print(h1)

# class
url_links = soup.select("a.external_link, a.internal_link")
print(url_links)