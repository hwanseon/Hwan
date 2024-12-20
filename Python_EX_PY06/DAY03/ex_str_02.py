# -------------------------------------
# 문자열 str 데이터 다루기
#  - 문자요소 연산 : 산술, 비교, 멤버연산 
# -------------------------------------
# [1] 산술연산 
data1 = "Happy"
data2 = "Year"

# 덧셈(+) 연산 : str + str => str 연결, 문자열은 문자열끼리만 덧셈연산 가능
print(f'{data1} + {data2} => {data1 + data2}')
print(f'{data1} + {10} => {data1 + str(10)}')

# 뺄셈(-) 연산 : str - str => str 연결 : 미지원, 즉 불가능
# print(f'{data1} - {data2} => {data1 - data2}') => 미지원 

# 곱셈(*) 연산 : str * int => 숫자만큼 반복 str 연결
print(f'{data1} * {3} => {data1 * 3}')

# [2] 멤버 연산 
# 요소/원소가 있을 시에만 사용 가능 
# 요소/원소 in 문자열 => 존재 O True, 존재 X False
# 요소/원소 not in 문자열 => 존재 O False, 존재 X True
print(f'h in {data1} : {"h" in data1}')
print(f'h not in {data1} : {"h" not in data1}')

# print(3 in 123) => ERROR 123은 123을 의미하지 1, 2, 3을 의미하진 않음 
# print(len(123)) => ERROR
# ==> 요소/원소를 가진 데이터 타입에서만 사용 가능 