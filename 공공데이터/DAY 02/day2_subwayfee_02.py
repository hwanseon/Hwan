import csv

file1 = r"C:\Hwan\공공데이터\DAY 02\subwayfee.csv"

f = open(file1, encoding = "utf-8-sig")
data = csv.reader(f)
header = next(data)
max_rate = 0
rate = 0

##  분모에 0이 들어가서 에러가 남
# for row in data :
#     for i in range(4, 8) :
#         row[i] = int(row[i])
#     rate = row[4] / row[6]
#     if rate > max_rate :
#         max_rate = rate
# print(max_rate)
# f.close()

## 무임승차 인원이 0인 역 찾기
# for row in data :
#     for i in range(4, 8) :
#         row[i] = int(row[i])
#     rate = row[4] / (row[4] + row[6]) # rate = (유임 승차 인원) / (전체탑승인원 = 유임승차인원 + 무임승차인원)

#     if row[6] == 0 :
#         print(row)
        
# f.close()

## 유동인구가 10만명 이상인 최대 유임 승차 인원이 있는 역
# max_rate = []
max_total_num = 0

for row in data :
    for i in range(4, 8) :
        row [i] = int(row[i])
    total_count = row[4] + row[6]

    if row[6] != 0 and total_count > 100000 :
        rate = row[4] / total_count
        if rate > max_rate :
            max_rate = rate
            max_row = row
            max_total_num = total_count
            print(f"역이름 : {max_row[3]}, 전체 인원 : {max_total_num:,}명,"
                f"유임승차인원 : {max_row[4]:,}명, "
                f"유임승차 비율 : {round(max_rate * 100, 1):,}%")
print("-"*80)
print("최대 유임 승차역")
print(f"역이름 : {max_row[3]}, 전체인원 : {max_total_num:,}명, "
    f"유임승차인원 : {max_row[4]:,}명, "
    f"유임승차 비율 : {round(max_rate * 100, 1):,}%")
            
f.close()