# ----------------------------------------------
# 람다표현식, 람다함수 => 다시 쓸 일 없을 때 (이번만 쓸 때 사용)
# - 1줄 함수, 익명함수
# - 형식: lambda 
# - 매개변수 : 실행코드
# -----------------------------------------------
names = {1:'kim', 2:'Adam', 3:'Zoo'}

# 정렬하기 => 내장함수 sorted() => list 반환
# [기본] : key로 정렬
result = sorted(names)
print("오름차순 정렬 [키 기준] : ", result)

# vlaue로 정렬 // names.items() => (1, 'kim), (2,'Adam'), (3,'Zoo')
result = sorted(names.items(), key = lambda itesms: itesms[1]) # 마지막 괄호는 변수명 아무거나 하면 됨
print("오름차순 정렬 [value 기준]: ", result)

result = sorted('This is a test string form Andrew'.split())
print(result)
result = sorted('This is a test string form Andrew'.split(), key=str.lower)
print(result)

## map 내장함수와 lambda ------------------------------------
data = [11, 22, 33, 44]

# 각 원소의 값에 *2 ==> list 저장 
def multi2(value) : return value*2

data2 = list(map(multi2, data))
print(data2)

def multi2(value) : return value*2 # 두번 안 쓸 함수 => 람다 사용

data2 = list(map(lambda a:a*2, data)) # 람다 뒤에는 아무 변수
print(data2)