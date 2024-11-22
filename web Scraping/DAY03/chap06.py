# 하나의 칼럼에서 분할이 되었을때 설치 라이브러리 : pip	install	html_table_parser
from html_table_parser import parser_functions as parse
import pandas as pd
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen
import collections

if not hasattr(collections, "Callable") :
    collections.Callable = collections.abc.Callable

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, "html.parser")

table = bs.find("table", {"class":"wikitable"})
table_data = parse.make2d(table) # 2차원 리스트 형태로 변환

print("[0] : ", table_data[0])
print("[1] : ", table_data[1])

# pandas DataFrame으로 저장 (2행부터 데이터 저장)
df = pd.DataFrame(table_data[2:], columns = table_data[1])
print(df.head())

# csv 파일로 저장
csvFile = open("editors1.csv", "wt", encoding="utf-8")
writer = csv.writer(csvFile)

for row in table_data:
    writer.writerow(row)

csvFile.close()

# page table에서 id 값이 2인 데이터 가져오기
import pymysql

conn = pymysql.connect(host = "localhost", user="hwansun", passwd = "1234", db = "scraping", charset = "utf8")

cur = conn.cursor()
cur.execute("use scraping")
cur.execute("select * from pages where id-2")

print(cur.fetchone())
cur.close()
conn.close()

import random
import re
import collections

if not hasattr(collections, "Callable") :
    collections.Callable = collections.abc.Callable

def store(conn, cur, title, content) :
    cur.execute("insert into pages (title, content) values ('%s', '%s')", (title, content))
    conn.commit()

def get_links(conn, cur, articleUrl) :
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html, "html.parser")

    title = bs.find("h1").text
    content = bs.find("div", {"id":"mw-content-text"}).find("p").text
    print(title, content)

    store(conn, cur, title, content)

    return bs.find("div", {"id":"bodyContent"}).\
            find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def main():
    conn = pymysql.connect(host =8 "localhost", user="hwansun", passwd = "1234", db = "scraping", charset = "utf8")
    cur = conn.cursor()
    random.seed(None)

    links = get_links(conn, cur, '/wiki/Kevin_Bacon')

    try:
        while len(links) >0 :
            newArticle	=	links[random.randint(0,	len(links)-1)].attrs['href']
            print(newArticle)
            links	=	get_links(conn,	cur,	newArticle)
    finally:
        cur.close()
        conn.close()


main()