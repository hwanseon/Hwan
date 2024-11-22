# -------------------------------------------------
# 모듈 : 변수, 함수, 클래스가 들어있는 파이썬 파일
# 패키지 : 동일한 목적의 모듈들을 모은 것
#         패키지 안에는 여러개의 모듈 파일들이 존재
# 모듈 사용법 : import 모듈 파일명 (확장자 제외)
# -------------------------------------------------
import random as rad # as = ~ 줄여서 쓴다

# 임의의 숫자 생성 후 추출
# 임의의 숫자 10개 생성
# -> random() : 0.0 <= ~ < 1.0
# for cnt in range(10) :
#     print(rad.random()) 

# -> randint(a,b) : a <= ~ <= b
# for cnt in range(10) :
#     print(rad.randint(0,1))

## ---------------------------------------------
## [실습] 로또 프로그램을 만들어라
#         - 1 ~ 45 범위에서 중복되지 않는 6개 추출
## ---------------------------------------------
# 반복횟수 : 알수없음 ==> 무한반복문
# 종료조건 : 중복 안되는 6개의 숫자 => list, set, dict
lotto = [0,0,0,0,0,0]
idx = 0

while True :
    lo = rad.randint(1, 45)
    if lo not in lotto : 
        lotto[idx] = lo
        idx = idx + 1
    if idx == 6 :
        break

print(lotto)

lotto = {}
key = 0

while len(lotto) <= 6 :
   num = rad.randint(1, 45)
   if num not in lotto.values() : 
        lotto[key] = num
        key = key + 1
        
print(lotto.values())

###########################################

lotto = set()
key = 1
while len(lotto) <= 6 :
   num = rad.randint(1, 45)
   num_set=set([num])
   lotto = lotto.union(num_set)
  
print(lotto)

# set 타입의 add() 메서드 추가 : 원소 추가, 중복 시 추가 X
lotto = set()
while len(lotto) < 6 :
    num = rad.randint(1, 45)
    lotto.add(num)

print(lotto)