# ----------------------------------------
# List 데이터 자료형 살펴보기
#  - list와 메모리
# ----------------------------------------
# List 생성
nums = [] # 리스트가 비어있지만 메모리는 할당 받음
nums2 = list() # 리스트가 비어있지만 메모리는 할당 받음
print(f'nums의 id => {id(nums)}')
print(f'nums2의 id => {id(nums2)}')

nums = [10, 20]
nums2 = list([10, 20])

print(f'nums의 id => {id(nums)}')
print(f'nums[0]의 id => {id(nums[0])}')
print(f'nums[1]의 id => {id(nums[1])}')
print("*"*15)
print(f'nums2의 id => {id(nums2)}')
print(f'nums2[0]의 id => {id(nums2[0])}') # 15줄과 주소 동일
print(f'nums2[1]의 id => {id(nums2[1])}') # 16줄과 주소 동일 