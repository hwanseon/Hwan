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
 
print(print_menu)

# ---------------------------------------
# 함수기능 : 연산을 수행 후 결과를 반환하는 함수
# 함수이름: calc
# 매개변수 : 함수명, 숫자(str 타입) 2개
# 함수결과 : 없음
# ---------------------------------------
def calc(func, num1, num2, op) :
    num1 = int(num1) ; num2 = int(num2)
    print(f'결과 : {num1}{op}{num2} = {func(num1, num2)}')
    

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
        num1, num2 = input("정수 2개 ex) 10 2 : ").split()
        calc(add, num1, num2, "+")
   elif choice == 2 :
        num1, num2 = input("정수 2개 ex) 10 2 : ").split()
        calc(minus, num1, num2, "-")
   elif choice == 3 :
        num1, num2 = input("정수 2개 ex) 10 2 : ").split()
        calc(mult, num1, num2, "*")
   elif choice == 4 :
        num1, num2 = input("정수 2개 ex) 10 2 : ").split()
        calc(div, num1, num2, "/")
   else : 
       print("선택된 메뉴는 없습니다.")