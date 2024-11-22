import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

file1 = r"C:\Hwan\공공데이터\DAY 02\subwaytime.csv"

with open(file1, encoding="utf-8-sig") as f :
    data = csv.reader(f)
    next(data)
    next(data)
    subway_in = [0] * 24
    subway_out = [0] * 24

    for row in data :
        row[4:] = map(int, row[4:])
        for  i in range(24) :
            subway_in += row[4+i*2]
            subway_out += row[5+i*2]
    
xticks_list = []
for i in range(4, 28) :
    n = i % 24
    xticks_list.append(str(n))

plt.figure(dpi = 100)
plt.title("지하철 시간대별 승하차 인원 추이", size = 16)
plt.grid(linestyle =":") # 그리드 라인 표시
plt.plot(subway_in, label = "승차")
plt.plot(subway_out, label = "하차")
plt.legend()

plt.xticks(range(24), labels=xticks_list)
plt.xlabel("시간")
plt.ylabel("인원 (천만명)")
plt.show()