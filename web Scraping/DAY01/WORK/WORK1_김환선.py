from urllib.request import urlopen
from bs4 import BeautifulSoup

# weateher_url = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY"
# urlrequest = Request(weateher_url, headers={"User-Agent":"Mozilla/5.0"})

# html = urlopen(urlrequest)
# soup = BeautifulSoup(html.read().decode("utf-8"), "html.parser")
# print(soup)

# bs = BeautifulSoup(html.read(), "html.parser")
# print(bs.h1)


def scraping_use_find(html) :
    print("[find 함수 사용]")
    weather = html.find_all("div", {"class":"tombstone-container"})
    print(f"총 tombstone-container의 검색 개수 : {len(weather)}개")
    print('-' * 70)

    for w in weather :

        weather_period_find = w.find("p", {"class":"period-name"}).string   
        print(f"[Period]: {weather_period_find}")

        weather_short_find = w.find("p", {"class":"short-desc"}).string  
        print(f"[Short desc]: {weather_short_find}")

        weather_temp_find = w.find("p", {"class":"temp temp-low"})
        print(f"[Temperature]: {weather_temp_find}")

        weather_img_find = w.find("img")["title"]
        print(f"[Image desc]: {weather_img_find}")
        print('-' * 70)

def parse_use_select(html) :
    print("[select 함수 사용]")
    weather = html.select("div.tombstone-container")
    print(f"총 tombstone-container의 검색 개수 : {len(weather)}개")
    print('-' * 70)

    for w in weather :

        weather_period_select = w.select_one("p.period-name").string      
        print(f"[Period]: {weather_period_select}")

        weather_short_select = w.select_one("p.short-desc").string  
        print(f"[Short desc]: {weather_short_select}")

        weather_temp_select = w.select_one("p.temp temp-low") 
        print(f"[Temperature]: {weather_temp_select}")

        weather_img_select = w.select_one("img")["title"]
        print(f"[Image desc]: {weather_img_select}")
        print('-' * 70)

def main():
    weateher_url = r"https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Yst5ji9yxTY"
    page = urlopen(weateher_url)
    html = BeautifulSoup(page.read(), "html.parser") # 전체 페이지

    print("National Weather Service Scraping")
    print("-"*25)

    scraping_use_find(html)
    print()
    print()
    parse_use_select(html)

main()