# print('Hello, world!')

# # p49 
# print('Hello, world!')
# print('Python Programming')

# print('Hello, world!')
# print('Hello, world!')

# # p50
# print('Hello, world!')
# print('Hello'); print('1234')

# # p52
# a = 10
# if a == 10 :
#     print('10')
#     print('10입니다.')

# # p 56
# print( 1 + 1 )
# print(1-2)
# print(2*2)
# print(5/2)
# print(4/2)

# print(5//2)
# print(4//2)
# print(5.5//2)
# print(4//2.0)
# print(4.1 // 2.1)

# print(5%2)
# print(2 ** 10)

# # p58
# print(int(3.3))
# print(int(5/2))
# print(int('10'))
# print(type(10))
# print(divmod(5, 2)) # 몫, 나머지를 동시에 구하는 => 튜플
# print(0b110)
# print(0o10)
# print(0xF)

# # P59
# print(3.5+2.1)
# print(4.3-2.7)
# print(1.5*3.1)
# print(5.5/3.1)
# print(4.2+5)

# # p60
# print(float(5))
# print(float(1+2))
# print(float('5.3'))
# print(type(3.5))

# # p61
# print(35 + 1 * 2)
# print((35 + 1) * 2)

# # p62
# road = int(input("도로와의 거리 : "))
# print(int(0.2467 * road + 4.159 ), '층')

# print(102 * 0.6 +225)

# # p63
# x = 10
# print(x)
# y= 'Hello, world!'
# print(y)
# print(type(x))
# print(type(y))

# # p 65
# x, y, z = 10, 20, 30
# print(x); print(y); print(z)
# x = y = z = 10
# print(x); print(y); print(z)
# x, y = 10, 20
# x, y = y, x
# print(x); print(y)

# # p66
# a, b = 10, 20
# c = a + b
# print(c)

# a = 10
# print(a + 20)
# print(a)

# a = 10
# a = a + 20 
# print(a)

# a = 10
# a += 20 # a와 20을 더한 후 결과를 다시 a에 저장
# print(a)

# h = input("내용 : ")
# print(h)

# x = input("문자열을 입력하세요 : ")
# print(x)

# a = int(input(" 첫 번째 숫자를 입력하세요 : "))
# b = int(input(" 두 번째 숫자를 입력하세요 : "))
# print(a+b)

# # p71
# a, b = input("문자열 두 개를 입력하세요 : ").split() # 입력받은 값을 공백을 기준으로 분리 
# print(a); print(b)

# a, b = input("숫자 두 개를 입력하세요 : ").split()
# a = int(a)
# b= int(b)
# print(a+b)

# # p73
# a, b = map(int, input("숫자 두 개를 입력하세요 : ").split()) # map = split의 결과를 int or float로 반환
# print(a+b) 

# a, b = map(int, input("숫자 두 개를 입력하세요 : ").split(","))
# print(a+b) 

# # p75
# a, b, c = map(int, input("정수 세 개를 입력하세요 : ").split())
# print(a+b+c)

# a = 50
# b = 100
# c = "None"
# print(a)
# print(b)
# print(c)

# a, b, c, d = map(int, input().split())
# print((a+b+c+d)/4)

# # p77
# print(1, 2, 3)
# print('Hello', 'Python')
# print(1, 2, 3, sep = ", ")
# print(1, 2, 3, sep = ",")
# print('Hello', 'Python', sep = '')
# print(1920, 1080, sep = 'x')
# print(1, 2, 3, sep ='\n')
# print('1\n2\n3')

# # p79
# print(1, end = " ")
# print(2, end = " ")
# print(3)


# # p87
# print(3>1)
# print(10 == 10)
# print(10 != 5)
# print('Python'=='Python')
# print('Python'=='python')
# print('Python'!='python')

# print(10>20)
# print(10<20)
# print(10>=10)
# print(10<=10)

# print(1 is 1.0)  # 값(숫자)을 비교할때는 is 연산자 말고 비교 연산자 (==, !=) 사용
# print( 1 is not 1.0)

# # p90
# print(True and True)
# print(True and False)
# print(False and False)
# print(not True)
# print(not False)
# print(not True and False or not False)

# print(10 == 10 and 10 != 5)
# print(10 > 5 or 10 > 3)
# print(not 10 > 5)
# print(not 1 is 1.0)

# p95
Korean = 90
math = 85
English = 80
science = 80
print(Korean >= 90 and English > 80 and math > 85 and science >= 80)

# p96
hello = 'Hello world'
print(hello)

hello = "안녕하세요"
print(hello)

hello = '''Hello, world !
안녕하세요.
Python 입니다.'''
print(hello)

s = "Pyhhon isn't difficult"
print(s)

s = 'He said "Python is easy"'
print(s)