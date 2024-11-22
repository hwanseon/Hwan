import csv
csvFile = open("test.csv", "w", encoding = "utf-8")

try:
    writer = csv.writer(csvFile)
    writer.writerow("number", "number+2", "(number+2)^2")

    for i in range(10) :
        writer.writerow(i, i+2, pow(i+2, 2))
except Exception as e:
    print(e)

finally :
    csvFile.close()

# 테이블 데이터를 csv로 저장
from urllib.request import urlopen
from bs4 import  BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, "html.parser")

table = bs.find_all("table", {"class":"wikitable"})
rows = table.find_all("tr")

csvFile = open("editors.csv", "wt", encoding="utf-8")
writer = csv.writer(csvFile)

try:
    for row in rows :
        csvRow = []
        for cell in row.find_all(["th", "td"]) :
            print(cell.text.strip())
            csvRow.append(cell.text.strip())
        writer.writerow(csvRow)

finally:
    csvFile.close()
# 해더의 정보가 잘못됨 

# 하나의 칼럼에서 분할이 되었을때 설치 라이브러리 : pip	install	html_table_parser
from html_table_parser import parser_functions as parse
import pandas as pd
import collections

# if not hasattr(collections, "Callable") :
collections.Callable = collections.abc.Callable

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, "html.parser")

table = bs.find_all("table", {"class":"wikitable"})
table_data = parse.make2d(table) # 2차원 리스트 형태로 변환

print("[0] : ", table_data[0])
print("[1] : ", table_data[1])

# pandas DataFrame으로 저장 (2행부터 데이터 저장)
df = pd.DataFrame(table_data[2:], columns = table_data[1])
print(df.head())

# csv 파일로 저장
csvFile = open("editors1.csv", "wt", encoding="utf-8")
writer = csv.writer(row)

for row in table_data:
    writer.writerow(row)

csvFile.close()