# ----------------------------------------------------
# 사용자 정의 함수
# ----------------------------------------------------
# ===> 만드는 사람 마음대로라서 이름이나 다 멋대로 하기
# 함수기능 : 2개 정수를 덧셈한 후 결과를 출력해주는 함수
# 함수이름 : add
# 매개변수 : 2개, num1, num2
# 함수 결과 (=return) : 없음 => 함수를 만들 때 반환값을 줄지말지도 스스로 결정해서 하면 됨
# ----------------------------------------------------
def add(num1, num2) :
    result=num1 + num2
    print(f'{num1} + {num2} = {result}')

# 함수 사용하기 즉, 호출 ----------
add(5,8)

# ----------------------------------------------------
# 함수기능 : 인사 메세지를 출력하는 함수
# 함수이름 : hello
# 매개변수 : 없음
# 함수 결과 (=return) : 없음 
# ----------------------------------------------------
def hello():
    print('Hello ~ ^^')

# 함수 사용하기 즉, 호출 ----------

hello()