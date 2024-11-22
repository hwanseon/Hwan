# 문제은행 중 메서드 안 푼 문제: 44 ~ 46, 53 ~ 55, 66 ~ 68

# 44, 45
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))
print(file_name.endswith('xlsx' or 'xls'))

# 46
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 53, 54, 55
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)
movie_rank.remove("럭키")
print(movie_rank)
movie_rank.remove("스플릿") ; movie_rank.remove("배트맨")
print(movie_rank)

# 66, 67, 68
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))

# 81, 82, 83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)
_, _, *valid_score = scores ; print(valid_score)
_, *valid_score, _ = scores ; print(valid_score)

# 84, 85, 86
temp = {}
temp.update(메로나 = 1000, 폴라포 = 1200, 빵빠레 = 1800) ; print(temp)
temp.update(**{"죠스바":1200, "월드콘":1500}) ; print(temp)

# 87, 88, 89
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(f'메로나 가격 : {ice["메로나"]}')
ice["메로나"] = 1300 ; print(ice)
del ice['메로나'] ; print(ice)

# 90
# dict에 없는 값을 인덱싱 

# 91, 92, 93, 94
inventory = {"메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]} ; print(inventory)
print(inventory["메로나"][0], "원")
print(inventory["메로나"][-1], "개")
inventory.update(월드콘 = [500, 7]) ; print(inventory)

# 95, 96, 97
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys()) ; print(ice)
cream = list(icecream.values()) ; print(cream)
hap = 0
for c in cream :
    hap = c + hap
print(hap)

# 98
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price)) ; print(close_table)

# 101, 102, 103, 104, 105, 106, 107, 108
# bool
# Flase
# True
# True
# True
# "" or '' 없음
# 아무것도 출력 X
# Hi, there.

# 109
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 1\n2\n4

# 110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# 3\n5

# 111
# msg = input()
# print(msg*2)

# 112
# num = int(input("숫자를 입력하세요 : "))
# print(num+10)

# 113
# num = int(input())
# print("짝" if not num%2 else "홀" )

# 114
# num = int(input("입력값 : "))
# if num + 20 > 255 :
#     print("출력값 : 255")
# else :
#     print(f'출력값 : {num+20}')

# 115
# num = int(input("입력값 : "))

# if num - 20 < 0 :
#     print(f'출력값 : 0')
# elif num - 20 > 255 :
#     print(f'출력값 : 255')
# else :
#     print(f'출력값 : {num - 20}')

# 116
# clock = input("현재 시간  ex) 10:15 : ").split(":")
# if clock[-1] == "00" :
#     print("정각 입니다.")
# else :
#     print("정각이 아닙니다.")

# 117
# fruit = ["사과", "포도", "홍시"]
# favorite = input("좋아하는 과일은 ? ").strip()
# if favorite in fruit : print("정답입니다.")
# else : print("오답입니다.")

# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# data = input("종목명 : ").split()
# if data in warn_investment_list : print("투자 경고 종목입니다.")
# else : print("추자 경고 종목이 아닙니다.")

# 119, 120
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# season = input("좋아하는 계절은 ? ").strip()
# if season in fruit : print("정답입니다.")
# else : print("오답입니다.")
# like = input("좋아하는 과일은 ? ").strip()
# if like in fruit.values() : print("정답입니다.")
# else : print("오답입니다.")

# 121
# alpha = input().strip()
# if "a" <= alpha <= "z" :
#     print(alpha.upper())
# else : print(alpha.lower())

# 122 
# score = int(input("score : "))
# if 81 <= score <= 100 : print('grade is A')
# elif 61 <= score <= 80 : print('grade is B')
# elif 41 <= score <= 60 : print('grade is C')
# elif 21 <= score <= 40 : print('grade is D')
# else : print('grade is E')

# 123
# won = input("입력 : ").split()
# if won[-1] == "달러" :
#     won = float(won[0])
#     print(f'{won * 1167} 원')
# elif won[-1] == "엔" :
#     won = float(won[0])
#     print(f'{won * 1.0967} 원')
# elif won[-1] == "유로" :
#     won = float(won[0])
#     print(f'{won * 1268} 원')
# else :
#     print(f'{won * 171} 원')

#124
# i = 1
# num1 = int(input(f"number{i} : "))
# num2 = int(input(f"number{i+1} : "))
# num3 = int(input(f"number{i+2} : "))
# print(max(num1, num2, num3))

# 125
# number = input("휴대전화 번호 입력: ")
# num = number.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")

# # 126
# jooso = input("우편번호 : ")
# if '010' <= jooso[:3] <= '012' :
#     print("강북구")
# elif '013' <= jooso[:3] <= '015' :
#     print("도봉구")
# else :
#     print("노원구")

# 127, 128
# joomin = input("주민등록번호 : ").split("-")
# if joomin[-1][0] == "1" or joomin[-1][0] == "3" :
#     print("남자")
# else : print("여자")
# if "00" <= joomin[-1][1:3] <= "08" :
#     print("서울 입니다.")
# else : print("서울이 아닙니다.")

