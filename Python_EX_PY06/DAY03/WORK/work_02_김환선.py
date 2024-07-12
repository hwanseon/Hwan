# p102 
a = [38, 21, 53, 62, 19]
print(a)

person = ['james', 17, 175.3, True]
print(person)

a = []
b= list()
print(a, b)

print(range(10))

a = list(range(10))
print(a)

b = list(range(5, 12))
print(b)

c = list(range(-4, 10, 2))
print(c)

d = list(range(10, 0, -1))
print(d)

# 10.2 튜플 사용해보기 p105 
a = (38, 21, 53, 62, 19)
print(a)

a = 38, 21, 53, 62, 19
print(a)

person = ('james', 17, 175.3, True)
print(person)

a = 38,
print(a)

# range를 이용하여 튜플 만들기
a = tuple(range(10))
print(a)
b = tuple(range(5, 12))
print(b)
c = tuple(range(-4, 10, 2))
print(c)

# 튜플을 리스트로 만들고 리스트를 튜플로 만들기
a = [1, 2, 3]
print(tuple(a))

b = (1, 2, 3)
print(list(b))

# 리스트와 튜플로 변수 만들기 p108
a, b, c = [1, 2, 3]
print(a, b, c)
d, e, f = (4, 5, 6)
print(d, e, f)

# 리스트언패킹, 튜플 언패킹 => 언패킹: 리스트와 튜플의 요소를 변수 여러 개에 할당하는 것
x = [1, 2, 3]
a, b, c = x 
print(a, b, c)
y = (4, 5, 6)
d, e, f = y 
print(d, e, f)

# data = input("숫자 2개를 입력하세요 ex) 10 20 : ").split()
# a, b = data
# print(a, b, type(a), type(b))

# 심사문제: range로 튜플 만들기 p110
# data = int(input())
# print(tuple(range(-10,11,data)))

# 시퀀스 자료형 활용하기 p111
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(30 in a); print(100 in a)
print(100 not in a); print(30 not in a)

print(43 in (38, 76, 43, 62, 19))
print(1 in range(10))
print('P' in 'Hello Python')

# 시퀀스 객체 연결하기
a = [0, 10, 20, 30]
b = [9, 8, 7 ,6]
print(a+b)

# 문자열과 숫자 연결
print('Hello' + str(10))

# 시퀀스 객체 반복하기 p114
print([0, 10, 20, 30]*3)
print(list(range(0, 5, 2)) * 3)
print("Hello"*3)

# 시퀀스 객체의 요소 개수 구하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(len(a))
b = (38, 76, 43, 62, 19)
print(len(b))
# range의 숫자 생성 개수 구하기
len(range(0,10,2))

# 문자열의 길이 구하기 p117
hello = 'Hello, World!'
print(len(hello))

hello = "안녕하세요"
print(len(hello))

# 11.3 인덱스 사용하기 p 118
a = [38, 76, 43, 62, 19]
print(a[0], a[2], a[4])

b =(38, 76, 43, 62, 19)
print(b[0])

r = range(0, 10, 2)
print(r[2])

hello = 'Hello, World!'
print(hello[7])

# __getitem__() 메서드 => 인덱스를 바로 가져올 수 있는 메서드 p119
a = [38, 76, 43, 62, 19]
print(a.__getitem__(1))

# 음수 인덱스 저장 p120
a = [38, 76, 43, 62, 19]
print(a[-1], a[-5])
b = (38, 76, 43, 62, 19)
print(b[-1])
r = range(0,10,2)
print(r[-3])
hello = 'Hello, World!'
print(hello[-4])

# 마지막 요소에 접근하기 p122
a = [38, 76, 43, 62, 19]
print(len(a)) # 5
print(a[len(a)-1]) # -1을 해주어야 마지막 요소에 접근
# del로 요소 삭제
del a[2]
print(a)

# 슬라이스 사용 p125
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[:4])
print(a[1:1])
print(a[1:2])
# 리스트 중간부분 가져오기
print(a[4:7]); print(a[:7])
print(a[4:-1]); print(a[7:])
print(a[:])

# 인덱스 폭 증가하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[2:8:3])
print(a[:7:2])
print(a[7::2])
print(a[::2])
print(a[::]) # 리스트 전체를 가져옴 
print(a[5:1:-1]) # 시작인덱스 > 끝 인덱스 
print(a[::-1])

# len 응용 p131
print(a[0:len(a)]) # a의 요소 10개 -> len(a) = 10이므로 -1을 하면 안됨
print(a[:len(a)])

# 11.4.6 튜플, range, 문자열에 슬라이스 사용하기
b = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
print(b[4:7])
print(b[4:])
print(b[:7:2])

r = range(10)
print(r)
print(r[4:7])
print(r[4:])
print(r[:7:2]); print(list(r[:7:2]))

hello = 'Hello, World!'
print(hello[2:9])
print(hello[2:])
print(hello[:9:2])

# slice  객체 사용하기
print(range(10).__getitem__(slice(4, 7, 2)))

# 슬라이스에 요소 할당
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c'] 
print(a)
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a']  # 요소의 개수를 맞추지 않아도 할당 가능
print(a)
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c', 'd', 'e'] 
print(a)
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:8:2] = ['a', 'b', 'c'] # 슬라이스 요소의 개수 = 할당 개수 => 같지 않으면 오류 
print(a)

# del로 슬라이스 삭제 p138
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:5]
print(a)
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:8:2]
print(a)
# range, 튜플, 문자열은 del로 슬라이스 삭제 불가능

# 11.8 리스트의 마지막 부분 삭제하기 p142
x = input("데이터를 입력하세요 ex) 1 2 3 4 5 6 7 8 9 : ").split()
x = list(x)
print(tuple(x[:len(x)-5]))

# 11.9 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기
x = input().strip()
y = input().strip()
data1 = x[1::2]
data2 = y[::2]
print(data1 + data2)