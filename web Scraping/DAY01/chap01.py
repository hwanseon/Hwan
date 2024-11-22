from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.daangn.com/fleamarket/")
print(type(html))
print(html.read())

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), "html.parser")
print(bs)
print()
print(bs.h1)
print()
print(bs.h1.string) # 태그 내부의 문자열만 가져옴
print(bs.h1.text)   # 14라인과 같음
print()
print(bs.div.text) # <div> 텍스트 ... </div> 에서 텍스트 정보만 가져옴

"""
웹 페이지 소스 보기

<html>
<head>
<title>A Useful Page</title>
</head>
<body>
<h1>An Interesting Title</h1>               # </h1> 끝나는 부분 // <h1> 시작하는 부분 
<div>
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</div>
</body>
</html>

<html> ~ </html> 한쌍 
<head> ~ </head> 속성 : 눈에 보이지 않음
<body> ~ </body> 실제 웹 사이트에서 보이는 부분 

bs.h1 = > <h1>An Interesting Title</h1> 
bs.h1.string (문자열) => Interesting Title

왼쪽 상단 점 3개 -> 도구 더보기 -> 개발자 도구에서 문자가 어디 코드인지 확인하기

"""
 
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://www.pythonscraping.com/pages/error.html')
except HTTPError as e :
    print(e)
except URLError as e :
    print("The server could not be found!")
else :
    print("It worked!")

from bs4 import BeautifulSoup

def getTitle (url, tag) :
    try :
        html = urlopen(url)
    except HTTPError as e :
        return None
    
    try :
        bs0bj = BeautifulSoup(html.read(), "html.parser")
        value = bs0bj.body.find(tag)
    except AttributeError as e :
        return None
    return value

tag = "h2"
value = getTitle('http://www.pythonscraping.com/pages/page1.html',	tag)

if value == None :
    print(f"{tag} could not be found")
else :
    print(value)

# 멜론 웹사이트 접속

# -----------------------------------------------------
# <사용자 정보를 입력하지 않았을떄>
# 샘플코드 1
# urllib.error.HTTPError:	HTTP	Error	406:	Not	Acceptable	발생

melon_url = 'https://www.melon.com/chart/index.htm'
# html = urlopen(melon_url)

# soup = BeautifulSoup(html.read(), "html.parser")
# print(soup) # 사용자 정보가 없기때문에 오류가 발생함
# -----------------------------------------------------
from urllib.request import Request
urlrequest = Request(melon_url, headers = {"User-Agent":"Mozilla/5.0"})

html = urlopen(urlrequest)
soup = BeautifulSoup(html.read().decode("utf-8"), "html.parser")

print(soup)

# User-Agent 사용법
# p16