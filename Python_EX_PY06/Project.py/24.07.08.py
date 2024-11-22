## 여행 일정 정리해주는 프로그램
# ---------------------------------------
# 함수기능 : 장소, 일정을 입력받아 일정을 추가하는 함수
# 함수이름: trip
# 매개변수 : trips
# 함수결과 : 없음
# ---------------------------------------
def trip(trips) :
    place = input("여행지 : ").strip()
    data = input("일정 ex) yyyy-mm-dd : ").strip()
    if check_data(data) : 
        if data not in trips :
            trips[data] = place
            print("일정이 추가되었습니다.")
        else :
            print("이미 입력된 일정입니다.")
    # else : 
    #     print("잘못된 날짜 형식입니다.\nyyyy-mm-dd 형식으로 입력하세요.")

# ---------------------------------------
# 함수기능 : 날짜의 문자열 길이 검사해주는 함수
# 함수이름: check_data
# 매개변수 : data
# 함수결과 : 없음
# ---------------------------------------
def check_data(data) :
    div = data.split("-")
    if len(div) != 3 :
        print("잘못된 날짜 형식입니다.\nyyyy-mm-dd 형식으로 입력하세요.")
        return False

    year, month, day = div

    if not year.isdecimal() and month.isdecimal() and day.isdecimal() :
        print("잘못된 날짜 형식입니다.\nyyyy-mm-dd 형식으로 입력하세요.")
        return False
    
    year = int(year) ; month = int(month) ; day = int(day)

    if year < 1000 or year > 2400 :
        print(f"{year}년은 입력할 수 없습니다.")
        return False
    
    if month < 1 or month > 12 :
        print(f"{month}월은 없는 달입니다.")
        return False
    if day < 1 or day > 31 :
        print(f"{day}일은 없는 날입니다.")
        return False
    
    if month in [4, 6, 9, 11] and day >30 :
        print(f"{month}월에는 {day}일이 없습니다.")
        return False
    
    if month == 2 :
        if year % 4 == 3 :
            day <= 29
            print("일정이 추가되었습니다.")
        else :
            day >= 29
            print(f"{year}년 {month}월에는 29일은 없습니다.")
            return False

    return True   

# ---------------------------------------
# 함수기능 : 저장된 일정이 있는 경우 확인해주는 함수
# 함수이름: print_trip
# 매개변수 : trips
# 함수결과 : 없음
# ---------------------------------------
def print_trip(trips) :
    if trips :
        print(f'\n{"일정":^12} | {"여행지":^12}')
        print('-'*30)
        for data in sorted(trips) :
            print(f'{data:^14} | {trips[data]:^14}')
    else :
        print("입력된 일정이 없습니다.")

# ---------------------------------------
# 함수기능 : 입력 프로그램 프레임 함수
# 함수이름: menu 
# 매개변수 : 없음
# 함수결과 : 없음
# ---------------------------------------
def print_menu () :
    print(f'{"*":*^30}')
    print(f'{"여행 일정 계획":^30}')
    print(f'{"*":*^30}')
    print(f'{"* 1 일  정  추  가 *":^29}')
    print(f'{"* 2 전체 일정 출력 *":>20}')
    print(f'{"* 3 종          료 *":^30}')
    print(f'{"*":*^30}')

# 여행지 입력 프로그램 -----------------------
# 사용자가 날짜와 장소를 입력 
# 날짜의 형식을 비교 후 저장
# ------------------------------------------
trips = {}

while True :
    
    print_menu()

    choice = input("메뉴 선택 : ")

    if choice.isdecimal() :
        choice = int(choice)
    else :
        print("0 ~ 9 사이 숫자만 입력하세요.")
        continue

    if choice == 3 :
        print("프로그램을 종료합니다.")
        break
    elif choice == 1:
        trip(trips)
    elif choice == 2 :
        print_trip(trips)
    else :
        print("선택된 메뉴는 없습니다. 0 ~ 9 사이 숫자만 입력하세요.")