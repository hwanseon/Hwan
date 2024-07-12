# 문제은행 중 메서드 안 푼 문제: 44 ~ 46, 53 ~ 55, 66 ~ 68
# 1 
print("Hello World")

# 2
print("Mary's cosmetics")

# 3
print('신씨가 소리질렀다. "도둑이야"')

# 4
print(R"C:Windows")

# 5
print("안녕하세요\n만나서\t\t반갑습니다.")
# \n: 줄바꿈, \t: 간격 설정(Tab)

# 6
print("오늘은", "일요일") # -> 오늘은 일요일

# 7
print('naver', 'kakao', 'sk', 'samsumg', sep = ';')

# 8
print('naver', 'kakao', 'sk', 'samsumg', sep = '/')

# 9 
print("first", end = " ") ; print("second")

# 10
print(f'5/3 => {5/3}')

# 11
samsungjunja = 50000
print(f'10주 보유 시 총 평가금액 = {samsungjunja * 10}')

# 12
siga, jooga, PER = 298, 50000, 15.79
print(f'시가 총액 : {siga}조, 현재가 : {jooga}원, PER : {PER}')

# 13 
s, t = 'hello', 'python'
print(s, "!", sep = '', end = " ") ; print(t) 

# 14
print(2 + 2 * 3) # -> 8

# 15
a= "132"
print(type(a)) # <class str>

# 16
num_str = "720"
print(int(num_str))

# 17
num = 100
print(str(num))

# 18
print(type(float(15.79)))

# 19
year = "2020"
year_int = int(year)
print(year_int+2, year_int+3, year_int+4)

# 20
air = 48584
print(f'에어컨 가격 : {air * 36}원')

# 21
letters = 'python'
print(letters[0], letters[2])

# 22
license_plate = "24가 2210"
print(license_plate[-4:])

# 23
string = "홀짝홀짝홀짝"
print(string[::2])

# 24
string = "PYTHON"
print(string[::-1])

# 25, 26
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))
print(phone_number.replace("-", ""))

# 27
url = "http://sharebook.kr"
print(url[-2:])
url2 = url.split(".")
print(url2[1])

# 28
# lang = 'python'
# lang[0] = 'P'
# print(lang) # -> ERROR

# 29
string = 'abcdfe2a354a32a'
A = string.replace("a", "A")
print(A)

# 30
string = 'abcd'
string.replace('b', 'B')
print(string) # -> abcd
print(string.replace('b', 'B')) # -> aBcd

# 31
a = "3"
b = "4"
print(a + b) # -> 34

# 32
print("Hi" * 3) # -> HiHiHi

# 33
print("-"*80)

# 34
t1 = 'python'
t2 = 'java'
t3 = t1 + " " + t2 + " "
print(t3*4)

# 35, 36, 37
name1, age1 = "김민수", 10
name2, age2 = "이철희", 13
print(f'이름 : {name1} 나이 : {age1}\n이름 : {name2} 나이 : {age2}', "\n")
print(f'이름 : %s 나이 : %d\n이름 : %s 나이 : %d' % (name1, age1, name2, age2), "\n")
print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2), "\n")

# 38
sangjang = "5,969,782,550"
sangjang = sangjang.replace(",","")
print(int(sangjang))

# 39
boongi = "2020/03(E) (IFRS연결)"
print(boongi[:7])

# 40
data = "   삼성전자    "
print(data.strip())

# 41 42
ticker = "btc_krw"
print(ticker.upper())
ticker = "BTC_KRW"
print(ticker.lower())

# 43
a = "hello"
print(a.capitalize())

# 47 
a = "hello world"
print(a.split())

# 48
ticker = "btc_krw"
print(ticker.split("_"))

# 49
date = "2020-05-01"
year = date.split("-")[0]
month = date.split("-")[1]
day = date.split("-")[2]
print(f"년도: {year}년, 달: {month}월, 일: {day}일")

# 50
data = "039490     "
print(data.rstrip())

# 51 52
movie_rank = ["닥더 스트레인지", "스플릿", "럭키"]
print(movie_rank)
movie = ["배트맨"]
print(movie_rank + movie)

# 56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 57
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'max : {max(nums)}')
print(f'min : {min(nums)}')

# 58
nums = [1, 2, 3, 4, 5]
print(f'합계 : {sum(nums)}')

# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(f'cook data의 개수 : {len(cook)} 개')

# 60
nums = [1, 2, 3, 4, 5]
print(f'nums의 평균 : {sum(nums)/len(nums)}')

# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 62 63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'홀수 : {nums[::2]}')
print(f'짝수 : {nums[1::2]}')

# 64
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 69
string = "삼성전자/LG전자/Naver"
data = string.split("/")
print(list(data))

# 70
data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data))

# 71
my_variable = () ; print(f'my_variable 튜플 : {my_variable}')

# 72
movie_rank = ("닥더 스트레인지", "스플릿", "럭키")
print(movie_rank )

# 73
num = 1, ; print(num, type(num))

# 74
# t = (1, 2, 3)
# t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# 오류발생 원인: 튜플은 요소/원소 값 수정 불가

# 75
t = 1, 2, 3, 4
print(type(t)) # -> 결과 값: 튜플

# 76
t = ('a', 'b', 'c')
T =  ('A', 'b', 'c')
print(T, type(T))

# 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest, type(interest))

# 78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest), type(tuple(interest)))

# 79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c) # a = apple, b = banana, c = cake

# 80
num = range(2, 100, 2)
num_t = tuple(num)
print(num_t)