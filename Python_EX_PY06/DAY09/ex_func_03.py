# ---------------------------------------
# 함수(Function) 이해 및 활용
# ---------------------------------------
# 함수(Function) 이해 및 활용
# - 4칙 연산 기능별 함수 생성 => 덧셈, 뺄셈, 곱셈, 나눗셈
# - 2개 정수만 계산
# ---------------------------------------
def add (num1, num2) :
    return num1 + num2

def minus (num1, num2) :
    return num1 - num2

def mult (num1, num2) :
    return num1 * num2

def div(num1, num2) :
    result = num1/num2
    if not num2 : 
        result = "0으로 나눌 수 없음"
    else : 
        result = num1/num2
    print(f'{num1} / {num2} = {result}')

# ---------------------------------------
# 메뉴 출력 함수
# 함수기능 : 계산기 메뉴를 출력하는 함수
# 함수이름: print_menu
# 매개변수 : 없음
# 함수결과 : 없음
# ---------------------------------------
def print_menu () : # 함수를 만들 때 매개변수가 없어도 () 작성
    print(f'{"*":*^16}') # 16자리를 "*"로 중간정렬 하는데 나머지는 공백, 공백을 채우려고 * 입력
    print(f'{"계 산 기":^16}')
    print(f'{"*":*^16}')
    print(f'{"* 1 덧    셈 *":16}')
    print(f'{"* 2 뺄    셈 *":16}')
    print(f'{"* 3 곱    셈 *":16}')
    print(f'{"* 4 나 눗 셈 *":16}')
    print(f'{"* 5 종    료 *":16}')
    print(f'{"*":*^16}')

# ---------------------------------------
# 함수기능 : 연산을 수행 후 결과를 반환하는 함수
# 함수이름: calc
# 매개변수 : 함수명, 숫자(str 타입) 2개
# 함수결과 : 없음
# ---------------------------------------
def calc(func, op) :
    data = input("정수 2개 입력 ex) 10 2 : ")
    if check_data(data, 2) :
        data = data.split()
        print(f'결과 : {data[0]}{op}{data[1]} = {func(int(data[0]), int(data[1]))}')
    else :
        print(f"{data} : 올바른 data가 아님 !")
# ---------------------------------------
# 함수기능 : 입력 받은 데이터가 유효한 데이터인지 검사하는 함수
# 함수이름: check_data
# 매개변수 : str data(ex) '10 3'), data 수
# 함수결과 : True or False
# ---------------------------------------
def check_data (data, count) :
    # 입력된 str == > list로 형변환 : split()
    data = data.split()
    # 개수 체크
    if len(data) == count :
        # 0~9로 구성된 str인지 체크 
        if data[0].isdecimal() and data[1].isdecimal( ) :
            isOk = True
            for d in data :
                if not d.isdecimal() :
                    isOk = False
                    break
            return isOk
    else : 
        return False

## 계산기 프로그램 ----------------------------
# - 사용자에게 연산방식을 선택하는 메뉴를 출력
# - 종료 메뉴 선택 시 프로그램 종료
# ==> 무한반복 : while 사용 
#  ---------------------------------------
while True :
   # 메뉴 출력 
   print_menu()

   # 메뉴 선택 요청
   choice = input("메뉴 선택 : ")
   if input("메뉴 선택 : ").isdecimal() :
       choice  = int(choice)
   else :
       print("0 ~ 9 사이 숫자만 입력하세요.")
       continue
   # 종료조건(5번 메뉴 선택) 처리
   if choice == 5 :
       print("프로그램을 종료합니다.")
       break
   elif choice == 1 :
        calc(add, "+")
   elif choice == 2 :
        calc(minus, "-")
   elif choice == 3 :
        calc(mult, "*")
   elif choice == 4 :
        calc(div, "/")
   else : 
       print("선택된 메뉴는 없습니다.")