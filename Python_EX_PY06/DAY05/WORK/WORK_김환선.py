# for, range 사용하기 p 185
for i in range(100) :
    print('Hello world ! ')
for i in range(100) :
    print('Hello world ! ', i)

for i in range(5, 12) :
    print('Hello world ! ', i)

for i in range(0, 10, 2) :
    print('Hello world ! ', i)

for i in range(10, 0, -1) :  # 숫자 감소
    print('Hello world ! ', i)

# reversed를 이용하면 숫자의 순서를 반대로 뒤집을 수 있음
for i in reversed(range(10)) : # 9 ~ 0까지 
    print('Hello world ! ', i)

## 반복문의 변수 변경
for i in range(10) :
    print(i, end = ' ')
    i = 10 # 반복문의 변수를 i로 변경
print()

# 입력한 횟수대로 반복하기 p 190
# count = int (input("반복할 횟수를 입력하세요 : "))

# for i in range(count) :
#     print('Hello world ! ', i)

# 시퀀스 객체로 반복하기 p191
a= [10, 20, 30, 40, 50]
for i in a :
    print(i)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits :
    print(fruit)

for letter in 'Python' :
    print(letter, end = " ")
print()
for letter in reversed('Python') :
    print(letter, end = " ")
print()

## 구구단 출력하기 p 193
gugudan = int(input())

for gu in range(1, 10) :
    print(f'{gugudan:^3} * {gu:^3} = {gugudan * gu:^5}')