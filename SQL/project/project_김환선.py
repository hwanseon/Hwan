import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import csv
import koreanize_matplotlib
from tabulate import tabulate

water = pymysql.connect(host = "172.20.145.44", user = "hwansun", password = "1234", db = "mini_project", charset = "utf8")


cur = water.cursor()
cur.execute("SELECT * FROM water")

# desc = cur.description
# for i in range(len(desc)):
#     print(desc[i][0], end = " ")
# print()

rows = cur.fetchall()
# print(rows)

water_df = pd.DataFrame(rows)
print(tabulate(water_df.head(), headers = "keys", tablefmt = "pretty"))

cur.close()
water.close()

water_df_sorted = water_df.sort_values(by=1, ascending=False)
top_10 = water_df_sorted.head(10)
bottom_10 = water_df_sorted.tail(10)

# 에비앙 가격 상위 10개국 추출 
plt.figure(figsize=(10, 8))
plt.bar(top_10[0], top_10[1], color='pink')
plt.xlabel('Country')
plt.ylabel("에비앙 가격 $")
plt.title('[나라별 에비앙 가격 - 상위 10개국]')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# 에비앙 가격 하위 10개국 추출
plt.figure(figsize=(10, 8))
plt.bar(bottom_10[0], bottom_10[1], color='pink')
plt.xlabel('Country')
plt.ylabel("에비앙 가격 $")
plt.title('[나라별 에비앙 가격 - 하위 10개국]')
plt.xticks(rotation=45)
plt.legend()
plt.show()

## 지하수 데이터 시각화
ground_Water = pymysql.connect(host = "172.20.145.44", user = "hwansun", password = "1234", db = "mini_project", charset = "utf8")

cur = ground_Water.cursor()
cur.execute("SELECT * FROM ground_water")

rows = cur.fetchall()

ground_Water_df = pd.DataFrame(rows)
print(tabulate(ground_Water_df.head(), headers = "keys", tablefmt = "pretty"))

cur.close()
ground_Water.close()

ground_water_df_sorted = ground_Water_df.sort_values(by=1, ascending=False)

plt.figure(figsize=(10, 8))
plt.bar(ground_water_df_sorted[0], ground_water_df_sorted[1], color='green')
plt.xlabel('Country')
plt.ylabel("지하수의 상태")
plt.title('[유럽 지하수 상태]')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# 국가별 GDP 
gdp = pymysql.connect(host = "172.20.145.44", user = "hwansun", password = "1234", db = "mini_project", charset = "utf8")

cur = gdp .cursor()
cur.execute("SELECT * FROM gdp_data")

rows = cur.fetchall()

gdp_df = pd.DataFrame(rows)
print(tabulate(gdp_df.head(), headers = "keys", tablefmt = "pretty"))

cur.close()
gdp.close()

gdp_df = gdp_df[gdp_df[5] != 'n/a']
gdp_df[5] = gdp_df[5].str.replace(',', '').astype(float)

gdp_df_sorted = gdp_df.sort_values(by=5, ascending=False)
top_10 = gdp_df_sorted.head(10)

bottom_10_gdp = gdp_df[gdp_df[[0]].isin(bottom_10[[0]])]
bottom_10_countries = bottom_10[0].values

gdp_df_sorted.isna().sum()

plt.figure(figsize=(10, 8))
plt.bar(top_10[0], top_10[5], color='yellow')
plt.xlabel('Country')
plt.ylabel("GDP")
plt.title('[전 세계 GDP]')
plt.xticks(rotation=45)
plt.legend()
plt.show()
