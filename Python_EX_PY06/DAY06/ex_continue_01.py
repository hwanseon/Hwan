# ------------------------------------------
# 반복문과 continue
#  - continue 구문을 만나면 구문 아래 코드 실행 x
#  - 반복문으로 가서 다음 요소 데이터를 가지고 진행 
# ------------------------------------------
## [실습] 1 ~ 50까지 숫자로 구성된 data
## 3의 배수인 경우만 화면에 출력 
data = list(range(1, 51))

for d in data :
    if d % 3 == 0 :
        print(d)

# continue 사용
for d in data :
    if d % 3 : continue
    print(d)