# 129
# joomin = input("주민등록번호 : ").replace("-", '')
# joomin = list(joomin) 
# idx = 2
# for jj in joomin :
#     jj = int(jj)
#     gob = jj * idx
#     gob = gob + gob
#     idx += 1
#     if idx == 10 :
#         idx = 2
# if not 11 - (gob % 11) == int(joomin[-1]) :
#     print("유효하지 않은 주민등록번호 입니다.")

# # 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# range = float(btc["max_price"]) - float(btc["min_price"])
# siga = float(btc["opening_price"])
# maxx = float(btc["max_price"])

# if (siga + range) > maxx :
#     print("상승장")
# else :
#     print("하락장")

# 131, 132
# ["사과", "귤", "수박"]
# print('####')가 3번 반복

# 133, 134, 135
print("A") ; print('B') ; print('C')
print("출력 : ","A") ; print("출력 : ",'B') ; print("출력 : ",'C')
print("출력 : ","a") ; print("출력 : ",'b') ; print("출력 : ",'c')

# 136, 137, 138, 139
aa = [10, 20, 30]
for a in aa :
    print(a)
for b in aa :
    print(b)
    print("-"*6)
print("+"*4) 
for c in aa : print(c)

# 140
for i in range(4) :
    i = "-"
    print(i*6)

# 141
price = [100, 200, 300]
for p in price :
    print(p + 10)

# 142
food = ["김밥", "라면", "튀김"]
for fo in food :
    print(f"오늘의 메뉴 : {fo}")

# 143
compa = ["SK하이닉스", "삼성전자", "LG전자"]
for com in compa :
    print(len(com))

# 144, 145
animal = ['dog', 'cat', 'parrot']
for ani in animal :
    print(f"{ani} {len(ani)}")
for ani in animal :
    print(ani[0])

# 146, 147
nums = [1, 2, 3]
for n in nums :
    print(f"3 X {n}")
for n in nums :
    print(f"3 X {n} = {3*n}")

# 148, 149, 150
korean = ["가", "나", "다", "라"]
for kor in korean :
    if kor == "가" : 
        continue
    print(kor)

for kor in korean[::2]:
    print(kor)

for kor in korean [::-1]:
    print(kor)

# 151
nums = [3, -20, -3, 44]
for n in nums :
    if n < 0 :
        print(n)

# 152
nums = [3, 100, 23, 44]
for n in nums :
    if not n % 3 : print(n)

# 153
nums = [13, 21, 12, 14, 30, 18]
for n in nums :
    if n < 20 and n%3 == 0 :
        print(n) 

# 154
msg = ["I", "study", "python", "language", "!"]
for m in msg :
    if len(m) >= 3 :
        print(m)

# 155, 156
msg = ["A", "b", "c", "D"]
for m in msg :
    if "A" <= m <= "Z" :
        print(m)
for m in msg :
    if "a" <= m <= "z" :
        print(m)

# 157
animal = ['dog', 'cat', 'parrot']
for ani in animal :
    print(ani.capitalize())

# 158
name = ['hello.py', 'ex01.py', 'intro.hwp']
for na in name :
    na = na.split(".")
    print(na[0])

# 159
name = ['intra.h', 'intra.c', 'define.h', 'run.py']
for na in name :
    na = na.split(".")
    if na[-1] == "h" :
        print(na[0]+"."+na[-1]) 

# 160
for na in name :
    nam = na.split(".")
    if nam[-1] == "h" or nam[-1] == "c" :
        print(na)

# 161 
for i in range(100) :
    print(i, end = " ")

# 162
for w in range(2002, 2051, 4) :
    print(w)

# 163
for t in range(1, 31, 3) :
    print(t)

# 164
for d in range(100) :
    print(99-d)

# 165
for f in range(10) :
    print("0.", f, sep='')

# 166, 167
for i in range(1, 10) :
    print(F"3 X {i} = {3*i}")
for i in range(1, 10, 2) :
    print(F"3 X {i} = {3*i}")

# 168
sum = 0
for i in range(11) :
    sum += i
print(sum)

# 169
sum = 0
for i in range(1,11,2) :
    sum += i
print(sum)

# 170
gob = 1
for i in range(1,11,2) :
    gob = i * gob
print(gob)

# 171, 172, 173, 174
price_list = [32100, 32150, 32000, 32500]
for price in range(len(price_list)) :
    print(price_list[price])
for price in range(len(price_list)) :
    print((price), price_list[price])
for price in range(len(price_list)) :
    print(3 - price, price_list[price])
for price in range(1, len(price_list)) :
    print((price*10)+90, price_list[price])

# 175
# my_list = ["가", "나", "다", "라"]
# for m in range(len(my_list)-1) :
#     print(my_list[m], my_list[m+1])

