# ----------------------------------------
# Tuple data 자료형 살펴보기
#  - 다양한 종류의 여러 개 데이터를 저장하는 타입
#  - list와 비슷하지만 수정, 삭제 불가 => 읽기만 가능
#  - 형식 : (데1, ....,데n)
#            데1, ......, 데n
#           (데1,) or 데,
# ----------------------------------------
# 튜플 데이터 생성
datas = ()
print(type(datas), datas, len(datas))

datas = (1, 5, 7)
print(type(datas), datas, len(datas))

# datas = (1) -> int로 취급
# print(type(datas), datas, len(datas)) => int는 원소 개념이 없기에 len() 사용 X

datas = (1,) # 1개 들어가면 ,를 꼭 찍어줘야함
print(type(datas), datas, len(datas))

datas = 1, 
print(type(datas), datas, len(datas))

# 튜플 data의 원소/요소 읽기
datas = 11, 22, 33, 44, 55
# 여러개의 data를 1개의 변수로 사용 -> 인덱스를 붙어줘야함
#        0  1   2   3   4
#       -5  -4  -3  -2  -1

# 2번 요소 읽기
print(datas[2], datas[-3])

# 1~3번 요소 읽기
print(datas[1:4]) 

# 요소/원소 수정 및 삭제 => 변경이 불가
# 마지막 원소를 'A'로 변경하고자 함
# datas[-1] = 'A'
# print(datas)

# last 원소 삭제
# del datas[-1]

# 튜플 데이터의 요소/원소 변경 => 형변환 
birth = (2024, 1, 1)

# 1월 => 3월로 변경요망 
# birth가 튜플이기 떄문에 list로 형변환
birth = list(birth)
birth[1] = 3

# data 변경될수도 있으니 다시 tuple로 형변환
birth = tuple(birth)
print(birth)