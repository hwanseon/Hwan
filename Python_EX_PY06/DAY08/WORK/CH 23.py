# 2차원 리스트를 만들고 요소에 접근하기 p272
a = [[10, 20], [30, 40], [50, 60]]
print(a)
print(a[0][0], a[1][1], a[2][1], a[0][1])
a[0][1] = 1000
print(a[0][1])

from pprint import pprint 
pprint(a, indent=4, width=20) # indent 들여쓰기 칸 수, width = 가로 폭

## 반복문으로 2차원 리스트의 요소를 모두 출력
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a :
    print(x, y)
a = [[10, 20], [30, 40], [50, 60]]
for i in a : # i =[10, 20]
    for j in i : # j = 10, 20
        print(j, end = ' ')
    print()
from pprint import pprint 
a = [[10, 20], [30, 40], [50, 60]]
for i in range(len(a)) :
    for j in range(len[i]) :
        print(a[i][j], end = ' ')
    print()
