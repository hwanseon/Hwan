## while 반복문으로 Hello, world! 100번 출력하기 p195
i = 0
while i <= 100 :
    print('Hello, World!')
    i += 1 
# 초기값 = 1
# i = 1
# while i <= 100 :
#     print('Hello, World!')
#     i += 1 
# # 초기값 감소
# i = 100
# while i >0 :
#     print('Hello, World!', i)
#     i -= 1 

# count = int(input("반복할 횟수를 입력하세요 : "))

# i = 0
# while i < count :
#     print('Hello, World!', i)
#     i += 1 

# count = int(input("반복할 횟수를 입력하세요 : ")) # count 감소
# while count > 0 :
#     print('Hello, World!', i)
#     count -= 1

# import 모듈 호출 
import random 

print(random.randint(1, 6))
print(random.randint(1, 6))
print(random.randint(1, 6))

i = 0 
while i != 3 :
    i = random.randint(1, 6)
    print(i)

# while문으로 무한루프 생성
# while True : # 0이 아닌 숫자 or 내용이 있는 문자열은 True로 취급하여 무한 루프
#     print('안녕')

## 교통카드 잔액 출력 p203
# money = int(input()) - 1350

# while money >= 0 :
#     print(money)
#     money -= 1350
#     if money < 0 :
#         break

## beark, continue로 반복문 제어하기 p204
i = 0
while True :
    print(i)
    i += 1
    if i == 100 :
        break

for i in range(10000) :
    print(i)
    if i == 100 :
        break
for i in range(100) :
    if i % 2 == 0 :
        continue
    print(i, end = '  ') # 홀수 출력

i = 0 
while i < 100 :
    i += 1
    if i % 2 == 0 :
        continue
    print(i)   # 홀수출력 

### 반복문(for, while)의 반복할 코드에서 아무 일도 하지 않지만, 
### 반복문의 형태유지를 하고 싶으면 pass()
# count = int(input("반복할 횟수 입력 : "))
# # i = 0 
# # while True :
# #     print(i)
# #     i += 1
# #     if i == count ::
# #     break
# for i in range(count+1) :
#     if i % 2 == 0 :
#         continue
#     print(i)

### 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력 p 212
# start, stop = map(int, input().split())

# i = start

# while True :
#     if i % 10 == 3 :
#         i += 1
#         continue
#     elif i > stop :
#         break
#     print(i, end = ' ')
#     i += 1

## 계단식으로 별 출력하기 p213
for i in range(5) :
    for j in range(5) :
        print('j :', j, sep ="", end = ' ')
    print("i:", i, '\\n', sep='')

# 사각형으로 별 출력 p214
for i in range(5):
    for j in range(5) :
        print('*', end = ' ')
    print()

for i in range(3) :
    for j in range(7) :
        print("*", end = "")
    print()

## 계단식 별 출력하기 p 216
for i in range(5) :
    for j in range(5) :
        if i >= j :  # 별의 개수는 세로방향인 줄의 위치에 비례
            print( "*", end = '')
    print() 

## 대각선으로 별출력
## ===========> 그냥 세로 일자로 출력됨
for i in range(5) :
    for j in range(5) :
        if j == i : # 기로 방향 변수와 세로 방향 변수가 같을 떄
            print("*", end = '')
    print()

### ======> 대각선 출력
for i in range (5):
    for j in range(5) :
        if i == j : # 기로 방향 변수와 세로 방향 변수가 같지 않을 떄 공백 출력
            print("*", end = '')
        else :
            print(' ', end = '')
    print()

# 산모양으로 별 출력하기 p219
# heigh = int(input())

# for h in range(heigh) :
#     for g in range(heigh) :
#         if h > g  :
#             print("*", end = '')
#         else :
#             print(" ", end = '')
#     print()

# FizzBuzz 문제
# 1 ~ 100까지 숫자를 출력 중에 3의 배수는 Fizzz, 5의 배수는 Buzz
# 3, 5의 공배수는 FizzBuzz 출력

for n in range(1, 101) :
    if n % 3 == 0 :
        print('Fizz')
    elif n % 5 == 0 :
        print('Buzz')
    elif n % 3 == 0 and n % 5 == 0 :
        print('FizzBuzz')
    else :
        print(n)

# 위의 코드는 n = 30 일때 fizz를 찍고 넘어감 
# ==> 그렇기 때문에 공배수 확인 문자를 젤 첫줄에 적어줘야함
for n in range(1,101) :
    if n % 3 == 0 and n % 5 == 0 : # 논리연산자를 사용하지 않으면 n % 15
        print('FizzBuzz')
    elif n % 3 == 0 :
        print('Fizz')
    elif n % 5 == 0 :
        print('Buzz')
    print(n)

# 코드 단축하기 p223
for i in range(1, 101) :
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
# 위의 코드랑 똑같은 것

# 5와 7의 배수, 공배수 처리하기 p226
start, stop = map(int, input().split())
i = start 

while True :
    if i % 5 == 0 and i % 7 == 0 :
        print('FizzBuzz')
        i += 1
        continue
    elif i % 5 == 0 :
        print("Fizz")
        i += 1
        continue
    elif i % 7 == 0 :
        print('Buzz')
        i += 1
        continue
    elif i > stop :
        break
    print(i)
    i += 1