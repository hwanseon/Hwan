## 김환선 공공데이터 project
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib 
import pandas as pd
from tabulate import tabulate

file1 = r"C:\Hwan\공공데이터\project\DATA\2020년 신재생 에너지 지역별 비율 EPSIS.csv"

county_new_engery = pd.read_csv(file1, encoding='cp949')
print(county_new_engery)

# 불필요 행 및 칼럼 삭제
county_new_engery.drop(index = 0, inplace = True)
county_new_engery.drop(["회원구분", "급전방식", "사업구분"], axis =1, inplace = True)
county_new_engery.drop(county_new_engery.columns[2:12], axis = 1, inplace=True)
county_new_engery.drop(county_new_engery.columns[3:], axis = 1, inplace=True)

print(tabulate(county_new_engery.head(), headers = "keys", tablefmt = "pretty"))

# 결측치 확인
print(county_new_engery.isna().sum())

# 기간 뒤에 소수점 제거
county_new_engery["기간"] = county_new_engery["기간"].astype(int)
print(tabulate(county_new_engery.head(), headers = "keys", tablefmt = "pretty"))
print(county_new_engery.dtypes)

# 지역별 신재생 에너지의 량 구하기
for year in [2023, 2022, 2021, 2020]:
    year_data = county_new_engery[(county_new_engery["기간"] == year) & (county_new_engery["지역"] != "소계")]
    print(f"\n{year}년 지역별 신재생 에너지 값:")
    print(tabulate(year_data, headers="keys", tablefmt="pretty"))

    plt.figure(figsize=(10, 6))
    plt.bar(year_data["지역"], year_data["신재생"])
    plt.xlabel('지역')
    plt.ylabel('신재생 에너지의 양')
    plt.title(f'{year}년 지역별 신재생 에너지의 양')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

### 결론: 신재생 에너지의 사용량이 전남이 가장 많음 

# ---------------------------------------------------------------------------------------------------------------------
# 2020 ~ 2022 대한민국 신재생 에너지 중에서 태양광이 차지 하는 비율 
file2 = r"C:\Hwan\공공데이터\project\DATA\신재생에너지_발전_및_열공급업_현황__사업체수_20240731161339_KOSIS.csv"

new_engery = pd.read_csv(file2, encoding='cp949')

# 필요없는 행 및 칼럼 삭제
new_engery.drop(index = [0, 1], inplace =True)
new_engery.drop("업종별(1)", axis = 1, inplace = True)
new_engery.columns = ["업종별", 2020, 2021, 2022]
print(tabulate(new_engery.head(), headers = "keys", tablefmt = "pretty"))

# 결측치 확인
print(new_engery.isna().sum())
# 데이터 값이 없는 것이 있는데 결측치 = 0 으로 인식
print(new_engery.dtypes) # object 객체 

# X data -> 0으로 변경
for i in [2020, 2021, 2022] :
    new_engery[i].replace('X',0, inplace=True)
    
# 2020, 2021, 2022 칼럼 : int 타입으로 변경
for i in [2020, 2021, 2022] :
    new_engery[i] = new_engery[i].astype(int)

print(new_engery.dtypes)

# 각 연도별 꺾은선 그래프 작성

df = pd.DataFrame({
   '태양E': [77737, 97220, 114715],
   '풍력E' : [93, 96, 92],
   "수력E" : [124, 131, 125],
   "해양E" : [0 ,0 ,0],
   "바이오E": [105, 109, 80],
   "폐기물E": [105, 109, 80],
   "연료전지": [63, 71, 75],
   "기타" : [0, 0, 0],
   "증기" : [104, 116, 105]}, index=[2020, 2021, 2022])

