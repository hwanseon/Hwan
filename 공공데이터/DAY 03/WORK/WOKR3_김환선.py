import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import re
import pandas as pd

file1 = r"C:\Hwan\공공데이터\DAY 03\gender.csv"

label_list = ["남성", "여성"]
daegu_list = ["대구광역시 중구", "대구광역시 동구", "대구광역시 서구", "대구광역시 남구", "대구광역시 북구", "대구광역시 수성구", "대구광역시 달서구", "대구광역시 달성군", "대구광역시 군위군"]

f = open(file1, encoding="euc_kr")
data = csv.reader(f)
all_male_count = []
all_female_count = []
city = "대구광역시"
male_count = 0
female_count = 0

for row in data :
    if city in row[0] :
        male_count = int(row[104].replace(",", ""))
        female_count = int(row[207].replace(",", ""))
        all_male_count = all_male_count.append(male_count)
        all_female_count = all_female_count.append(female_count)
        break

print(f"{city} : (남:{male_count:,} 여: {female_count:,})")

gu_male_count = []
gu_female_count = []

for daegu in daegu_list :
    for row in data :
        if daegu in row[0] :
            male_count = int(row[104].replace(",", ""))
            female_count = int(row[207].replace(",", ""))
            gu_male_count.append(male_count)
            gu_female_count.append(female_count)
        break
        
    print(f"{daegu} : (남:{male_count:,} 여: {female_count:,})")


fig, axs = plt.subplots(5, 2, figsize=(12, 20))

axs = axs.flatten()
axs[9] = plt.pie([male_count, female_count], labels=label_list, autopct="%.1f%%", startangle=90, colors=plt.cm.Paired.colors)
axs[9] = plt.title("대구광역시")
for i, daegu in enumerate(daegu_list):
    axs[i].pie([gu_male_count[i], gu_female_count[i]], labels=label_list, autopct="%.1f%%", startangle=90, colors=plt.cm.Paired.colors)
    axs[i].set_title(daegu)

plt.suptitle("대구광역시 구별 남녀 인구 비율", fontsize=16)
plt.tight_layout()
plt.show()
