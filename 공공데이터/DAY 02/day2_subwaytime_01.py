import csv

file1 = r"C:\Hwan\공공데이터\DAY 02\subwaytime.csv"

result = []
total_number = 0
with open(file1, encoding="utf-8-sig") as f :
    data = csv.reader(f)
    next(data)
    next(data) # 원본파일에 해더가 2줄이라서 2줄 건너뜀

    for row in data :
        row[4:] = map(int, row[4:])
        total_number += row[4]
        result.append(row[4])

print(f"총 지하철 역의 수 : {len(result)}")
print(f"새벽 4시 승차인원 : {total_number:,}명")

import matplotlib.pyplot as plt
import koreanize_matplotlib

with open(file1, encoding="utf-8-sig") as f :
    data = csv.reader(f)
    next(data)
    next(data)
    result = []
    total_number = 0
    max_num = -1
    max_station = ""

    for row in data :
        row[4:] = map(int, row[4:])
        total_number += row[4]
        result.append(row[4])
        if row[4] > max_num :
            max_num = row[4]
            max_station = row[3]

print(f"새벽 3시 총 승차 인원수 : {total_number:,}")
print(f'최대 승차역 : {max_station}, 인원수 : {max_num:,}')
result.sort()
plt.figure(dpi = 200)
plt.bar(range(len(result)), result)
plt.title("새벽 4시 지하철 승차인원 현황")
plt.show()