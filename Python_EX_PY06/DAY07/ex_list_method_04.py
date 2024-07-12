# -----------------------------------------------
# 리스트 전용의 함수 즉, 메서드 (Method)
# - 리스트 원소/요소를 제어하기 위한 함수
# -----------------------------------------------
datas = [11, 22, 33]
nums = datas # list의 주소를 datas와 num가 같이 가짐
print(f'datas ==> {datas}\nnums => {nums}')

nums[0] = '백'
print(f'datas ==> {datas}\nnums => {nums}')

## 메서드 - 리스트를 복사해주는 메서드 copy()
# 얕은 복사임 ===> 깊은 복사는 모듈 추가를 해야함 
nums2 =datas.copy()
nums2[0] = 'A'
print(f'datas ==> {datas}\nnums => {nums}')
