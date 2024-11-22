# [실습 1] 데이터 저장 및 변수 생성 출력 
# - 생년월일
# - 띠 (용, 범)
# - 혈액형
# - 출력형태
#   나는 0000년 00월 00일 000띠 입니다
# 혈액형은 ___형 입니다
#  ----------------------------

# 데이터 저장
year = 2000
month = "08"
day = "05"
animal = "dragon"
blood = " A"

# 출력
print(f"나는 {year}년 {month}월 {day}일 {animal} 띠 입니다.")
print(f"혈액형은 멋진 {blood}형 입니다")

# [실습 2] 입력 받은 데이터 저장 단, 파일로 저장 
# - 좋아하는 계절
# - 좋아하는 나라
# - 여행가고 싶은 나라 
# -------------------------------
season = input("좋아하는 계절 : ").strip()
nation = input("좋아하는 나라 : ").strip()
trip = input("여행가고 싶은 나라 : ").strip()

FILENAME = "info.txt"
f = open(FILENAME, mode = "w", encoding = 'utf-8')

f.write(season)
f.write('\n') # 줄바꿈 문자
f.write(nation)
f.write('\n') # 줄바꿈 문자
f.write(trip)
f.write('\n') # 줄바꿈 문자

# f.close()

print(f"좋아하는 계절 : {season}", file = f)
print(f"좋아하는 나라 : {nation}", file = f)
print(f"여행가고 싶은 나라 : {trip}", file = f, end = "")

f.close()
