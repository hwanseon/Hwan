# ------------------------------------------------------------
# str data type 전용 함수 즉, 메서드 살펴보기
# ------------------------------------------------------------
# [문자열에서 좌우 여백 제거 메서드 -> strip(), lstrip(), rstrip()]
# 주의 : 문자열 내부 공백은 제거 X
msg = "Good Luck"
data = " Happy New Year 2025!         "

# 좌우 모든 공백 제거
m1 = msg.strip()
print(f'원복 msg : {len(msg)}개 -- 공백제거 m1 : {len(m1)}개')

d1 = data.strip()
print(f'원복 msg : {len(data)}개 -- 공백제거 m1 : {len(d1)}개')

# Left 즉, 문자열 시작 부분의 공백 제거 ==> lstrip()
d1 = data.lstrip()
print(f'원복 msg : {len(data)}개 -- 공백제거 m1 : {len(d1)}개')

# Right 즉, 문자열 끝 부분의 공백 제거 ==> rstrip()
d1 = data.lstrip()
print(f'원복 msg : {len(data)}개 -- 공백제거 m1 : {len(d1)}개')

## [실습] 이름을 입력 받아서 저장
name = input("name : ").strip()
if len(name)>0 :
    print(f'name : {name}')
else :
    print('Try Enter')

## [실습] 입력 받은 데이터를 따라 출력을 달리
## - input() 사용
## - [출력] 알파벳이면 ★, 숫자면 ♥, 나머지는 무시
data = input("Enter chr: ").strip()
# 입력값이 문자 1개
# if 'a' <= data <= 'z' or 'A' <= data <= 'Z' :
#     print("★")
# elif '0' <= data <= '9' :
#     print("♥")
# 입력값이 문자열
for d in data :
    if 'a' <= d <= 'z' or 'A' <= d <= 'Z' :
        print("★", end = '')
    elif '0' <= d <= '9' :
        print("♥", end = '')

import string

msg4 = ', python    .  '
print()
