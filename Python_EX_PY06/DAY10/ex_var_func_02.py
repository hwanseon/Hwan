# ----------------------------------------------------
# 함수와 변수 - 지역/전역 변수
# ----------------------------------------------------
## 전역변수 -------------------------
persons = ["홍"] 
gender = {'H':"남자"}
year = 2024

## 사용자 정의 함수
def add_person(name) :
    global year
    year += 1
    persons.append(name)
    gender[name] = '여'

def remove_person(name) :
    persons.remove(name)
    gender.pop(name)

# 함수 호출 ------------------------------------------
print(f'persons => {persons}')

add_person("Park")  # 리스트는 global 변수명을 안해도 값 추가 가능
print(f'persons => {persons}')

print(f'persons => {persons}')
print(f'gender => {gender}')

remove_person("Park")

print(f'persons => {persons}')
print(f'gender => {gender}')