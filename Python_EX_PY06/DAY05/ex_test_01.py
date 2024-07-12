# -----------------------------------------
# [실습 1] 글자를 입력 받음 ==> input() : 결과: str
#          입력 받은 글자(숫자 제외, 문자)의 코드값 출력
# -----------------------------------------
msg = input("문자를 입력하세요 (a~z, A~Z): ").strip()
# 문자 => 코드값 변환 내장함수 : ord(문자 1개)
if len(msg) > 0 :
    if len(msg) == 1 :
        if 'a' <= msg <= 'z' or 'A' <= msg <= 'Z' :
            print(f'{msg}의 코드값 : {ord(msg)}')
        else :
            print("대소문자 알파벳만 가능합니다.")
    else :
        print("1개의 문자만 입력하셔야 합니다.")
else :
    print(ord('입력된 데이터가 없습니다. 확인하세요.'))


if len(msg) == 1 :
    if 'a' <= msg <= 'z' or 'A' <= msg <= 'Z' :
        print(f'{msg}의 코드값 : {ord(msg)}')
    else :
        print("대소문자 알파벳만 가능합니다.")
else :
    print(ord('1개의 문자만 입력하셔야 합니다. 입력된 데이터가 없습니다. 확인하세요.'))

#   len(msg)에서 len(msg) 자체가 값이 있으면 True이므로 굳이 비교 연산을 쓸 필요가 없음 len(msg)라고 적어도 무방
if len(msg) == 1 and ('a' <= msg <= 'z' or 'A' <= msg <= 'Z') :
    print(f'{msg}의 코드값 : {ord(msg)}')
else :
    print('1개의 문자만 입력하셔야 합니다.\n입력된 데이터가 없습니다. 확인하세요.')

## 입력된 문자가 2개 이상인 경우
data = "Ab"
print(list(map(ord, data)))

# -----------------------------------------
# [실습 2] 점수를 입력 받은 후 학점 출력
#  - 학점: A+, A0, A-, B+, B0, B- C+, C0 C-, D(+, 0, -), F
#  - A+ :100~96, A0: 95, A-: 94 ~ 90 ....
# -----------------------------------------
jumsu = int(input('점수를 입력하세요 : '))

if jumsu <= 100 :
    if 96 <= jumsu < 100 :
        print('A+')
    elif jumsu == 95 :
        print('A0')
    elif 90 <= jumsu <= 94 :
        print('A-')
    elif 86 <= jumsu <= 89 :
        print('B+')
    elif jumsu == 85 :
        print('B0')
    elif 80 <= jumsu <= 84 :
        print('B-')
    elif 76 <= jumsu <= 79 :
        print('C+')
    elif jumsu == 75 :
        print('C0')
    elif 71 <= jumsu <= 74 :
        print('C-')
    elif 66 <= jumsu <= 69 :
        print('D+')
    elif jumsu == 65 :
        print('D0')
    elif 61 <= jumsu <= 64 :
        print('D-')
    else :
        print('F')
else :
    print('잘못된 점수')

jumsu = 75
grade = ''
if jumsu < 0 or jumsu > 100 :
    print(f'{jumsu}점은 잘못된 점수입니다.')
else :
    if jumsu > 95 : grade = 'A+'
    elif jumsu == 95 : grade = 'A0'
    elif jumsu >= 90 : grade = 'A-'
    elif jumsu >85 : grade = 'B+'
    elif jumsu == 85 : grade = 'B0'
    elif jumsu >= 80 : grade = 'B-'
    elif jumsu >75 : grade = 'C+'
    elif jumsu == 75 : grade = 'C0'
    elif jumsu >= 70 : grade = 'C-'
    elif jumsu > 65 : grade = 'D+'
    elif jumsu == 65 : grade = 'D0'
    elif jumsu >= 60 : grade = 'D-'
    else : grade = 'F'
    print(grade)