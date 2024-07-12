# ----------------------------
# 내장함수 range()
#  - 숫자 범위를 생성하는 내장함수
#  - 형식: range(시작숫자, 끝숫자 +1, 간격)
#          range(끝숫자 + 1) 
# ----------------------------
# [실습 1] 1~100까지의 숫자를 저장하세용
nums = range(1, 101)

print(f'nums 값 : {nums}\n타입 : {type(nums)}\n개수 : {len(nums)}')

# 요소/원소 읽기 => 인덱싱
print(nums[0], nums[-1])

# 원소/요소 여러개 읽기 => 슬라이싱 
print(nums[0:10], nums[30:41])\
# 요소/원소 하나하나를 보기 => list/tuple 형변환
print(list(nums[0:10]), tuple(nums[30:41]))

# [실습 2] 1~100에서 3의 배수만 저장
# => 3, 6, 9 ,12 ............., 99
# three = [3, 6, 9, 12 , 15, 18, 21, .........., 99]
three = range(3, 101, 3)
print(list(three))

# [실습 3] 1.0 ~ 10.0 사이 숫자저장
# range(1.0, 10.1) => 불가 int만 가능 
# 굳이 실수로 하고 싶으면 -> 형변환
data = list(range(1, 11))
# print(float(data)) -> 불가능, list 전체를 float로 변환을 못함 하나하나 뺴서 변환을 해야함
# float(data[0])
# float(data[1]) -> 이런 식으로 해야함 
# ===> map() 사용

data = map(float, data) # map은 object => 최종적으로 map -> list로 형변환 해야함
data = list(data)
print(data)