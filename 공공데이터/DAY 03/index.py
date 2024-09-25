# age, csv 파일 index 계산

import csv

file1 = r"C:\Hwan\공공데이터\DAY 03\age.csv"
file2 = r"C:\Hwan\공공데이터\DAY 03\gender.csv"

def get_index_of_age_csv() :
    f = open(file1, encoding= "euc_kr")
    data = csv.reader(f)
    header = next(data)

    print("-----------------------------")
    print(" age.csv index")
    print("-----------------------------")
    for i in range(len(header)) :
        print(f"[{i:3}] : {header[i]}") # {i:3} : 3자리 공간의 i 값 출력

    f.close()

get_index_of_age_csv()

f= open(file2, encoding="euc_kr")
data = csv.reader(f)
header = next(data)

for i in range(len(header)) :
    print(f"[{i:3d}] : {header[i]}", end = ", ")

    if (i+1) % 5 == 0 :
        print()

f.close()