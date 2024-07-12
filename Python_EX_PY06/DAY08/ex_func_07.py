# -----------------------------------
# 사용자 정의 함수
# -----------------------------------
# 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 각각 만들기
# - 매개변수 : 정수 2개, num1, num2
# - 함수결과 : 연산결과 반환 
# -----------------------------------

# [덧셈]
def plus(num1, num2) :
    return print(num1 + num2)

# [뺄셈]
def minus(num1, num2) :
    return print(num1 - num2)

# [곱셈]
def mult(num1, num2) :
    return print(num1 * num2)

# [나눗셈]
def div(num1, num2) :
    return print(num1 / num2 if num2 else '을 입력할 수 없습니다.')

# 함수 호출
plus(10,5)
minus(10,5)
mult(10,5)
div(10,5)
# [실습] 사용자로부터 연산자, 숫자1, 숫자2를 입력 받아서 연산결과 출력
# - input("연산자", 숫자1, 숫자2).split(',')

# -----------------------------------
# 함수 기능: 입력 데이터가 유효한 데이터인지 검사해주는 기능
# 함수 이름: check_data
# 매개변수: 문자열 데이터, 데이터 개수 data, count sep=' '
# 함수 결과: 유효 여부 True/Flase
# -----------------------------------
def check_data(data, count, sep=' ') :
    # data 여부
    if len(data) : 
        # data 분리 후 갯수 체크
        data2 = data.split(sep)
        return True if count == len(data2) else False
    else :
        return False
print(check_data('+ 10 3',3))

op, num1, num2 = input("연산자 1개와 슷자 2개를 입력하세요 ex) 연산자 숫자1 숫자 2 : ").split()

if op not in {'+', "-","/","*"} :
    print(f"{op}는 잘못된 연산자 입니다.")
else :
    if num1.isdecimal() and num2.isdecimal() :
        num1 = int(num1)
        num2 = int(num2)
        result = 0 
        if op == "+" : result = plus(num1, num2) 
        elif op == "-" : result = minus(num1, num2)
        elif op == "*" : result = mult(num1, num2)
        else: result = div(num1, num2)
        print(f'{num1}{op}{num2} = {result}')
    else :
        print("정수만 입력 가능합니다.")


