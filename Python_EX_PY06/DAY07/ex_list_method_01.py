# ------------------------------------------------
# 리스트 전용의 함수 즉, 메서드 (Method)
# - 리스트 원소/요소를 제어하기 위한 함수
# ------------------------------------------------
import random as rad

# [1] 실습 데이터 => 임의의 정수 숫자 10개로 구성된 리스트 
datas = [1, 2, 3, 4, 5, 6, 7,8, 9, 10]

# [메서드 - 요소 인덱스를 반환하는 메서드 index()]
# -> 요소 7의 인덱스 찾기
# -> 왼쪽 >>>>> 오른쪽으로 찾아줌 
idx = datas.index(7)
print(f'7의 인덱스 : {idx}')

# list안에 없는 data 인덱스 찾기 ==> 존재하지 않는 data 경우 ERROR 
if 0 in datas: 
    idx = datas.index(0)
    print(f'0의 인덱스 : {idx}') 
else :
    print('0은 존재하지 않는 data')

datas = [1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10, 3]
# list안에 증복되는 값이 존재하는 경우, 3의 인덱스 찾기
if 3 in datas :
    idx = datas.index(3)
    print(f'3의 인덱스 : {idx}') # 중복되는 data 중에서 제일 첫번째 값을 찾아줌

# 인덱스 범위 지정 
if 3 in datas :
    idx = datas.index(3, idx+1)
    print(f'첫번째 3의 인덱스 : {idx}')

    idx = datas.index(3, idx+1)
    print(f'두번째 3의 인덱스 : {idx}')

    # idx = datas.index(3, idx+1)
    # print(f'세번째 3의 인덱스 : {idx}')

## 형식 : index(데이터, 찾기 시작 인덱스 지정)

# [메서드 : 데이터가 몇개 존재하는지 갯수 파악 메서드] ==> count(데이터)
## 3의 갯수 찾기
cnt = datas.count(3)
print(f'3의 개수 : {cnt}개')
idx = 0
for i in range(cnt) :
    idx = datas.index(3, idx if not i else idx + 1)
    print(f'{i+1}번째 3의 인덱스 : {idx}')