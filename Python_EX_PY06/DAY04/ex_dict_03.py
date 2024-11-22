# --------------------------------------
# Dict 자료형 살펴보기
#  - Dict 자료형 전용의 함수 즉, 메서드(Method) 사용
#  - 사용법: 변수명.method명()
# --------------------------------------
## [Dict에서 키만 추출하는 메서드 keys()] -----
p1 = {'name': '홍길동', 'age': 20, 'job':'student'}

result = p1.keys()
print(f'키 추출 : {result}, {type(result)}')

# list 형변환 -> list(keys)
result=list(result)
print(f'키 추출 : {result}, {type(result)}')

## [Dict에서 값/데이터만 추출하는 메서드 values()] -----
result = p1.values()
print(f'값/데이터 추출 : {result}, {type(result)}')

## [Dict에서 키+데이터 추출하는 메서드 items()] -----
result = p1.items()
print(f'키 + 값을 묶어서 추출 : {result}, {type(result)}') # -> 값은 튜플 

result = list(result)
print(f'키 + 값을 묶어서 추출 : {result[0]}, {type(result[0])}')