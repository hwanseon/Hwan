# ----------------------------------------
# Tuple data 자료형 살펴보기
#  - 내장함수 : len(), max(), min(), sum() ...
#  - 연산자: 덧셈, 곱셈, 멤버연산자
# ----------------------------------------
nums = 11, 22, 33, 44, 55

# 내장함수 
print(f'nums의 개수 : {len(nums)}개')
print(f'최대값 : {max(nums)}, 최소값 : {min(nums)}')
print(f'nums의 합계 : {sum(nums)}')
print(f'정렬 : {sorted(nums)}, {sorted(nums, reverse = True)}')
# sorted(list[]) -> 정렬 함수, sorted(data = list, reverse = True) => 내림차순 정렬

print( max('abc', 'abC'))
print( sorted(['abc', 'Zoo']))

# 연산자
# 덧셈
data1 = 11, 22
data2 = 'A', 'B', 'C'
data3 = [1, 2]

print(data1 + data2) # list는 합쳐서 하나의 문자열로 덧셈, 튜플 + 튜플은 하나의 튜플로
# print(data1 + data3) 형이 동일해야 덧셈 가능 => 형 변환 후 연산 수행
print(data1 + tuple(data3))

# 곱셈 => tuple * int => list랑 동일 
print(data1 * 3)

# 멤버연산자 => in, not in
print(11 in data1)
print('A' in data1)