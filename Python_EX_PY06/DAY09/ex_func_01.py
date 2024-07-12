# ---------------------------------------
# 함수(Function) 이해 및 활용
# ---------------------------------------
# 함수기능 : 3개의 정수를 덧셈 후 결과를 반환하는 함수
# 함수이름 : add3
# 매개변수 : num1. num2, num3
# 함수결과 : 정수 result
# ---------------------------------------
def add3(num1, num2, num3) :
    result = num1 + num2 + num3
    return result  # return은 나를 호출한 함수에게로 감

# ---------------------------------------
# 함수기능 : 3개의 정수를 곱셈 후 결과를 반환하는 함수
# 함수이름 : multi3
# 매개변수 : num1. num2, num3
# 함수결과 : 정수 result
# ---------------------------------------
def multi(num1, num2, num3) :
    result = num1 * num2 * num3
    return result

# ---------------------------------------
# 함수기능 : 3개의 정수를 나눗셈 후 결과를 출력하는 함수
# 함수이름 : div
# 매개변수 : num1. num2
# 함수결과 : NOne (반환값이 없으면 => None)
# ---------------------------------------
def div(num1, num2) :
    result = num1/num2
    if not num2 : 
        result = "0으로 나눌 수 없음"
    else : 
        result = num1/num2
    print(f'{num1} / {num2} = {result}')

    ## 함수 사용하기 즉, 호출
    # 덧셈
    value = add3(1, 2, 3) # 변수에 저장을 해야 출력 가능 print는 none 이라서 

    # 나눗셈
    value1 = div(3,  4)
    print(value1)

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

## 계산기 프로그램 ----------------------------
# - 사용자가 종료를 원할 때 종료 => 'x' or 'X' 입력 시 
# - 계산 연산방식과 숫자 데이터 입력 
while True :
    # (1) 입력 받기
    req = input("연산(+, -, *, /) 방식과 정수 2개 입력 ex) + 10 2 : ")
    # (2) 종료 조건 검사
    if req =='x' or req == "X" :
        print("계산기를 종료합니다.")
        break

    # (3) 입력에대한 연산방식과 data 추출  '+ 10 2'
    op, num1, num2 = req.split() # ['+', '10', '2']
    # str 정수 ==> int 변환
    num1 = int(num1)
    num2 = int(num2)
    # 연산에 따른 계산 진행
    if op == "+" :
       print(f'{num1} + {num2} = {add(num1, num2)}')
    elif op == '-' :
       print(f'{num1} - {num2} = {minus(num1, num2)}')
    elif op == "*" :
       print(f'{num1} * {num2} = {mult(num1, num2)}')
    elif op == "/" :
       print(f'{num1} / {num2} = {div(num1, num2)}')
    else : print(f"{op}는 지원되지 않는 연산자입니다.")

        
