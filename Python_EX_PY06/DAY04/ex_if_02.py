# ---------------------------
# [실습] 숫자를 입력 받아서 음이 아닌 정수와 음수 구분핳기
# ---------------------------
num = int(input("숫자를 입력하세요 : "))

if num >= 0 :
    print(f'숫자 {num}은 음이 아닌 정수입니다.')
else :
    print(f'숫자 {num}은 음수입니다.')

# [실습] 점수를 입력 받아서 합격과 불합격 출력
#  - 합격: 60점 이상
score = int(input("점수를 입력하세요 : "))

if score >= 60 :
    print(f'축하드립니다. {score}점으로 합격입니다.')
else :
    print(f'{score}점으로 탈락입니다. {60-score}점이 부족하네요 ! ')

# [실습] 점수를 입력 받아서 학점 출력
#  - 학점: A, B, C, D
jumsu = int(input("점수를 입력하세요 : "))

if jumsu >= 90 :
    print("A학점입니다.")
elif jumsu >= 80 :
    print('B학점입니다.')
elif jumsu >= 70 :
    print('C학점입니다.')
elif jumsu >= 60 :
    print("D학점입니다.")
else :
    print('F학점입니다.')