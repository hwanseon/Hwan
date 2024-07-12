# -----------------------------------------------------------------
# str data type 전용 함수 즉, 메서드 살펴보기
# -----------------------------------------------------------------
msg = "Hello 0705"

# [요소/원소 인덱스 찾기 메서드 - fine(문자 1개 or 문자열)]
# ==> 존재하지 않으면 -1 반환
# - 'H'의 인덱스 
idx = msg.find('H')
print(f'H의 인덱스 : {idx}')
# - '7'의 인덱스 
idx = msg.find('7')
print(f'7의 인덱스 : {idx}')
# - 'llo'의 인덱스 
idx = msg.find('llo')
print(f'llo의 인덱스 : {idx}') # 문자열의 시작 위치의 인덱스를 뽑아줌
# - 'llO'의 인덱스   ===> 대소문자 일치, 문자열이 존재하지 않으면 -1 반환 
idx = msg.find('llO') 
print(f'llO의 인덱스 : {idx}')

# [요소/원소 인덱스 찾기 메서드 - index(문자 1개 or 문자열)]
# ==> 존재하지 않으면 ERROR 발생
# - 'H'의 인덱스
idx = msg.index('H')
print(f'H의 인덱스 : {idx}')
# - 'h'의 인덱스 : 존재하지 않으면 ERROR 발생
# idx = msg.index('h')
# print(f'h의 인덱스 : {idx}')
if 'h' in msg:
    idx = msg.index('h')
    print(f'h의 인덱스 : {idx}')
else :
    print("'h'는 존재하지 않습니다.")
# 문자열에 동일한 문자가 여러개 존재하는 경우
msg = "Good Luck Good"
# # - 'o'의 인덱스 찾기 => 1) 첫번째 'o' 인덱스
# # ==> "Good Luck Good"
# idx = msg.fine('o')
# print(f'o의 인덱스 : {idx}')
# # - 'o'의 인덱스 찾기 => 2) 두번째 'o' 인덱스
# # ==> "od Luck Good"
# idx = msg.fine('o', idx+1)
# print(f'두번째 o의 인덱스 : {idx}')
# # - 'o'의 인덱스 찾기 => 3) 세번째 'o' 인덱스
# # ==> "d Luck Good"
# idx = msg.fine('o', idx+1)
# print(f'세번째 o의 인덱스 : {idx}')
# # - 'o'의 인덱스 찾기 => 4) 네번째 'o' 인덱스
# # ==> " Luck Good"
# idx = msg.fine('o', idx+1)
# print(f'네번째 o의 인덱스 : {idx}')

## 반복문 사용
cnt = msg.count('o') ; print(f'cnt = > {cnt}')
idx = -1 # 밑에서 +1을 해주기 때문에 초기값은 0이 되어야 해서 -1부터 시작
for n in range(cnt) :
    idx = msg.find('o', idx+1)
    print(f'{n+1}번째 o의 인덱스 : {idx}')

# --------------------------------------------------
# [문자열의 뒷부분부터 인덱스를 찾는 메서드 - rfind(문자, start index, end index+1)
#                                        - rindex(문자, start index, end index+1)
# --------------------------------------------------
msg = "Happy"
#      01234
# 'y' index 찾기
idx = msg.rfind('y')
print(f'y index => {idx}')
# 첫번째 'p' index 찾기  ====> 뒷 문자의 인덱스를 먼저 반환 
# "Happy"
idx = msg.rfind('p')
print(f'p index => {idx}') 
# 두번째 'p' index 찾기 
# "Hap" 
idx = msg.rfind('p', 0, idx) # ===> 범위지정 
print(f'p index => {idx}') 

# 파일명에서 확장자 txt, jpeg, xlsx, zip, gz 찾기
# 파일명 : hello.txt  ===>  뒤에서부터 찾는 것이 빠름
# 파일명 : 2024상반기경제분석.doc
# .을 찾고 .의 인덱스 + 1 부터 끝까지 
files = ['hello.txt', '2024상반기경제분석.doc', 'kakako_123456789.jpg']
for f in files :
    dot_index = f.find(".")
    print(f[dot_index:])


for n in files : 
    name = n.split('.')
    print(name[-1])