ax = df.plot(kind='line', figsize=(12, 8))
ax.set_title('2020 ~ 2022년 신재생 에너지 업종별 사용량')
ax.set_xlabel('년도')
ax.set_ylabel('에너지별 사용량')
plt.legend(title='업종', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# # 태양에너지를 제거 (값이 너무 높기에 다른 그래프들이 안보임)
df = pd.DataFrame({
   '풍력E' : [93, 96, 92],
   "수력E" : [124, 131, 125],
   "해양E" : [0 ,0 ,0],
   "바이오E": [105, 109, 80],
   "폐기물E": [105, 109, 80],
   "연료전지": [63, 71, 75],
   "기타" : [0, 0, 0],
   "증기" : [104, 116, 105]}, index=[2020, 2021, 2022])

ax = df.plot(kind='line', figsize=(12, 8))
ax.set_title('2020 ~ 2022년 신재생 에너지 업종별 사용량')
ax.set_xlabel('년도')
ax.set_ylabel('에너지별 사용량')
plt.legend(title='업종', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 필요없음
# plt.figure(figsize=(10, 6))
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
# plt.xlabel('년도')
# plt.ylabel('업종별 사용량')
# plt.title('2020 ~ 2022년 신재생 에너지 업종별 사용량')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

## 결론 : 신재생 에너지 중에서 태양에너지의 사용량이 압도적으로 높음 -> 우리 주변에서 쉽게 접할 수 있음
## ------------------------------------------------------------------------------------------
# 2021 ~ 2024년 상반기 자가용 태양광 설치 데이터 
file4 = r"C:\Hwan\공공데이터\project\DATA\2020 자가용 태양광 설치 현황_EPSIS.csv"

sun = pd.read_csv(file4, encoding='cp949')
print(tabulate(sun.head(), headers = "keys", tablefmt = "pretty"))

# 필요없는 칼럼 제거
sun.drop(sun.columns[1:3], axis = 1, inplace = True)
sun.columns = ["날짜", "자가용 태양광 설치현황"]
print(tabulate(sun.head(), headers = "keys", tablefmt = "pretty"))

# 날짜 칼럼에서 연도 추출
sun['날짜'] = sun['날짜'].astype(int)

# 날짜를 인덱스로
print(tabulate(sun.head(), headers = "keys", tablefmt = "pretty"))
print(sun.groupby("날짜").get_group(2024).sum())
print(sun.groupby("날짜").get_group(2023).sum())
print(sun.groupby("날짜").get_group(2022).sum())
print(sun.groupby("날짜").get_group(2021).sum())

sun_sum = [2731072, 6018531, 5936648, 2408906]

# 연도별 설치현황 막대그래프 그리기
plt.figure(figsize=(12, 8))
plt.bar(["2021", "2022", "2023", "2024"], [2731072, 6018531, 5936648, 2408906])
plt.xlabel('년도')
plt.ylabel('자가용 태양광 설치현황')
plt.title('2021 ~ 2024년 상반기 자가용 태양광 설치현황')
plt.tight_layout()
plt.show()
# 결론 : 태양광 에너지 설치 비율은 날이 갈수록 증가
# -------------------------------------------------------------------------------------
# # 전국별 스마트팜 현황
file5 = r"C:\Hwan\공공데이터\project\DATA\2020년 스마트팜 농업 비율_스마트팜코리아.csv"

smartfarm = pd.read_csv(file5)
print(tabulate(smartfarm.head(), headers = "keys", tablefmt = "pretty"))

smartfarm.drop(smartfarm.columns[1:4], axis = 1, inplace = True)
print(tabulate(smartfarm.head(), headers = "keys", tablefmt = "pretty"))

# 막대그래프 그리기
plt.figure(figsize=(12, 8))
plt.bar(smartfarm['지역'], smartfarm['합계'])
plt.xlabel('지역')
plt.ylabel('합계')
plt.title('2024년 스마트팜 비율')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 결론: 전라남도의 스마트팜 비율이 가장 높다 
# -------------------------------------------------------------------------------------
# 기온그래프 

import numpy as np

file6 = r"C:\Hwan\공공데이터\project\DATA\년도별_평균기온.xls"
raw_temp_df = pd.read_csv(file6, encoding='euc_kr', header=6, delimiter='\t')
raw_temp_df

print(raw_temp_df.info())

# 지점 칼럼 삭제
raw_temp_df.drop('지점', axis=1, inplace=True)
#raw_temp_df

# 데이터프레임 컬럼 이름 변경
# 년: year, '평균기온(℃)': ave_temp, '평균최저기온(℃)': min_temp, '평균최고기온(℃)': max_temp
raw_temp_df.rename(columns={'년': 'year', '평균기온(℃)': 'ave_temp', 
                            '평균최저기온(℃)': 'min_temp', '평균최고기온(℃)': 'max_temp'}, inplace=True)
#raw_temp_df.columns


# 2018 ~ 2022년 DF 추출
source_DF = raw_temp_df.iloc[8:13]
# source_DF

# 그래프 plot
plt.figure(figsize=(8,6))

x = source_DF['year']

temp_y1 = source_DF['ave_temp']
temp_y2 = source_DF['min_temp']
temp_y3 = source_DF['max_temp']

plt.plot(x,temp_y1, label='평균기온', marker='o', ms=4, color='k')
plt.plot(x,temp_y2, label='평균최저기온', marker='s',color='blue')
plt.plot(x,temp_y3, label='평균최고기온', marker='s', color='red')

plt.title("2018 - 2022 년별 평균기온 변화")
plt.xticks(x, labels=range(2018,2023))
plt.ylim(bottom=0, top=22)
plt.legend(loc=4)
plt.show()
# -------------------------------------------------------------------------------------
# 전라도 기온 함수
file7 = r"C:\Hwan\공공데이터\project\DATA\2018, 2024 전남 기온 데이터.csv"

data = pd.read_csv(file7, encoding='euc-kr')

# 불필요한 공백 제거
data['년월'] = data['년월'].str.strip()

# '년월' 열을 datetime 형식으로 변환
data['년월'] = pd.to_datetime(data['년월'], format='%Y-%m')

# '년월'을 인덱스로 설정
data.set_index('년월', inplace=True)

# 그래프 그리기
plt.figure(figsize=(14, 8))
plt.plot(data.index, data['평균기온(℃)'], label='평균기온 (℃)', marker='o')
plt.plot(data.index, data['평균최저기온(℃)'], label='최저기온의 평균기온 (℃)', marker='o')
plt.plot(data.index, data['평균최고기온(℃)'], label='최대온도의 평균기온(℃)', marker='o')

# 제목과 라벨 추가
plt.title('2018 ~ 2024년 전라남도 기온 데이터')
plt.xlabel('년-월')
plt.ylabel('온도 (℃)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ------------------------------------------------------------------------------------
# 2020 전국 월별 평균 일조량 데이터
file8 = r"C:\Hwan\공공데이터\project\DATA\2020_전국 일조량 데이터.csv"

sunny = pd.read_csv(file8, encoding='euc-kr')

plt.figure(figsize=(14, 10))

for column in sunny.columns[1:]:
    plt.plot(sunny['월'], sunny[column], marker='o', label=column)

plt.title('2020년 전국 월별 평균 일조량')
plt.xlabel('월')
plt.ylabel('일조 시간 (시간)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.tight_layout()

plt.show()
# 결론 : 전남이 높은 편에 속함
# -------------------------------------------------------------------------------------
# 망한 데이터
# ## 농가수별 태양광 에너지가 없기에 전국 데이터 중에서 농가의 수가 가장 높은 곳을 찾음
# ## 농가 데이터, 2020년 기준

# file3 = r"C:\Hwan\공공데이터\project\DATA\2020 지역별 농가의 수_KOSIS.csv"

# field = pd.read_csv(file3, encoding='cp949', skiprows=1)

# # 불 필요 칼럼 제거 및 인덱스 재설정
# field.drop(index = range(0, 32), inplace = True)
# field.drop(field.columns[3:], axis = 1, inplace = True)
# print(tabulate(field.head(), headers = "keys", tablefmt = "pretty"))
# field = field[field['특성별'] == "계"]
# field.reset_index(drop=True, inplace=True)

# print(tabulate(field.head(), headers="keys", tablefmt="pretty"))

# # 지역별 농가수 막대그래프 그리기 
# plt.figure(figsize=(12, 8))
# plt.bar(field['행정구역별'], field['농가 (가구)'])
# plt.xlabel('행정구역')
# plt.ylabel('농가 수')
# plt.title('2020년 지역별 농가의 수')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()