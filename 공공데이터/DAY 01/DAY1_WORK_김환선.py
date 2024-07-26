import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import pandas as pd 

weather_df = pd.read_csv("daegu-utf8.csv")

weather_df.columns = ["날짜", "지점", "평균기온", "최저기온", "최고기온"]
weather_df["날짜"] = pd.to_datetime(weather_df["날짜"].str.strip(), format='%Y-%m-%d')

max_tem = []
mini_tem = []
start_year = int(input("시작 연도를 입력하세요 : "))
end_year = int(input("마지막 연도를 입력하세요 : "))
check_month = int(input("기온 변화를 측정할 달을 입력하세요 : "))

print(f'{start_year}년 부터 {end_year}까지 {check_month}월의 기온 변화')

years = list(range(start_year, end_year + 1))

for year in years:
    year_month_df = weather_df[(weather_df["날짜"].dt.year == year) &
                               (weather_df["날짜"].dt.month == check_month)]
    if not year_month_df.empty:
        max_tem.append(round(year_month_df["최고기온"].mean(), 2))
        mini_tem.append(round(year_month_df["최저기온"].mean(), 2))
    else:
        max_tem.append(None)
        mini_tem.append(None)

print(f"{check_month}월의 최저기온 평균 : ", mini_tem, sep = "\n")
print()
print(f"{check_month}월의 최고기온 평균 : ", max_tem, sep = "\n")

def draw_two_plots(x_data, max_tem, mini_tem):
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(17, 5))
    plt.plot(x_data, max_tem, marker='s', markersize=6, color='r', label="최고기온")
    plt.plot(x_data, mini_tem, marker='s', markersize=6, color='b', label="최저기온")
    plt.xticks(x_data)
    plt.xlabel('년도')
    plt.ylabel('기온')
    plt.title(f'{start_year}년 부터 {end_year}까지 {check_month}월의 기온 변화')
    plt.legend()
    plt.show()

draw_two_plots(years, max_tem, mini_tem)
