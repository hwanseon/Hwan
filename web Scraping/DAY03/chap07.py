# 네이버 검색 API 예제 - 블로그 검색
# 네이버에서 제공하는 기본 소스코드
import os
import sys
import urllib.request
client_id = "p2wVJWa62O3VIgit27no"
client_secret = "3Xq2zzahe9"

encText = urllib.parse.quote("빅데이터")        # 검색할 단어

url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 형태의 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):       # 200은 sucess를 의미함
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

import	urllib.request
import	datetime
import	json

def	get_request_url(url):
    client_id = "p2wVJWa62O3VIgit27no"
    client_secret = "3Xq2zzahe9"
    req	=	urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",	client_id)
    req.add_header("X-Naver-Client-Secret",	client_secret)
    try:
        response	=	urllib.request.urlopen(req)
        if	response.getcode()	==	200:												
            return	response.read().decode('utf-8')
    except	Exception	as	e:
        print(e)
        print(f"Error	for	URL:	{url}")

def	get_naver_search(node,	search_text,	start,	display):
    base	=	"https://openapi.naver.com/v1/search"
    node	=	f"/{node}.json"
    query_string	=	f"{urllib.parse.quote(search_text)}"
     #	f"?query={query_string}&start={start}&display={display}"
    parameters	=	("?query={}&start={}&display={}".
                    format(query_string,	start,	display))
    
    url	=	base	+	node	+	parameters
    response	=	get_request_url(url)

    if response is None :
        return None
    else :
        return json.loads(response)
    
def	main():
    node	=	'news'		#	크롤링 대상
    #	search_text	=	input('검색어를 입력하세요:	')
    search_text	=	'인공지능'
    cnt	=	0
    json_response	=	get_naver_search(node,	search_text,	1,	100)
    if	(json_response	is	not	None)	and	(json_response['display']	!=	0):
        for	post	in	json_response['items']:
            cnt	+=	1
#	1단계
        print(f"[{cnt}]", end=" ")
        print(post['title'])
        print(post['description'])
        print(post['originallink'])
        print(post['link'])
        print(post['pubDate'])

if	__name__	==	'__main__':
    main()

import datetime
import pandas as pd

date_string = "Tue, 13 Aug 2024 09:02:00 +0900"

pdate = datetime.datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S +0900")
print(type(pdate))

pdate_string = pdate.strftime("%Y-%m-%d %H:%M:%S")
print(type(pdate_string))
print(pdate_string)

def get_post_data(post, json_result_list, cnt):
    title = post["title"]
    description = post["description"]
    org_link = post["originallink"]
    link = post["link"]

    pdate = datetime.datetime.strptime(post["pubDate"], "%a, %d %b %Y %H:%M:%S +0900")
    pdate = pdate.strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{cnt}]", end = " ")
    print(title, end = " ")
    print(pdate, end = " ")
    print(link)

    json_result_list.append([cnt, pdate, title, description, org_link, link])

def main():
    node = "news"
    search_text = "인공지능"
    cnt = 0
    json_result_list = []

    json_reponse = get_naver_search(node, search_text, 1, 100)
    while (json_reponse is not None) and (json_reponse["display"] != 0) :
        for post in json_reponse["items"]:
            cnt += 1
            get_post_data(post, json_result_list, cnt)
        
        start = json_reponse["start"] + json_reponse["display"]
        json_reponse = get_naver_search(node, search_text, start, 100)

    print(f"전체 검색 수 : {cnt}")

    columns = ["count", "date", "title", "description", "org_link", "link"]
    result_df = pd.DataFrame(json_result_list, columns = columns)
    result_df.to_csv(f"{search_text}_naver_{node}.csv", index = False, encoding = "utf-8")

if __name__ == "__main__":
    main()
