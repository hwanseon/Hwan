# ------------------------------------------
# 제어문 - while 반복문
# ------------------------------------------
num = 10

# while num > 0 :
#     print(num) # 무한반복 ==> 터미널에서 Ctrl + s
               # 초기값을 갱신하는 data가 있어야함 

while num > 0 :
    print(num) 
    num = num -1 

# [실습] list의 원소 읽기 -------------
## - while 반복문 : 개수(인덱스를 알기 위해)
nums = [11, 22, 33]

cnt = 0 
while cnt < len(nums) :
    print(cnt, nums[cnt])
    cnt = cnt + 1

## [실습] 'hello' 문자열의 원소를 하나씩 출력하기
msg = 'Hello'

idx = 0 
while idx < len(msg) :
    print(msg, msg[idx])
    idx = idx + 1