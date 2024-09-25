data = {"Seoul": ["South Korea", "Asia", 9655000],
        "Tokyo" : ["Japan", "Asia", 14110000],
        "Beijing" : ["China", "Asia", 21540000],
        "London" : ["United Kingdom", "Europe", 14800000],
        "Berlin" : ["Germany", "Europe", 3426000],
        "Mexico City" : ["Mexico", "America", 21200000]}

def print_menu () :
    print(f'{"-":-^50}')
    print(f'{"1. 전체 데이터 출력":<30}')
    print(f'{"2. 수도이름 오름차순 출력":<30}')
    print(f'{"3. 모든 도시의 인구수 내림차순 출력":<30}')
    print(f'{"4. 특정 도시의 정보 출력":<30}')
    print(f'{"5. 대륙별 인구수 계산 및 출력":<30}')
    print(f'{"6. 프로그램 종료":<30}')
    print(f'{"-":-^50}')

def menu_1 () :
    keys = list(data.keys())
    for i in range(len(data)):
        city = keys[i]
        info = data[city]
        print(f"[{i+1}] {city} : {info}")

def menu_2 () :
    sorted_keys = sorted(data.keys())
    for i in range(len(data)):
        city = sorted_keys[i]
        country, ground, population = data[city]
        print(f"[{i+1}] {city:<15} : {country:<15} {ground:<15} {population:<15,}")
          
def menu_3 ():
    sorted_data = sorted(data.items(), key=lambda item: item[1][2], reverse=True)    
    for i, (city, info) in enumerate(sorted_data, start=1):
        country, continent, population = info
        print(f"[{i}] {city:<15} : {population:<15,}")    

def menu_4():
    information = input("출력할 도시 이름을 입력하세요: ")

    if information in data:
        country, continent, population = data[information]
        print(f"{information}에 대한 정보:")
        print(f"국가: {country}, 대륙: {continent}, 인구수: {population:,}")
    else:
        print(f"도시 이름: {information}는 key에 없습니다.")


def menu_5 () :
    ground = input("대륙 이름을 입력하세요 (Asia, Europe, America) : ")
    total_population = 0
    for city, info in data.items():
        country, continent, population = info
        if continent == ground:
            print(f"{city}: {population:,}")
            total_population += population
    if continent != ground:
        print(f"{ground}라는 대륙은 없습니다. 입력값을 다시 확인해주세요.")

    
    else :
        print(f"\n{ground} 전체 인구수: {total_population:,}")


while True :
    print_menu()

    choice = int(input("메뉴를 입력하세요 : "))

    if choice == 1 :
        menu_1()
    elif choice == 2 :
        menu_2()
    elif choice == 3 :
        menu_3()
    elif choice == 4 :
        menu_4()
    elif choice == 5 :
        menu_5()
    elif choice == 6 :
        print("프로그램을 종료합니다.")
        break
    else :
        print("1 ~ 6 사이의 숫자를 입력하세요.")