# 176
my_list = ["가", "나", "다", "라", "마"]
for m in range(1, len(my_list)-1) :
    print(my_list[m-1], my_list[m], my_list[m+1])

# 177
my_list = ["가", "나", "다", "라"]
for m in range(len(my_list)-1) :
    print(my_list[3 - m], my_list[ 2- m])

# 178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1) :
    print(my_list[i + 1] - my_list[i])

# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(1, len(my_list)-1) :
    hap = my_list[i-1] + my_list[i] + my_list[i+1]
    print(hap/3)

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []

for i in range(len(low_prices)) :
    minus = high_prices[i] - low_prices[i]
    volatility.append(minus)

print(volatility)

# 181
apt1 = ["101호", "102호"]
apt2 = ["201호", "202호"]
apt3 = ["301호", "302호"]
apt = [apt1] + [apt2] + [apt3]
print(apt)

# 182, 183
siga = [100, 200, 300]
jonga = [80, 210, 330]
total = [siga] + [jonga]
print(total)

stock = {}
stock.update(zip(siga, jonga))
print(stock)

# 184
stock = {"10/10":[80, 110, 70, 90], "10/11":[210,230,190,200]}

# 185, 186, 187, 188, 189, 190
apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart :
    for aa in a :
        print(aa, "호")

apart.sort(reverse = True)
for a in apart :
    for aa in a :
        print(aa, "호")

apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart[::-1] :
    for aa in a[::-1] :
        print(aa, "호")

apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart :
    for aa in a :
        print(aa, "호")
        print("-----")

apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart :
    for aa in a :
        print(aa, "호")
    print("-----")

apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart :
    for aa in a :
        print(aa, "호")
print("-"*5)

# 191, 192, 193, 194
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for d in data :
    for dd in d :
        print(dd*1.00014)

result = []
for d in data :
    for dd in d :
        result.append(dd*1.00014)
    # print("-"*4)
print(result)

result = []
for d in data :
    rresult = []
    for dd in d :
        rresult.append(dd*1.00014)
    result.append(rresult)
print(result)

# 195, 196, 197, 198, 199, 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for o in ohlc[1:] :
    print(o[3])

for o in ohlc[1:] :
    if (o[3] > 150):
        print(o[3])

for o in ohlc[1:] :
    if (o[3] >= o[0]) :
        print(o[3])

volatility = []
for o in ohlc[1:] :
    volatility.append(o[1] - o[2])
print(volatility)

for o in ohlc[1:] :
    if o[3] > o[0] :
        print(o[1] - o[2])

hap = 0
for o in ohlc[1:] :
    money = o[3] - o[0]
    hap += money
print(hap)

# 201, 202, 203
# def print_coin() :
#     print("비트코인")
# print_coin()
# for n in range(100) :
#     print_coin()

# 204
def print_coins() :
    for _ in range(100) :
        print("비트코인")

# print_coins()

# 205, 206, 207, 208, 209, 210
# 함수 정의 전 호출
# A \n B \n C \n A \n B
# A \n C \n B
# A \n C \n B \n E \n D
# B \n A
# B \n C \n B \n C \n B \n C \n A

# 211, 212, 213, 214
# 안녕 \n Hi
# 7, 15
# ()가 비어있음 => 비어있는 걸 하고 싶으면 정의할때도 비게 해야함
# 문자열과 int를 더해야해서

# 215, 216
def print_with_smile(msg) :
    print(msg + ":D")

print_with_smile("안녕하세요")

# 217
def print_upper_price(price) :
    price = int(price)
    print(price*1.3)

# 218
def print_sum(num1, num2) :
    print(num1 + num2)

# 219
def print_arithmetic_operation(a,b) :
    a = int(a) ; b = int(b)
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

# 220
def print_max (a, b, c) :
    a = int(a) ; b = int(b) ; c = int(c)
    if a > b and a > c :
        print(a)
    elif b > a and b > c :
        print(b)
    else :
        print(c)

print_max(9, 10, 40)

# 221
def print_reverse(mag) :
    print(msg[::-1])

# 222
def print_score(score_list) :
    print(sum(score_list)/len(score_list))

# 223
def print_even(nums_list) :
    for n in nums_list :
        if not n % 2 : print(n)
    
print_even([1, 3, 2, 10, 12, 11, 15])

# 224
def print_keys(msg_dict) :
    print(msg_dict.keys())

print_keys({"이름":"김말똥", "나이":30, "성별":0})

# 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key (my_dict, key) :
    print(my_dict[key])
print_value_by_key (my_dict, "10/26")

# 226
# def print_5xn(line) :
#     chunk_num = int(len(line)/5)
#     for x in range(chunk_num+1) :
#         print(line[x * 5 : x * 5 + 5])

# print_5xn("아이엠어보이유알어걸")

# 227
# def print_mxn(line, num) :
#     chunk_num = int(len(line) / num)
#     for x in range(chunk_num+1) :
#         print(line[x * num : x * num + num])

# print_mxn("아이엠어보이유알어걸")
