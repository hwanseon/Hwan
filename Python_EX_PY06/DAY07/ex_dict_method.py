# ------------------------------------------------
# Dict 전용 함수 즉, 메서드
# -> keys(), values(), items()
# ------------------------------------------------
person = {'name':'홍길동', 'age': 40}

## [메서드 - 값 읽어오는 메서드 get(key, default)]
## ==> key에 해당하는 값이 없으면 default값 반환하도록 설정
## ==> default 값에 아무것도 입력이 되지 않았는데 key 값이 없으면 None 출력
print(person['name'])
# print(person['gender']) KeyError 발생 (없는 키 입력 시)

print(person.get('name'))
print(person.get('gender')) # 없으면 None 출력
print(person.get('gender', "없"))

# [메서드 키와 값 추가 메서드]
person['gender'] = 'M'

# 알파벳 별로 갯수 카운트
msg = "Hello Good Luck"
# 1) set 중복 제거 2) 개수 카운트 
alpha = set(msg)
print(alpha)
for m in alpha :
    print(m, msg.count(m), end = ' ')

alpha = set(msg)
save = {}
for m in alpha :
    print(m, msg.count(m), end = ' ')
    print()
    save[m] = msg.count(m)

## [메서드 - 수정 및 업데이트 메서드 update(key = value)]
## ====> 수정 및 추가 가능 
## key 값이 str이라도 '' or "" 금지
person['gender'] = 'F'

person.update(genfer ='어린이')
print(person)

person.update(genfer ='어린이', job = '학생')
print(person)

person.update( {'phone' : '010', 'birth':'240101'})
print(person)

## **{'weight':100, 'height':170} ==> weight = 100, heigh = 170으로 자동으로 바꿔줌
person.update( **{'weight':100, 'height':170})
print(person)