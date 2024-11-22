# --------------------------------------
# Dict 자료형 살펴보기
#  - 데이터의 의미를 함께 저장하는 자료형
#  - 형태 : {키1 : 값, 키2 : 값, ....., 키n:값 }
#  - 키는 중복 X, 값은 중복 O
#  - Data 분석 시 파일 데이터 가져올 때 많이 사용 + data 저장 시에도 많이 사용
# --------------------------------------

## [dict 생성]
data = {} # 비어있는 dict
print(f'data => {len(data)}개, {type(data)}, {data}')

# 사람에 대한 정보 : 이름, 나이, 성별
data = {'name':'마징가', 'age':100, 'gender':'M'}
print(f'data => {len(data)}개, {type(data)}, {data}')

# 강아지에 대한 정보 : 품종, 무게, 색상, 성별, 나이 
dog = {'kind': '푸들', 'wieght':'7.5kg', 'color':'brown', 'gender':'M', 'age':6}
print(f'dog => {len(dog)}개, {type(dog)}, {dog}')

## [dict 요소/원소 읽기]
#  - 키를 가지고 값/데이터 읽기
#  - 형식: 변수명[키]
dog = {'kind': '푸들', 'weight':'7.5kg', 'color':'brown', 'gender':'M', 'age':6}

# 색상출력
print(f'색상 : {dog["color"]}')

# 성별, 품종 출력
print(f'성별 : {dog["gender"]}, 품종 : {dog["kind"]}')

## [dict 요소/원소 변경]
# 변수명[키] = 새로운 값

# age 6 -> 7
dog['age'] = 7
print(dog)

# weight 7.5kg -> 8kg 
dog['weight'] = '8kg'
print(dog)

## [dict 요소/원소 삭제]
# del 변수명[키] or del(변수명[키])
# gender data 삭제
del dog['gender']
print(dog)

## [dict 요소/원소 추가]
# 변수명[새로운 키] = 값
# 이름 추가
dog["name"] = "김삼식"
print(dog)