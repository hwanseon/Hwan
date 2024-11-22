## 구구단 전체 출력 => for문 1개로 : 몫, 나머지 연산자

for i in range(82) :
    dan = ( i // 9 ) + 2 
    gugudan = ( i % 9 ) + 1
    if  dan <= 9 :
        if gugudan == 9 :
            print(f'{dan:^3} * {gugudan:^3} = {dan * gugudan:^3}')
        elif gugudan == 1 :
            print(f'[{dan}단]', f'{dan:^3} * {gugudan:^3} = {dan * gugudan:^3}', end = '  ')
        else:
            print(f'{dan:^3} * {gugudan:^3} = {dan * gugudan:^3}', end = '   ')
    else : 
        break

print()    
## [출력]
## 2단, 3단, 4단, 5단
## 6단, 7단, 8단, 9단 
for gugudan in range(1, 10) :
    for dan in range(2, 6):
        if dan == 5  :
            print(f'{dan:^3} * {gugudan:^3} = {dan * gugudan:^3}', end = '\t')
            print()
        else : 
            print(f'{dan:^3} * {gugudan:^3} = {dan * gugudan:^3}', end = '\t')

print()

for gugudan in range(1, 10) :
    for dan in range(6, 10):
        if dan == 9  :
            print(f'{dan:^3} * {gugudan:^3} = {dan * gugudan:^3}', end = '\t')
            print()
        else : 
            print(f'{dan:^3} * {gugudan:^3} = {dan * gugudan:^3}', end = '\t')

# for num in range(20) :
#     d, n = num // 10, num % 10
#     for dan in range(2+(d*4), 6+(d*4)) :