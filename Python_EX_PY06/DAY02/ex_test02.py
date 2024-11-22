# --------------------------
# 연산자 실습
# --------------------------

# [실습 1] 문자열 Data 2개에 대한 논리 연산 수행 후 출력
data1 = "Hello"
data2 = "hello"

# print(f'{data1} > "HELLO" and {data2} > "HELLO" : {data1 > "HELLO" and  data2 > "HELLO"}')
# print(f'{data1} > "HELLO" or {data2} == "HELLO" : {data1 > "HELLO" or  data2 == "HELLO"}')
# print(f'not {data1} > "HELLO" : {not data1 > "HELLO"}')

print(f'{data1} > {data2} and {data1} == {data2} : {data1 > data2 and data1 == data2}')
print(f'{data1} < {data2} or {data1} == {data2} : {data1 < data2 or data1 == data2}')


# [실습 2] 정수 1개와 문자열 1개에 대한 논리 연산 수행 후  출력
#          단, not 연산자만 사용 
num1 = -3.2
num2 = 0 # 0 = False 

# print(f'not {num1} > 0 : {not num1 > 0}')
# print(f'not {num2} > 10 : {not num2 > 10}')

msg1 = '원더우먼' 
msg2 = '' # '' = Flase 

# print(f'not {msg1} > {msg2} : {not msg1 > msg2}')
# print(f'not {msg2} > {msg2} : {not msg2 > msg2}')

print(f'not {num1} : {not num1}')
print(f'not {msg1} : {not msg1}')

print(f'not {num2} : {not num2}')
print(f'not {msg2} : {not msg2}')