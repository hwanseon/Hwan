# ----------------------------------
# Set 자료형 살펴보기
#  - 여러가지 종류의 여러개 데이터를 저장
#  - 단, 중복 불가  =============> 중복 제거 시 사용 
#  - 컬렉션 타입의 데이터 저장 시 Tuple 가능
#  - 형태: {data 1, data 2, data 3, ......, data n}
# ----------------------------------

## [Set 생성] -----------------
data = [] # 비어있는 list
data = () # 비어있는 tuple
data = {} # 비어있는 dict
data = set() # 비어있는 set

print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, data : {data}) ')

## 여러개 data 저장한 set
data = {10, 20, 30, -9, 10, 30, 10, 10, 10, 30}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, data : {data}) ') # 중복이 제거됨 
data = {9.34, 20, 'Apple', '10', True, 10, 10, 10, 30}
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, data : {data}) ') 
# data = {1, 2, 3, [1, 2, 3]} ===> list는 원소/요소 불가능
# print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, data : {data}) ') 
data = {1, 2, 3, (1, 2, 3)} # 튜플은 원소/요소 가능 
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, data : {data}) ') 
data = {1, 2, 3, (1)} # -> 1 중복 (1)은 튜플 X, 튜플이 되려면 (1,)
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, data : {data}) ') 
data = {1, 2, 3, (1,)} # ==> tuple
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, data : {data}) ') 
data = {1, 2, 3, (1,)[0]} # tuple에서 0번 원소는 1 (정수)
print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, data : {data}) ') 

# data2 = {1, 2, 3, data} data는 변경이 가능한 값 => set에 들어올 수 없음 
# print(f'data의 타입 : {type(data)}, 원소/요소 개수 : {len(data)}개, data : {data}) ') 
# data = {1, 2, 3, {1:100}} ===> dict도 변경 가능한 값이기에 set에 들어올 수 없음

## set() 내장함수
# 다양한 타입 ==> set 변환
data = {1, 2, 3} # ===> set([1, 2, 3]) 둘 다 동일
dict = set({1, 2})
data = set () # empty set
data = set({1, 2, 3}) # 형변환 : list -> set
data = set[1, 2, 3, 2, 1]

data = set("Good")
print(data)

data = set({'name':'홍길동', 'age': 12, 'name':'베트맨'})
print(data)
print({'name':'홍길동', 'age': 12, 'name':'베트맨'}) # 베트맨이 홍길동을 덮어씌움

data = set((1, 2, 3, 2, 1, 2, 1))
print(data) # tuple의 중복도 제거 

# set에서 데이터 추가 및 삭제할때는 전용 메서드를 사용해서 해야함