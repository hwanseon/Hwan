# ------------------
# 연산자 
# ------------------
# [3] 논리연산자 
# - 종류: and, or, not
# - 특징: 여러개의 경우에 대한 결과를 바탕으로 결론 도출
# - and : 결과 1 and 결과 2 and 결과 3 => 결과 1~3 모두 True => 결과값: True

num1 = 8
num2 = 3

print(f'{num1} > 0 and {num2} > 0 : {num1 > 0 and  num2 > 0}')
print(f'{num1} > 0 and {num2} == 0 : {num1 > 0 and  num2 == 0}')

# - or: 결과 1 or 결과 2 or 결과 3 => 결과 1~3 중 1개 이상 True => 결과값: True

print(f'{num1} > 0 or {num2} > 0 : {num1 > 0 or  num2 > 0}')
print(f'{num1} > 0 or {num2} == 0 : {num1 > 0 or  num2 == 0}')
print(f'{num1} == 0 or {num2} == 0 : {num1 == 0 or  num2 == 0}')


# - not : not 결과
#         결과에 반대로 결론 도출
#         True => False, False => Ture로 결론 

print(f'not {num1} > 0 : {not num1 > 0}')
print(f'not {num1} == 0 : {not num1 == 0}')
