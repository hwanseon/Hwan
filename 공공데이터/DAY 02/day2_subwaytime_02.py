import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

file1 = r"C:\Hwan\공공데이터\DAY 02\subwaytime.csv"

with open(file1, encoding="utf-8-sig") as f :
    data = csv.reader(f)
    next(data)
    next(data)

    station_list = []
    max_num = -1
    max_station = ""

    for row in data :
        row[4:] = map(int, row[4:])
        passenger_num = sum(row[10:15:2])

        station_name = row[3] + '('+ row[1] + ')'
        station_list.append((station_name, passenger_num))


sorted_passenger_list = sorted(station_list, key=lambda x:x[1], reverse = True)

index = 1
for station in sorted_passenger_list[:10] :
    print(f"[{index}]: {station[0]} {station[1]:,}")

station_name, station_passenger = zip(*sorted_passenger_list[:10])

plt.figure(figsize = (8, 6))

plt.title("출근 시간대 승차 인원이 가장 많은 10개 역", size = 16)
plt.bar(range(len(station_passenger)), station_passenger)

plt.xticks(range(len(station_name)), station_name, rotation = 70, fontsize = 8)
plt.ylabel("승차인원수")
plt.tight_layout()

plt.show()

with open(file1, encoding= "utf-8-sig") as f :
    data = csv.reader(f)
    next(data)
    next(data)
    max = [0] * 23
    max_station = [""]*23
    xticks_list = []

    for i in range(4, 27) :
        n = i % 24
        xticks_list.append(str(n))
    
    for row in data :
        row[4:] = map(int, row[4:])
        for j in range(23) :
            a = row[j*2 + 4]
            if a > max[j]:
                max[j] = a
                max_station[j] = xticks_list[j] + "시:" + row[3]

    for i in range(len(max)) :
        print(f"[{max_station[i]}] : {max[i]:,}")
plt.figure(figsize = (10, 10))
plt.title("시간대별 최대 승차역 정보")
plt.bar(range(23), max)
plt.xticks(range(23), labels = max_station, rotation = 80)
plt.tight_layout()
plt.show()