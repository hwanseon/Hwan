# ----------------------------------------------------
### 전역변수 (Global Variable) :파이선 파일 안에 존재하는 변수
##  - 모든 곳에서 사용가능
##  - 프로그램 실행 시 메모리에 존재
##  - 프로그램 종료 시 메모리에서 삭제
# ----------------------------------------------------
total = 100 # 전역변수 예시

# ----------------------------------------------------
### 함수 기능 : (여러개)정수를 덧셈한 후 결과를 반환하는 함수
# 함수이름 : addInt
# 매개변수 : 0 ~ n개 ==> 가변인자 *nums
# 함수결과: 정수 result
# ----------------------------------------------------
def addInt(*nums) :
    total = 0
    for n in nums :
        total += n
    return total

def multiInt(*nums) :
    total1 = 1
    for n in nums :
        total1 *= n
    return total1 + total # 값을 바꾸지 않기 때문에 global total 이라 안해도 됨


def multiInt2(*nums) :
    # 전역변수의 값을 변경할 경우 => 그냥 사용 X
    global total # 이렇게 값을 변경한다고 알려줘야함
    for n in nums :
        total *= n
    return total

# 함수호출
result1 = addInt(1)
print(f'result : {result1}')

result2 = multiInt(5)
print(f'result2 : {result2}')

print(f'전 : total =>  {total}')
result2 = multiInt2(5)
print(f'result2 : {result2}')
print(f'후 : total =>  {total}')