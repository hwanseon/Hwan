# --------------------------------------
# Dict 자료형 살펴보기
#  - 연산자와 내장함수
# --------------------------------------
person = {'name': '홍길동', 'age': 20, 'job':'student'}
dog = {'kind': '푸들', 'weight':'7.5kg', 'color':'brown', 'gender':'M', 'age':6}

## [연산자]
# 산술 연산 x
# person + dog 

# 멤버 연산자 : in, not in
#      key
print('name' in dog)
print('name' in person)

#      value : dict 타입에서는 key만 멤버 연산자로 확인 
print('푸들' in dog)
print(20 in person)

# value 추출 .values()
print('푸들' in dog.values())
print(20 in person.values())

## [내장함수]
# 원소/요소 개수 확인 : len()
print(f'dog의 요소 개수: {len(dog)}개')
print(f'person의 요소 개수: {len(person)}개')

# 원소/요소 정렬 : sorted() -> 반환값은 list
# - 키만 추출되고 정렬됨
print(f'dog 정렬 : {sorted(dog)}')
print(f'dog 정렬 : {sorted(dog, reverse = True)}') # 내림차순 정렬
jumsu = {'국어': 90, '수학': 170, '영어': 100}
## 값을 정렬하고 싶을 떄 
# print(f'dog 정렬 : {sorted(dog.values())}') -> ERROR 값이 int, str도 있기 때문에 정렬이 안됨 
print(f'점수 키 정렬 : {sorted(jumsu)}')
print(f'점수 값 정렬 : {sorted(jumsu.values())}')
print(f'점수 값 정렬 : {sorted(jumsu.values(), reverse = True)}')
# jumsu 값 오름차순 정렬 : [90, 100, 170]
# jumsu 키 오름차순 정렬 : ['국어', '수학', '영어']
# 대칭이 안됨 

print(f'jumsu 값 오름차순 정렬 : {sorted(jumsu.items())}')
# jumsu 값 오름차순 정렬 : [('국어', 90), ('수학', 170), ('영어', 100)] -> 키 값으로 오름차순으로 정렬됨

# 값을 기준으로 오름차순으로 정렬                                     x = ('국어', 90), x[0] = '국어', x[1] = 90이기에 x[1]이 기준 
print(f'jumsu 값 오름차순 정렬 : {sorted(jumsu.items(), key = lambda x:x[1])}')
#                                                                   의미: x중에서 1번자리에 있는 원소를 기준으로 하겠다는 의미

# 동일한 타입에서만 정렬 가능 -------------
# n1 = [1, 4, 5, -2]
# n2 = ['a', 'Z', 'f']
# n3 = [1, 'a', -4, 9, 'B']
# print(sorted(n1), sorted(n2), sorted(n3))  -> 타입이 달라서 정렬 X
## -> 타입이 같으면 정렬 가능