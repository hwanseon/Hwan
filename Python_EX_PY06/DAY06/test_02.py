# ----------------------------------
# [실습] 10번의 숫자 데이터를 입력 받음
#  - 숫자 데이터를 모두 더해서 합계가 30 이상이 되면, 10번 입력이 되지 않더라도 종료
# ----------------------------------
sum = 0

for i in range(1, 11) :
    i = int(input(f"{i}번 데이터 입력 : "))
    sum = i + sum
    if sum >= 30 :
        break
print(f"입력한 숫자의 합 = {sum}")