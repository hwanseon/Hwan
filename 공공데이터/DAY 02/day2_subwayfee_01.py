import csv

file1 = r"C:\Hwan\공공데이터\DAY 02\subwayfee.csv"

f = open(file1, encoding = "utf-8-sig")
data = csv.reader(f)
header = next(data)
print(header)
i = 1
for row in data :
    print(row)
    if i > 5 :
        break
    i += 1

f.close()