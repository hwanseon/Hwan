## 딕셔너리 사용하기 p143
lux = {'health':490, 'mana': 334, 'melee':550, 'armor':18.72}
print(lux)

lux = {'health':490, 'health': 334, 'melee':550, 'armor':18.72}
print(lux['health']) # 키 값이 중복되면 뒤에 값으로 저장

x = {100:'hundred', False:0, 3.5:[3.5, 3.5]} # 키 자리에는 리스트와 딕셔너리가 올 수 없음
print(x)

x = {} ; print(x, type(x))
y = dict() ; print(y, type(y))

lux1 = dict(health = 490, mana = 334, melee = 550, armor = 18.72)
print(lux1) # dict에서 키 = 값 형식은 '' or "" 사용 X

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print(lux2)

# 키 = 값을 list 안에 튜플 형식으로 나열
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)

# dict 안에서 {} => dict 생성
lux4 = dict({'health':490, 'health': 334, 'melee':550, 'armor':18.72})
print(lux4)

## 딕셔너리 키에 접근하기 p146
lux = {'health':490, 'mana': 334, 'melee':550, 'armor':18.72}
print(lux['health']) ; print(lux['armor'])

# 딕셔너리 값 변경 및 추가
lux['health'] = 2037 ; lux['mana'] = 1184
print(lux)
lux['mana_regen'] = 3.28 # 값이 추가됨
print(lux)

lux = {'health':490, 'mana': 334, 'melee':550, 'armor':18.72}
print('health' in lux) ; print('attack_speed' in lux)
print('health' not in lux) ; print('attack_speed' not in lux)
print(len(lux)) ; print(len({'health': 490, 'mana': 334, 'melee':550, 'armor':18.72}))

## p148
x = {10:'Hello', 'world':30}
print(x[10])

## 딕셔너리에 게임 캐릭터 능력치 저장하기
# keys = input().split()
# val = input().split()
# key = list(keys)
# vall = list(val)
# print(dict(zip(key, vall)))

## if 조건문 사용하기 p 157
x = 10
if x == 10 :
    print('10입니다.')

if x == 10:
    pass

if x == 10 :
    print('x에 들어있는 숫자는')
    print('10 입니다.')

x = 15
if x >=  10 :
    print('10 이상입니다')
if x == 15 :
    print('x는 15입니다.')
if x == 20 :
    print('20입니다.')

if x >=  10 :
    print('10 이상입니다')
    if x == 15 :
        print('x는 15입니다.')
    if x == 20 :
        print('20입니다.')

# 사용자가 입력한 값에 if 조건문 사용하기 p162
# x = int(input())

# if x == 10 :
#     print('10입니다.')
# if x == 20 :
#     print('20입니다.')

## 온라인 할인 쿠폰 시스템 만들기 p165
# price = int(input())
# coupon = input()

# if coupon[-4:] == '5000' :
#     print(price-5000)
# elif coupon[-4:] == '3000' :
#     print(price-3000)

## else 사용하기 p166
x = 5
if x == 10:
    print('10 이상입니다')
else :
    print('10이 아닙니다.')

x = 5
if x == 10 :
    y == x
else :
    y = 0
print(y)

# if, else 축약하기
x = 5
y = x if x == 10 else 0
print(y)

if x == 10 :
    rint('10 이상입니다')
else :
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.')

# if True :                  # 출력: 참
#     print('참')
# else :
#     print('거짓')

# if False :                 # 츨력: 거짓
#     print('참')  
# else :
#     print('거짓')

# if None :                  # 출력: 거짓
#     print('참')
# else :
#     print('거짓')

# if 조건문에 숫자 지정하기
if 0 :
    print('참')          # 출력: 거짓
else :
    print("거짓")

if 1 :                   # 출력: 참
    print('참')
else :
    print('거짓')

if 0x1F :                # 출력: 참
    print('참')
else :
    print('거짓')

if 0b1000 :              # 출력: 참
    print('참')
else :
    print('거짓')

if 13.5 :                # 출력: 참
    print('참')
else :
    print('거짓')

if 'Hello' :             # 출력: 참
    print('참')
else :
    print('거짓')

if '' :                  # 출력: 거짓
    print('참')
else : 
    print('거짓')

if not 0 :
    print('참')
if not None :
    print('참')
if not '' :
    print('참')

## 조건식을 여러 개 지정하기
x, y = 10, 20
if x == 10 and y == 20 :
    print('참')
else :
    print('거짓')

## 합격 여부 판단하기 p174
# jumsu = input().split()
# kor = int(jumsu[0]) ; eng = int(jumsu[1]) ; math = int(jumsu[2]) ; scien = int(jumsu[3])
# sum = kor + eng + math + scien

# if kor <= 100 and eng <=100 and math <= 100 and scien <= 100:
#     if sum/4 >= 80 :
#         print('합격')
#     else : 
#         print('불합격')
# else :
#     print("잘못된 점수")
# 1) 4과목 점수 입력 받기, 2) 4과목 점수 모두 0 ~ 100 검사 ==> 참: 합격/불합격 검사
#  input().split() => [str, str, str, str]
# int(nums[0]) in rang(101) 사용 가능
# [1] str 점수 4개 리스트 
jumsu = input().split()

# [2] str 점수 => int 점수 반환
jumsu = list(map(int, jumsu))  # 한번에 모두 형변환

# [3] 4과목의 점수를 0 ~ 100 범위 검사
if (0 <= int(jumsu[0]) <= 100) and (0 <= int(jumsu[1]) <= 100) and (0 <= int(jumsu[2]) <= 100) and (0 <= int(jumsu[3]) <= 100) :
    if (sum(jumsu) / len(jumsu)) >= 80 :
        print("합격")
    else :
        print('불합격')
else :
    print("잘못된 점수")

## if, elif, else를 모두 사용하기 p 178
x= 30

if x == 10:
    print('10입니다.')
elif x == 20 :
    print("20입니다.")
else :
    print("10도 20도 아닙니다.")

## 음료수 자판기 만들기 p178
# button = int(input())

# if button == 1 :
#     print("coke")
# elif button == 2 :
#     print('sprite')
# elif button == 3 :
#     print('hwan-ta')
# else :
#     print('제공하지 않는 메뉴')

## 교통카드 시스템 만들기 p180
age = int(input())

# if 7<= age <= 12 :
#     print(9000-650)
# elif 13<= age <= 18 :
#     print(9000-1050)
# elif age <= 6 :
#     pass
# else :
#     print(9000-1250)
balance = 9000
if age <= 6 :
    pass
elif 7 <= age <= 12 :
    balance = balance - 650
elif 13 <= age <= 18 :
    balance = balance - 1050
else :
    balance = balance - 1250
print(balance)