import csv


f = open("C:\Hwan\공공데이터\DAY 01\daegu.csv", "r", encoding = "utf-8")
data = csv.reader(f)
count = 0
for row in data :
    if count > 5 :
        break
    else :
        print(row)
    count += 1

f.close()
