import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import re

file1 = r"C:\Hwan\공공데이터\DAY 03\age.csv"

def parse_distric_name(city) :
    city_name = re.split("[()]", city)
    return city_name[0]

def print_population(popluation) :

    for i in range(len(popluation)) :
        print(f"{i:3d}세 : {popluation[i]:4d}명", end =  " ")
        if (i + 1) % 10 == 0 :
            print()

def draw_population(city_name, population_list) :
    plt.title(f"{city_name} 인구 현황")
    plt.xlabel("나이")
    plt.ylabel("인구수")
    plt.bar(range(101), population_list)
    plt.xticks(range(0, 101, 10))
    plt.show()

def get_population(city) :
    f = open(file1, encoding="euc_kr")
    data = csv.reader(f)

    population_list = []
    full_distric_name = ""
    for row in data :
        if city in row[0] :
            full_distric_name = parse_distric_name(row[0])
            for data in row[3:] :
                data = data.replace(",", "")
                population_list.append(int(data))
            break
    f.close()
    print_population(population_list)
    draw_population(full_distric_name, population_list)

city = input("인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요 : ")
get_population(city)

city = "대구광역시"