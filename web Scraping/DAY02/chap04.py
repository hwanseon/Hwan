from urllib.request import urlopen
from	bs4	import	BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, "html.parser")
for link in bs.find_all("a") :
    if "href" in link.attrs:
        print(link.attrs["href"])

# 연관 기사 링크 찾기
import re
html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, "html.parser")
body_content = bs.find("div", {"id":"bodyContent"})

pattern = "^(/wiki/)((?!:).)*$"
for link in body_content.find_all("a", href = re.compile(pattern)) :
    if "href" in link.attrs:
        print(link.attrs["href"])

## 링크 간 무작위로 이동하기 
# import random

# random.seed(None)

# def getLinks(articleUrl) :
#     html = urlopen('https://en.wikipedia.org' + articleUrl)
#     bs = BeautifulSoup(html, "html.parser")
#     bodyContent = bs.find("div", {"id":"bodyContent"})
#     wikiUrl = bodyContent.find_all("a", href=re.compile('^(/wiki/)((?!:).)*$'))
#     return wikiUrl

# links = getLinks('/wiki/Kevin_Bacon')
# print("links의 길이 : ", len(links))

# while len(links) > 0 :
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)

# # 전체 사이트 데이터 수집 소스
# pages =	set()
# count = 0
# def	getLinks(pageUrl):
#     global	pages
#     global	count
#     html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
#     bs = BeautifulSoup(html,	'html.parser')
#     try:
#         print(bs.h1.get_text())	#	<h1>태그 검색
#         #print(bs.find(id='mw-content-text').find('p').text)
#         print(bs.find('div',	attrs={'id':	'mw-content-text'}).find('p').text)
#     except	AttributeError	as	e:
#         print('this	page	is	missing	something!	Continuing:	',	e)
    
#     pattern	=	'^(/wiki/)((?!:).)*$'
    
#     for	link in	bs.find_all('a', href=re.compile(pattern)):
#         if 'href' in link.attrs:
#             if	link.attrs['href']	not	in	pages:
#                 newPage	=	link.attrs['href']
#                 print('-'*40)
#                 count	+=	1
#                 print(f'[{count}]:	{newPage}')
#                 pages.add(newPage)
#                 getLinks(newPage)
# getLinks('')

# 인터넷 크롤링 : url 구조
from urllib.parse import urlparse

urlString1 = r'https://shopping.naver.com/home/p/index.naver'

url = urlparse(urlString1)
print(url.scheme)
print(url.netloc)
print(url.path)

# ---------------------------------------------------------------------------------
# naver blog search 
## 프로젝트 시 사용 가능함

# 쿼리를 한국어로 쓰고 싶으면 
# from urllib.parse import quote를 하고
# query = quote("c챗지피티") 로 하면 됨

import requests

query = "ChatGPT"
url = f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={query}'

html = urlopen(url)
soup = BeautifulSoup(html.read(), "html.parser")
blog_results = soup.select("a.title_link") # 검색 블로그의 타이틀
print("검색 결과 수 : ", len(blog_results))
search_count = len(blog_results)
desc_results = soup.select("a.dsc_link") # 검색된 블로그의 간단한 설명

for blog_title in blog_results :
    title = blog_title.textlink = blog_title["href"]
    print(f"{title}, [{link}]")

for i in range(search_count) :
    title = blog_results[i].text
    link = blog_results[i]["href"]
    print(f"{title}, [{link}]")
    print(desc_results[i].text)
    print("-"*80)
