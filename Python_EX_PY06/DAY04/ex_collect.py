# -------------------------------------
# Collection 자료형에 공통적인 부분 살펴보기
# -------------------------------------
## [여러개의 변수에 데이터 저장]
name = 'hwan-seon'
age = 25
job = 'student'
gender = 'M'
# 패킹(paking) 방식 : 변수명 = tuple 타입
data = 'hwan_seon', 25, 'student', 'M'

# -------------------------------------------------------------
# 언패킹(unpaking): 변1, 변2, ... 변n = tuple 타입
#                   변수명 개수 == 데이터의 수 
# -------------------------------------------------------------
name, age, job, gender = 'hwan-seon', 25, 'student', 'M'
print(name, age, job, gender)

# 개수를 달리하고 싶을 떄 _ 사용 (의미없는 data)
name, age, _, _ = 'hwan-seon', 25, 'student', 'M'
print(name, age, _) # print에 _f를 사용하면 마지막 값이 들어옴 

jumsu = [100, 99]
kor, math = [100, 99]
print(jumsu, kor, math)

person = {'name':'Park', 'age':30}
k1, k2 = {'name':'Park', 'age':30}
print(person, k1, k2)

# -------------------------------------------------------------
# 생성자 (Constructor) 함수: 타입명과 동일한 이름의 함수
#  - int(), float(), str(), bool(), list(), tuple(), dict(), set()
#  - map(), range()
# -------------------------------------------------------------
# 기본(일반적인) 데이터 타입 
num = int(10) ; fnum = float(10.2) ; msg = str('Good') ; isOk = bool(False)
# num = 10,     fnum = 10.2            msg = 'Good'      isOk = Flase
print(num, fnum, msg, isOk)
# 컬렉션 데이터 타입
lnums = list([1, 2, 3, 4])         # 1nums = [1, 2, 3, 4]
tnums = tuple((3, 6, 9))           # tnums = (3, 6, 9)
ds = dict({"d1":10, 'd2':30})     # ds = {'d1':10, 'd2':30}
ss = set({1, 1, 3, 3, 5})          # ss = {1, 1, 3, 3, 5}
print(lnums, tnums, ds)

# 타입 변경 => 형변환 
# dict 자료형은 다른 자료형과 달리 데이터 형태가 다름
#  - data 형태 => 키 : 값 
#  - dict( key 1 = value, key2 = value2) ==> key는 str만 가능 
ds = dict(n1 = 1, n2 = 2, n3 = 3) # key 이름에 '' 사용 금지 (변수명이라서), value에 str이오면 '' or "" 해야함
print(ds)

ds = dict([('name', '마징가'), ('age', 12)]) # 안에 있는 원소가 튜플이면 앞에껄 키, 뒤에껄 값으로 보고 가능함
print(ds)

ds = dict([['name', '마징가'], ['age', 12]])
print(ds)

## 내장함수 : zip() : 같은 인덱스의 요소끼리 묶어줌
l1= ['name', 'age', 'gender']
l2 = ['마징가', 12., 'M']
l3 = [False, True, True]
print(zip(l1, l2, l3)) # -> 타입이 zip() 형태 ===> 보려면 list로 형변환
print(list(zip(l1, l2, l3)))

ds = dict(zip(l1,l2))
print(ds)