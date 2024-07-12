# --------------------------------------------------------------
# 제어문 - 반복문
# --------------------------------------------------------------
# [실습] 2 ~ 9단까지 구구단을 출력하세요
dan =2 
for n in range(1, 10) :
    print(f'{dan} * {n} = {dan * n}')

dan = 3
for n in range(1, 10) :
    print(f'{dan} * {n} = {dan * n}')

dan = 4 
for n in range(1, 10) :
    print(f'{dan} * {n} = {dan * n}')

## ==> 이렇게 적는건 비효율 적

for dan in range(2, 10) :
    print(f"<{dan:^3} 단 >")
    for n in range(1, 10) :
        if n % 3 :
            print(f'{dan:^3} * {n:^3} = {dan * n:^5}', end = "   ")
        elif n == 9 :
            print(f'{dan:^3} * {n:^3} = {dan * n:^5}')
            print('*'*60)
        else : print(f'{dan:^3} * {n:^3} = {dan * n:^5}')