# --------------------------------------
# 함수명에 대해서 
# -> 코드가 있는 부분에 붙여진 이름 
# -> 코드가 시작되는 주소를 저장하고 있음 
# --------------------------------------
# [실습] 내장함수 
show = print
show("Happy")

# 함수명 여러개를 리스트에 담아서 원소로 처리 --------------
data = [11, 22, 33]
func = [max, min, sum] # 함수 이름이 리스트에 담길 수 있음 => 원소취급

print(func[0](data), func[1](data), func[2](data))

# print = 10
# print("A")  ==> ERROR 10('A')로 해야 출력됨