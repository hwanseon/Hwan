# -----------------------------------
# 사용자 정의 함수
# 매개변수가 가변인자인 경우 (들어오는 data 타입이 다를떄)
# -----------------------------------
# 매개변수에 전달되는 데이터가 지정되지 않는 경우
# - 어떤 종류의 data가 들어오는지 = 값 ==> dict 형태
# ============> 키워드 파라미터(키워드 매개변수)
# 형식 def 함수명 (**params) => 키 = 값
# -----------------------------------
# 함수 기능: 회원가입의 기능 함수
# 함수 이름: register
# 매개변수: 가입자마다 입력하는 정보가 모두 다름 **params
# 함수결과: 가입메시지 str
# -----------------------------------
def register(**params) :
    print(type(params))
register(name = "김환선", job = "학생")
register(id = "master", age = 10, gender =  "M")
register()
# ===============> 누군 뭐 입력, 누군 뭐 입력 통일성이 없음

# -----------------------------------
# 함수 기능: 회원가입의 기능 함수
# 함수 이름: register2
# 매개변수: 필수 입력 사항 id, pw, email
#           선택 입력 사항  **params
# 함수결과: 가입메시지 str
# -----------------------------------
def register2(id, pw, email,**params) :
    print(type(params))

# register2("Hong", "j789im", "h@nate.com", 'F') # 키 값이 없어서 ERROR
register2("Hong", "j789im", "h@nate.com", gender = 'F')
# register2("Hong", "j789im") # 키 값 부족 => ERROR 