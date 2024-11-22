# ----------------------------------------------------------------------
# 제어문 - 반복문과 break
#  - 중첩 반복문일 경우 break()는 가장 가까이 있는 반복문만 종료
# ----------------------------------------------------------------------
# [실습] 단의 숫자만큼만 구구단 출력 
# 2 * 1 = 2  2 * 2 = 4 
# 3 * 1 = 3  3 * 2 = 6  3 * 3 = 9
# 4 * 1 = 4  4 * 2 = 8  4 * 3 = 12  4 * 4 = 16

# 그냥 구구단 입력한 경우
for d in range(2, 10):
    print(f'\n[{d}단]', end = '   ')
    for n in range(1, 10) :
        print(f'{d} * {n} = {d*n:2}', end = ' ') #:2 자리수를 2칸하겠다는 의미 (기본이 오른쪽 정렬, :2>를 하지 않아도 됨)

print()

dan = int(input("출력 원하는 단 입력 : "))
isBreak = False                 # isBreak의 초기값도 중요

for d in range(2, 10):
    print(f'\n[{d}단]', end = '   ')
    for n in range(1, 10) :
        print(f'{d} * {n} = {d*n:2}', end = ' ')
        if n == d : break
    if d == dan : break

print()
print()
print("*"*30)
for d in range(2, dan+1) :
    print(f'\n[{d}단]', end = '   ')
    for n in range(1, d+1) :
        print(f'{d} * {n} = {d*n:2}', end = ' ')
        if n == d : break
    if d == dan : break
