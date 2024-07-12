## 리스트와 튜플 응용하기 p244
a = [10, 20, 30]
a.append(50)
print(f'a의 길이 => {len(a)}, {a}')

a = []
a.append(10)
print(a)

a = [10, 20, 30]
a.append([500, 600])
print(a, len(a))

# 리스트 확장 
a = [10, 20, 30]
a.extend([500, 600])
print(a, len(a))

# 특정 인덱스 요소에 추가
a = [10, 20, 30]
a.insert(2, 500)
print(a, len(a))

# 끝에 추가하기
a = [10, 20, 30]
a.insert(len(a), 500)
print(a)

a = [10, 20, 30]
a[1:1] = [500, 600]
print(a)

# 삭제 
a = [10, 20, 30]
a.pop() ; print(a)
a.pop(1) ; print(a)
a = [10, 20, 30]
del a[1] ; print(a)
a = [10, 20, 30]
a.remove(20) ; print(a)
a= [10, 20, 30, 20] # 값이 여러개일때는 처음값 삭제
a.remove(20) ; print(a)

# 리스트에서 특정 값의 인덱스 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.index(20)) 
print(a.count(20))
a = [10, 20, 30, 15, 20, 40]
print(a.reverse())
print(a.sort())
print(sorted(a))
print(a.clear())
a = [10, 20, 30, 15, 20, 40]
del a[:]
print(a)
a = [10, 20, 30]
a[len(a):] = [500]
print(a)

# 리스트 할당과 복사
a = [0,0,0,0,0] 
b = a 
print(a is b)
b[2] = 99
print(a, b)
a = [0,0,0,0,0] 
b = a.copy()
print(a is b, a == b) # a, b는 다른 객체 => 둘 중 하나의 값을 변경해도 서로에게 영향 X
b[2] = 99
print(a, b)

# for 반복문으로 요소 출력하기 p256
a = [38, 21, 53, 62, 19]
for i in a :
    print(i)

# 인덱스와 요소를 함께 출력하기
a = [38, 21, 53, 62, 19]
for idx, v in enumerate(a) :
    print(idx, v)

for idx, v in enumerate(a, start = 1) :
    print(idx,v)

# while 반복문으로 요소 출력하기 p258
a = [38, 21, 53, 62, 19]
i = 0
while i < len(a) :
    print(a[i])
    i += 1

## list에 가장 작은수, 가장 큰수, 합계 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a :
    if i < smallest :
        smallest = i

print(smallest)

a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a :
    if i > largest :
        largest = i

print(largest)

a = [38, 21, 53, 62, 19]
print(a.sort())
print(a[0])
a = [38, 21, 53, 62, 19]
a.sort(reverse =  True)
print(a[0])

print(min(a), max(a))

a = [10, 10, 10, 10, 10]
x = 0
for i in a :
    x += i
print(x)
print(sum(a))

# conprehension
a= [i for i in range(10)]
print(a)
b = list(i for i in range(10)) ; print(b)
c = [i+5 for i in range(10)] ; d = [i*2 for i in range(10)]
print(c,d)

a = [ i for i in range(10) if i % 2 == 0]
print(a)

b = [ i + 5 for i in range(10) if i % 2 == 1] ; print(b)

## 튜플 표현식
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

## 2의 거듭제곱 리스트 생성하기 p271
# start, end = map(int, input().split())
# num = list(range(start, end+1))
# c= [2**v for idx, v in enumerate(num) if not(idx == 1 or idx == len(num)-2)]
# print(c)

## 딕셔너리 응용하기 p313
x = {'a':10, 'b':20, 'c':30, 'd':40}
x.setdefault('e') # 키 값만 입력하면 값은 Nnoe
print(x)

x = {'a':10, 'b':20, 'c':30, 'd':40}
x.update(a=90)
print(x)
x.update(e=50)
print(x)
x.update(a=900, f=60)
print(x)
y = {1:'one', 2:'two'}
y.update({1:'ONE', 3:'THREE'})
print(y)
y.update([[2, 'TWO'], [4, 'FOUR']])
print(y)

y.update(zip([1,2], ['one', 'two']))
print(y)

## 리스트와 튜플로 딕셔너리 만들기 p318
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)