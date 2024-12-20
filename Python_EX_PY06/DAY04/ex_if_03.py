# --------------------------
# 충첩조건문
#  - 조건문 안에 조건문이 존재하는 제어문
#  - 형식
#    if 조건식:
#        실행코드
#        if 조건식 :
#            실행코드
#            실행코드
# --------------------------
# [실습] 숫자가 음이 아닌 정수와 음수 구분하기
#        음이 아닌 정수 중에 0과 양수 구분하기
# - 음이 아닌 정수 : 숫자 >= 0 
#   - 숫자 > 0
num = 8
# 중첩조건문
if num >= 0 :
    print(f'{num}은 음이 아닌 정수')
    if num > 0 :
        print(f'{num}은 양수')
    else :
        print(f'{num}은 0')
else :
    print(f'{num}은 음수')
# 다중조건문 
if num > 0 :
    print(f'{num}은 양수')
elif num < 0 :
    print(f'{num}은 음수')
else :
    print(f'{num}은 0')

# ------------------
# 동네이름 데이터에서 입력받은 동네이름 해당 여부
city = ['대구', '부산', '울산']
data = '마산'

if data == city[0] or data == city[1] or data == city[2] :
    print(f'{data}는 광역시입니다.')

if data in city :
    print(f'{data}는 광역시입니다.')
    