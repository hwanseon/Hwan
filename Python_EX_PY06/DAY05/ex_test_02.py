# ---------------------------------------
# ==> 1줄로 조건식을 축약: 조건부 표현식
# ---------------------------------------
## [실습] 임의의 숫자가 5의 배수 여부 결과 출력
num = int(input('숫자를 입력하세요 : '))

print('5의 배수가 아닙니다.') if num % 5 else print('5의 배수입니다.')

## [실습] 문자열을 입력 받아서 문자열의 원소 개수를 저장 
##        단, 원소 개수가 0이면 None 저장
##        1) 입력받기 input(), 2) 원소/요소 개수 파악 len()
##        3) 원소/요소 개수 저장 단, 0인 경우 None 저장

num = input("문자열을 입력하세요 : ")
result = None

result = len(num) if len(num) else result
print(result)

## [실습 3] 연산자(4칙연산자: +, - , *, /)와 숫자 2개 입력 받기
##  - 입력된 연산자에 따라 계산 결과 저장 
##  - ex) + 10 3 => 13
data = input("연산자와 숫자 2개 입력 ex) + 10 3 : ").split()
yeon, num1, num2 = data[0], int(data[1]), int(data[2])

if yeon == '+' : result = (f'{num1} {yeon} {num2} = {num1 + num2}')
elif yeon == '-' : result = (f'{num1} {yeon} {num2} = {num1 - num2}')
elif yeon == '*' : result = (f'{num1} {yeon} {num2} = {num1 * num2}')
elif yeon == '/' : result = (f'{num1} {yeon} {num2} = {num1 / num2}')
else : print("4칙 연산자가 아닙니다.")
print(result)