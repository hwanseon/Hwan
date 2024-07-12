# ----------------------------------------------
# Tuple 전용 함수 즉, 메서드
# - 수정 불가 즉, 추가, 삭제, 변경 X
# ----------------------------------------------
nums = 10, 20, 30

## [메서드 - 인덱스 확인 메서드 inedex(data)]
idx = nums.index(20)
print(idx)

if 5 in nums :
    idx = nums.index(20)
    print(idx)

## [메서드 - data 갯수 메서드 count(data)]
print(10, nums.count(10))
print(5, nums.count(5))
