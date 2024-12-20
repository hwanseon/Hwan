# --------------------------------------
# 내장함수 map(함수명, 여러개 데이터)
# --------------------------------------
data = input('숫자 데이터 입력 : ')
print(type(data))

# 1개의 문자열 => 여러개 문자열 분리
# ex) '10, 20, 30' => '10', '20', '30'  
nums = data.split()

# 문자열 숫자 => 정수로 형변환
result = map(int, nums)
print(type(result), result)

myfunc = int  # myfunc = int() 하면 int()의 결과에 대한 주소를 주어지므로 틀린 것임
result2 = map(myfunc, nums)
print(type(result2), result2)
print(id(int), id(myfunc))

# --------------------------------------
# 형변환 => 자동형변환, 수동형변환 
#          1) 자동형변환: 컴퓨터가 진행 => 작은 것 -> 큰 것
#          2) 수동형변환: 개발자가 진행 => 큰 것 -> 작은 것
# --------------------------------------

a = 10
b = 3
print(a/b) # 자동형변환 int -> float