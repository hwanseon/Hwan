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

file1 = r"C:\Hwan\공공데이터\DAY 01\daegu.csv"
file2 = "daegu-utf8.csv"

import csv
fin = open(file1, "r", encoding = "utf-8-sig")
data = csv.reader(fin, delimiter = ",")

fout = open(file2, "w", newline = "", encoding = "utf-8-sig")
wr = csv.writer(fout)

for row in data :
    for i in range(len(row)) :
        row[i] = row[i].replace('\t', "")
    print(row)
    wr.writerow(row)

fin.close()
fout.close()
print("파일 저장 완료")

f = open(file2, encoding = "utf-8-sig")
data = csv.reader(f, delimiter = ",")
header = next(data)
print(header)

i = 1
for row in data :
    print(row)
    if i >= 5 :
        break
    i += 1

f.close()

import csv

def get_minmax_temp(data) :

    header = next(data)

    min_temp = 100
    min_date = ''

    max_temp = -999
    max_date = ''

    for row in data :
        if row[3] == '' :
            row[3] = 100
        row[3] = float(row[3])

        if row[4] == '' :
            row[4] = -999
        row[4] = float(row[4])

        if row[3] < min_temp :
            min_temp = row[3]
            min_date = row[0]

        if row[4] > max_temp :
            max_temp = row[4]
            max_date = row[0]

print("-"*50)
print(F"대구 최저 기온 날씨 : {min_date}, 온도 : {min_temp} ")
print(f"대구 최고 기온 날씨 : {max_date}, 온도 : {max_temp}")

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open(file2)
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != "" :
        result.append(float(row[-1]))
f.close()

plt.figure(figsize = (10, 2))
plt.hist(result, bins = 500, color = "bule")

plt.rcParams["axes.unicode_minus"] = Falseplt.title("1907년부터 2024년까지 대구 기온 히스토그램")
plt.show()
