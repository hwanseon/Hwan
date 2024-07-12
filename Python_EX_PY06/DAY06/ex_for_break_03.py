# ----------------------------------------------------------------------
# 제어문 - 반복문과 break
#  - 중첩 반복문일 경우 break()는 가장 가까이 있는 반복문만 종료
# ----------------------------------------------------------------------
# [실습] 단의 숫자만큼만 구구단 출력 

# 중첩반복문 : 내부 반복문 종료시 외부 반복문 종료
## 내부 반복문 종료여부를 변수 저장
## 외분 반복문애소는 냐뷰 반복문이 종료되면 함께 종료

dan = int(input("출력 원하는 단 입력 : "))
isBreak = False                 # isBreak의 초기값도 중요

for d in range(2, 10):
    print(f'\n[{d}단]', end = '   ')
    for n in range(1, 10) :
        print(f'{d} * {n} = {d*n:2}', end = ' ')
        if n == d :
            isBreake = True
            break
    if isBreak : break

# for d in range(2, dan+1) :
#     print(f'\n[{d}단]', end = '   ')
#     for n in range(1, d+1) :
#         print(f'{d} * {n} = {d*n:2}', end = ' ')
