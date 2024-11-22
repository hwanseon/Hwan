from urllib.request import urlopen
from bs4 import	BeautifulSoup
import re
import requests
import csv 

head_name = ["매장이름", "지역", "주소", "전화번호"]

f = open("C:\Hwan\web Scraping\DAY02\WORK\hollys_branches.csv", "w", encoding="utf-8")
writer = csv.writer(f)
writer.writerow(head_name)

for query in range(1, 51) :
    query 
    hollys_web = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={query}&sido=&gugun=&store="
    html = urlopen(hollys_web)
    soup = BeautifulSoup(html.read(), "html.parser")

    hollys_index = soup.find("tbody").find_all("tr")  

    for num in hollys_index:
            hollys_region = num.find_all("td", class_ = "noline center_t")[0]
            hollys_region = hollys_region.text

            hollys_name = num.find_all("td", class_ = "center_t")[1]
            hollys_name = hollys_name.text

            hollys_location = num.find_all("td", class_ = "center_t")[3]
            hollys_location = hollys_location.text

            hollys_call = num.find_all("td", class_ = "center_t")[5]
            hollys_call = hollys_call.text

            writer.writerow([hollys_region, hollys_name, hollys_location, hollys_call])

f.close()