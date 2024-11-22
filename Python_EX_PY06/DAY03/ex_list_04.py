# ----------------------------------------
# List 데이터 자료형 살펴보기
#  - list와 str
# ----------------------------------------
msg = "Happy"

# str => list 형변환
datas = list(msg) # 문자열을 주면 문자 하나하나를 다 쪼갬 (하나하나가 다 원소라서)
print(datas)

msg = ['Happy'] # 이 자체가 원소 
datas = list(msg)
print(datas) # 쪼개지지않음

# + 메모장 참고