# ----------------------------------------------
# List/Set/Dict 자료형과 반복문, 조건브표현식 결합
# - 메모리 사용량 감소 & 속도 향상
# conprehensions ==> 대량의 data 처리 시 사용 
# ----------------------------------------------
# [실습] A리스트의 데이터를 b 리스트에 담기
#        단, A 리스트에서 짝수값은 3을 곱하고, 홀수값은 그대로해서 B리스트에 담기
# ----------------------------------------------
a = [1, 2, 3, 4, 5, 6]
b = []
for num in a :
    if num%2 : 
        b.append(num)
    else :
        b.append(num*3)

print(f'a=>{a}\nb=>{b}')
# ----------------------------------------------
# [1] 모든 원소를 새로운 리스트에 담기
c = [num for num in a ] # fof num in a a에서 나온 num을 새로운 num에 넣는다는 의미
print(f'a=>{a}\nb=>{b}\nc=>{c}')
# ----------------------------------------------
# [2] 짝수 원소만 새로은 리스트 c에 담기
# if not num%2 : c.append(num*3) 이 들어가야함
c = [num*3 for num in a if not num%2] # list 안에서 for문을 먼저
# 1) for num in a 뽑고 2) if not num%2 조건 검사 후 3) num에 추가 후 *3
print(f'a=>{a}\nb=>{b}\nc=>{c}')
# ----------------------------------------------
# [3] 짝수 데이터는 3을 곱하고 홀수 데이터는 그대로 새로운 리스트에 담기
c = [num*3 if not num % 2 else num for num in a ]
# 1) for num in a, 2) num*3 if not num % 2 else num 
print(f'a=>{a}\nb=>{b}\nc=>{c}')
