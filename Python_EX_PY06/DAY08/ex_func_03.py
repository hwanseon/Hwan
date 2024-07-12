# -----------------------------------
# 사용자 정의 함수
# -----------------------------------
# [실습]
# 함수기능 : 원하는 단의 구구단을 출력해주는 기능 함수
# 함수이름 : gugudan()
# 매개변수 : num1
# 함수결과 : 없음
# -----------------------------------
def gugudan (num1) :
    for n in range(10) :
        if n == 0 :
            print(f"**[{num1} 단]**")
        else : 
            print(f'{num1:^2} * {n:^2} = {num1 * n}')
gugudan(8)
# -----------------------------------
# [실습]
# 함수기능 : 파일의 확장자를 변환해주는 기능 함수
# 함수이름 : FILE_NAME extract
# 매개변수 : str  FILE_NAME
# 함수결과 : 없음, 확장자 str
# -----------------------------------
def FILE_NAME (str) :
    name = str.split('.')
    print(name[-1])
FILE_NAME("2024 정보처리 기사 CBT.pdf")

def extract (FILE_NAME) :
    return FILE_NAME[FILE_NAME.rfind(".")+1 :]
FILE_NAME("2024 정보처리 기사 CBT.pdf")
