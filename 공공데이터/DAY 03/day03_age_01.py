import csv

file1 = r"C:\Hwan\공공데이터\DAY 03\age.csv"

f = open(file1, encoding= "euc_kr")
data = csv.reader(f)

header = next(data)

for row in data :
    if "산격3동" in row[0] :
        print(row)

f.close()

result = []

# for row in data :
#     if "산격3동" in row[0] :
#         for data in row[3:] :
#             result.append(data)

# print(result)
# f.close()

import matplotlib.pyplot as plt
import re
import koreanize_matplotlib

f = open(file1, encoding= "euc_kr")
data = csv.reader(f)

city = ""
for row in data :
    if "산격3" in row[0] :
        str_list = re.split("[()]", row[0]) # split에 여러개의 문자를 추가하고 싶을때 [] 그룹을 지어주면 됨
        city = str_list[0]                  # [] 안에 있는 문자는 순서 상관없이 문자열에서 분리
        for data in row[3:] :
            data = data.replace(",", "")
            result.append(int(data))

f.close()
print(result)

plt.title(f"{city} 인구현황")
plt.xlabel("나이")
plt.ylabel("인구수")
plt.plot(result)
plt.show()