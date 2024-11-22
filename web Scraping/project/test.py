from urllib.request import Request
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import collections

if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

def search_job(number):
    try:
        search_word = quote('AI연구원')
        url = f'https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&recruitPage={number}&recruitPageCount=100&searchType=search&searchword={search_word}'

        urlrequest = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(urlrequest)

        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.find('div', {'class':'content'})
        items = contents.select('div.item_recruit > div.area_job > div.job_sector')
        for item in items:
            item_string = item.text.replace('\n', '').strip()
            print(item_string)
    except Exception as e:
        print(e)

for i in range(1,10):
    search_job(i)
