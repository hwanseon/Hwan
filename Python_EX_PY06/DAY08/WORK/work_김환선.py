# 문자열 응용하기 p287
msg = 'Hello, World!'
msg = msg.replace('World', 'Python')
print(msg)

msg = 'apple'
table = str.maketrans('aeiou','12345')
print(msg.translate(table))

fruit = 'apple pear grape pineapple orange'
print(fruit.split())
fruit = 'apple, pear, grape, pineapple, orange'
print(fruit.split(","))

fruits = ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(fruits)

fruits = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(fruits)

msg= "python" ; print(msg.upper())
msg1 = msg.upper() ; print(msg1)
msg2 = msg1.lower() ; print(msg2)

msg3 = '     python      '
print(msg3.lstrip())
print(msg3.rstrip())
print(msg3.strip())

# 특정문자 삭제하기 
msg4 = ', python    .  '
print(msg4.lstrip(",."))
print(msg4.rstrip(",."))
print(msg4.strip(",."))

print(msg.rjust(10))
print(msg.center(20))

print(msg.rjust(30).upper()) # 메서드 체이닝

num = "35"
print(num.zfill(10))

# 문자열 위치 찾기 p293
msg = 'apple pineaplle'
#      012345678901234
print(msg.find('pl'))
print(msg.rfind('pl'))
print(msg.rfind("xy")) # -1 반환
print(msg.count('pl'))

# 서식지정자로 문자열 넣기
name = 'minsu'
print('I am %s' % name)
print('I am %d years old' % 25)
print('%f'%2.5) # %7은 기본적으로 소수점 이하 6자리까지 
print('%.2f'%2.5) ; print('%.3f'%2.5) # 소수점 자리수 출력
print('Today is %d %s' % (3, 'June'))

# format 메서드 

# ## 특정 단어 개수 세기 p305
# data = input().strip()
# print(data.count('the'))
# ## 높은 가격순으로 출력하기 p305
# price = input().split(";")
# price = sorted(price, reverse = True)
# for p in price :
#     p =int(p)
#     print(f'{p:>9,}')

## 함수 사용하기 p372
def hello() :
    print('Hello, world!')

hello()

def add(a,b) :
    print(a+b)

add(10,20)

# ## 사칙연산 함수 만들기 p384
# x, y = map(int, input().split())

# def plus(x, y) :
#     a = x + y
#     return a
# def minus(x, y) :
#     s = x - y
#     return s
# def mult(x, y) :
#     m = x * y
#     return m
# def div(x,y) :
#     d = x / y
#     return d
# a, s, m, d = plus(x,y), minus(x, y), mult(x, y), div(x,y)
# print(f'덧셈 : {a}, 뺄셈 : {s}, 곱셉 : {m}, 나눗셈 : {d}')

# 함수에서 위치 인수와 키워드 인수 사용하기 p386
x = [10, 20, 30]
print(*x)

def print_numbers(*args) :
    for arg in args :
        print(arg)

print_numbers(10)

def print_numbers(*args) :
    for arg in args :
        print(arg)

print_numbers(10, 20, 30, 40)
print_numbers(x)
print_numbers(*x)

def personal_info(name, age, address) :
    print('이름 : ', name)
    print('나이 : ', age)
    print('주소 : ', address)

personal_info('홍길동', '30', '대구광역시')
personal_info(name = '홍', age = 30, address = "대구광역시")

x = {'name':'홍길동', 'age':30, 'address':"대구광역시"}
personal_info(**x)
personal_info(**{'name':'홍길동', 'age':30, 'address':"대구광역시"})
