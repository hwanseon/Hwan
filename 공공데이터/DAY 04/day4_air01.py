import pandas as pd
from tabulate import tabulate

file1 = r"C:\Hwan\공공데이터\DAY 04\dust.xlsx"
file2 = r"C:\Hwan\공공데이터\DAY 04\weather.xlsx"

dust = pd.read_excel(file1)

print(dust.head())
print(tabulate(dust.head(), headers = "keys", tablefmt = "pretty"))

print(dust.info())

# colums 이름을 영문으로 변경
dust.rename(columns = {"날짜":"date", "아황산가스":"so2", "일산화탄소":"co", "오존":"o3",
                       "이산화질소":"no2"}, inplace = True)

print(tabulate(dust.head(), headers = "keys", tablefmt = "psql"))

# 날짜 데이터를 시간 없애고 날짜 데이터만으로 변경
dust["date"] = dust["date"].str[:10]
print(tabulate(dust.head(), headers = "keys", tablefmt = "psql"))

# DATE 열을 DATETIME 타입으로 변경
dust["date"] = pd.to_datetime(dust["date"])
print(dust.dtypes)

# date colunms에서 년도, 월, 일을 추출하여 새로운 칼럼 생성
dust["year"] = dust["date"].dt.year
dust["month"] = dust["date"].dt.month
dust["day"] = dust["date"].dt.day

# columns 순서 재정렬
dust = dust[["date", "year", "month", "day", "so2", "co", "o3", "no2", "PM10", "PM2.5"]]
print(tabulate(dust.head(), headers = "keys", tablefmt = "psql"))

# 결측치 개수 확인
print("결측치 개수 확인하기")
print(dust.isna().sum())

# 결측치를 포함하는 행 출력
print("결측치를 포함한 데이터 출력")
print(dust[dust.isna().any(axis=1)])

# 결측치 채우기
print("결측치 채우기")
dust.ffill(inplace = True)
print(dust.isnull().sum())

# 이전의 결측치의 index를 재출력하여 확인
print(dust.iloc[132:134])
print(dust.iloc[368:370])
print(dust.iloc[444:446])

# ---------------------------------------------------------------------------------

# data 엑셀 파일 읽기
weather = pd.read_excel(file2)
print(tabulate(weather.head(), headers = "keys", tablefmt = "psql"))

# 날씨 데이터 기본 정보 출력
print(weather.info()) # date의 값 자체가 datetime 형태로 지정되어 있기에 읽어오면 자동으로 datetime으로 인식

# 불필요 칼럼 삭제 및 칼럼 이름 영문으로 변경
weather.drop(["지점", "지점명"], axis = 1, inplace = True)

weather.columns = ["date", "temp", "wind", "rain", "humidity"]
print(tabulate(weather.head(), headers = "keys", tablefmt = "pretty"))

# 칼럼에서 시간 정보 삭제 후 데이터 타입 확인 
weather["date"] = pd.to_datetime(weather["date"].dt.date)
print(weather.info())
print(weather.head())

# 날씨 데이터 결측치 개수 확인 
print("날씨 데이터 결측치 개수 확인")
print(weather.isna().sum())

print("날씨 데이터에서 결측치를 포함하는 행 출력")
print(weather[weather.isna().any(axis=1)])

# 날씨 데이터 결측치 채우기
weather.ffill(inplace=True)
print(weather.isna().sum())

# 이전 결측치의 index의 값 비교
print(weather.iloc[[369, 565, 742]])

# 강수량 데이터 변경
print("강수량이 0인 항목을 0.01로 변경")
weather["rain"] = weather["rain"].replace(0,0.01)
print(weather["rain"].value_counts())

# -------------------------------------------------------------------------------------------
# 2개의 데이터 병합
print("dust, weather의 크기 확인")
print("dust.shape", dust.shape)         # 24:00:00 데이터까지 포함
print("weather.shape", weather.shape)   # 23시까지 있고 24시 데이터는 다음날 데이터의 00시로 인식되어 빠짐

# 미세먼지 데이터의 마지막 부분 확인
print(dust.iloc[740:])

# 날씨 데이터의 마지막 부분 확인
print(weather.iloc[740:])

# 미세먼지 데이터의 마지막 행 삭제 후 크기 확인
dust.drop(index = 743, inplace = True)
print(dust.shape)

# 데이터 프레임 병합
print("dust, weather 데이터프레임 merge")

merge_df = pd.merge(dust, weather, on = "date")
print(merge_df)

# 모든 요소별 상관관계 확인
# 보통 데이터가 많으면 짤려서 출력이 되는데 밑에 함수를 사용해서 데이터 전체 출력시킴 
pd.set_option("display.max_columns", None) # 전체 칼럼 출력
pd.set_option("display.max_rows", None)    # 전체 행 출력 

print(merge_df.corr())

# 미세먼지 (PM10)과 상관관계 
print("미세먼지(PM10)과 상관관계 분석")
corr = merge_df.corr()
print(corr["PM10"].sort_values(ascending=False)) # 내림차순 정렬

# 각 칼럼별 히스토그램 작성
import matplotlib.pyplot as plt

merge_df.hist(column = ["so2", "co", "o3", "no2", "PM10", "PM2.5", "temp", "wind", "rain", "humidity"],
              bins = 50, figsize = (20, 15))

plt.show()

# PM10의 농도 막대 그래프
import seaborn as sns
import koreanize_matplotlib

plt.figure(figsize = (15, 10))
daygraph = sns.barplot(x ="day", y ="PM10", data = merge_df)
plt.title("날짜별 PM10 농도")
plt.show()

# 히트맵 작성
plt.figure(figsize = (15, 10))
sns.heatmap(data = corr, annot = True, fmt = ".2f", cmap = "hot")
plt.show()

# 산점도 
plt.figure(figsize=(15, 10))
x = merge_df["PM10"]
y = merge_df["PM2.5"]

plt.plot(x, y, marker = "o", linestyle = "none", color = "red", alpha = 0.5)
plt.title("PM10 vs PM2.5")
plt.xlabel("PM10")
plt.ylabel("PM2.5")
plt.shoW()