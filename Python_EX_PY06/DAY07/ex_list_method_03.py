# ------------------------------------------------
# 리스트 전용의 함수 즉, 메서드 (Method)
# - 리스트 원소/요소를 제어하기 위한 함수
# ------------------------------------------------
# [메서드 - 요소 순서 제어 메서드 reverse()]
import random as rad

rad.seed(10)  # 동일한 랜덤 숫자 추출을 위한 기준점 
datas = []
for _ in range(10) :
    datas.append(rad.randint(1,30))

print(f'datas의 개수 : {len(datas)}, {datas}')

## 0번 -> -1번, -1번 -> 0번으로 
datas.reverse()
print(f'datas의 개수 : {len(datas)}, {datas}')

# [메서드 - 요소 크기를 비교해서 정렬해주는 메서드 sort())]
# 기본정렬 : 오름차순 즉, 작은 데이터부터 큰 데이터 순서로
datas.sort() # 원본 값에 순서변경이 저장된 것임
print(f'datas의 개수 : {len(datas)}, {datas}')

# 내림차순 즉, 큰 데이터부터 작은 데이터 순서로
datas.sort(reverse = True) # 원본 값에 순서변경이 저장된 것임
print(f'datas의 개수 : {len(datas)}, {datas}')

# [메서드 - 리스트에서 요소를 꺼내는 메서드 pop()]
# - 리스트에서 요소가 삭제됨 
# - remove는 값을 삭제하지만 pop는 값을 꺼내서 (리스트에는 없지만) 값을 줌
value = datas.pop() # 제일 마지막 원소/요소를 꺼냄 
print(f'value : {value} {len(datas)}, {datas}')

value = datas.pop(0) # pop(특정 인덱스) 하면 원하는 값 꺼내기 가능
print(f'value : {value} {len(datas)}, {datas}')

# [메서드 - 리스트 확장 시켜주는 메서드 extend()]
datas.extend([11, 22, 33])
print(f'datas의 개수 : {len(datas)}, {datas}')

datas.extend((11, 22, 33)) # extend()안에 [], (), str, 등 이터러블 데이터가 오면 됨
print(f'datas의 개수 : {len(datas)}, {datas}')

datas.extend("Good Luck") 
print(f'datas의 개수 : {len(datas)}, {datas}')

datas.extend({555, 777, 555, 777, 555}) # set은 중복제거이므로 555, 777 1개씩만 들어감
print(f'datas의 개수 : {len(datas)}, {datas}')

datas.extend({'name':'홍길동', 'age':12})  # dict는 키만 들어감
print(f'datas의 개수 : {len(datas)}, {datas}')

# [메서드 - 모든 원소 삭제 메서드 clear()]
datas.clear()
print(f'datas의 개수 : {len(datas)}, {datas}')
