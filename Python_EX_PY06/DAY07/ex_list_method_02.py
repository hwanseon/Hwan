# ------------------------------------------------
# 리스트 전용의 함수 즉, 메서드 (Method)
# - 리스트 원소/요소를 제어하기 위한 함수
# ------------------------------------------------
# [메서드 - 요소 추가 메서드 append(data)]
datas = [1, 3, 5]

# 새로운 data 100 추가 : 제일 마지막 원소로 추가
datas.append(100)
print(f'datas의 개수 : {len(datas)}, {datas}')

# 중복값 한번더 추가하기 ===> list는 똑같은 값이 들어가도 상관X ==> 인덱스로 값 구분
datas.append(100)
print(f'datas의 개수 : {len(datas)}, {datas}')

# [메서드 - 요소 추가 메서드 insert(추가하고 싶은 위치의 인덱스, data)]
datas.insert(0, 1024)
print(f'datas의 개수 : {len(datas)}, {datas}')
datas.insert(-1, 1024) # => 제일 마지막 자리에 넣고싶을 때
print(f'datas의 개수 : {len(datas)}, {datas}')

# [실습: 임의의 정수 숫자 10개 저장하는 리스트 생성] ------
# 1) random 모듈, 2) 빈리스트 생성, 3) for 반복문 
import random as rad

nums = []
for cnt in range(10) :
    n = rad.randint(1, 50)
    nums.append(n)

print(f'nums => {nums}')

# [메서드 - 요소 삭제 메서드 remove(data)] 
# 존재하지 않는 데이터 삭제 시 ERROR 발생 
datas = [1024, 1, 3, 5, 100, 1024, 100]
datas.remove(1024)
print(f'datas의 개수 : {len(datas)}, {datas}')

# 중복 data 한번에 삭제
for cnt in range(datas.count(1024)) :
    datas.remove(1024)
    print(f'datas의 개수 : {len(datas)}, {datas}')
