# -----------------------------------------
# 제어문 - while 반복문
# -----------------------------------------
# [실습] 3단 출력하기 단, while문 사용 
dan = 3 
gugudan = 1

while gugudan < 10 :
    print(f"{dan:^3} * {gugudan:^3} = {dan * gugudan:^3}")
    gugudan = gugudan + 1

## [실습] 1 ~ 30 범위의 숫 중에서 홀수만 출력, while문 사용
## [1] 1) 1 ~ 30 숫자 while문으로 출력
num = 1
while num <= 30 :
    print(num, end = "  ")
    num = num + 1
print()
##     2) 홀수 출력
num = 1
while num <= 30 :
    if num % 2 : print(num, end = "  ")
    num = num + 1
print()
## [2] 
num = 1
while num <= 30 :
    print(num, end = "  ")
    num = num + 2

## 반복문
# for  in : 원소 읽을 때 접합 
# while   : 반복의 횟수가 많을 때 사용 