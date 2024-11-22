# -------------------------------------------------------
# ==> 1줄로 조건식을 축약 : 조건부 표현식
# -------------------------------------------------------
# [실습] 문자 1개 코드값을 지정하는 조건식을 작성
## - 알파벳(a~z, A~Z) code 값으로 변환
## - 그 외는 None으로 코드값 변환
data = 'm'
# result = None
if ('a' <= data <= 'z') or ('A' <= data <= 'Z') :
    print(ord(data))
    # result = ord(data)
else :
    print(None)
    # result(None)
# print(result)

# 조건부 표현식
print(ord(data)) if ('a' <= data <= 'z') or ('A' <= data <= 'Z') else print(None)

# 결과를 변수로 지정
result = ord(data) if ('a' <= data <= 'z') or ('A' <= data <= 'Z') else print(None)
print(f'{data}의 코드값 : {result}')