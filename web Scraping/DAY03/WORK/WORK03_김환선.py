import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from tabulate import tabulate
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_market_sum.naver"
html = requests.get(url)
soup = BeautifulSoup(html, "html.parser")

nums = soup.find_all("a")["href"]
nums.rfind(7)

print(nums)
# driver = webdriver.Chrome(f"https://finance.naver.com/sise/sise_market_sum.naver?code="+"{nums}")
# driver.get()

# <a href="/item/main.naver?code=005930" class="tltle">삼성전자</a>