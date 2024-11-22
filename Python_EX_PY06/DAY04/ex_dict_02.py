# --------------------------------------
# Dict 자료형 살펴보기
#  - 여러가지 data를 dict 타입으로 저장
# --------------------------------------
# 다양한 종류의 키(key)

## key가 1개로 안되는 경우 
# - 키 여러개 정보 합쳐서 사용하는 경우  => tuple 타입으로 사용해야함 
# - ex) 홍길동 1996, 홍길동 2000 -> 이름과 생년월일
person = {'age': 20, ("홍길동", 2000): 100} # tuple로 사용

# 3명의 정보 저장
p1 = {'name': '홍길동', 'age': 20, 'job':'student'}
p2 = {'name': '마징가', 'age': 100, 'job':'cooker'}
p3 = {'name': '베트맨', 'age': 98, 'job':'police'}
p4 = {'name': '홍길동', 'age': 11, 'job':'student'}
# 4개의 정보를 하나에 담고 싶음
person = [p1, p2, p3, p4] # list에 담기
# p1의 이름 찾기
print(person[0]['name'])
# dict로 담는 경우 -> data에서 중복 안되는 값 1개 찾아서 찾기
# 키: 나이 데이터를 쓴 경우
person2 = {20:{'name': '홍길동', 'job':'student'},
           100:{'name': '마징가', 'job':'cooker'},
           98:{'name': '베트맨', 'job':'police'},
           11:{'name': '홍길동', 'job':'student'}}
print(person2)

# 키: 이름과 나이 데이터 사용
person3 = {('홍길동', 20):{'job':'student'},
           ('마징가', 100):{'job':'cooker'},
           ('베트맨', 98):{'job':'police'},
           ('홍길동', 11):{'job':'student'}}
print(person3[('홍길동',20)])