# --------------------------------------------------------------
# 제어문 - 반복문
# --------------------------------------------------------------
# [실습] 문자열을 기계어 즉, 2진수로 변환해서 저장
# - ex) 입력: Hello, 출력: Hello에 대한 2진수

# 코드값 -> 10진수 -> 2진수 
msg = 'Hello'
result = ''
for m in msg :
    result = result + bin(ord(m))[2:]
print(result)

# [실습] 요소/원소의 인덱스와 값을 함께 가져오기
# enumerate() 내장함수
# - 전달된 반복가능한 객체에서 원소당 번호를 부여해서 튜플로 묶어줌
# - 원소의 인덱스 정보가 필요한 경우 사용 
# -----------------------------------------------
nums = [11, 33, 55]

# 원소만 가져오는 경우
for n in nums :print(n)

# 원소에 인덱싱 부여한 객체 변환 
print("enumerate() 변환 : ", list(enumerate(nums)))

# 인덱스와 원소 데이터 가져오기
for idx, data in enumerate(nums) :  # -> 언패킹으로 가져옴 
    print(idx, data) # 인데스와 원소를 가져옴

# e = (0,11)
for e in enumerate(nums) :
    print(e[0], e[1]) # 인데스와 원소를 튜플 가져옴
    nums[e[0]] = int(e[1])

nums = ['11', '33', '55']
# e = (0,'11')
for e in enumerate(nums) :
    print(e[0], e[1]) 
    nums[e[0]] = int(e[1])