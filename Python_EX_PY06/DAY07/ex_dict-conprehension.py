# ----------------------------------------------
# List/Set/Dict 자료형과 반복문, 조건브표현식 결합
# - 메모리 사용량 감소 & 속도 향상
# conprehensions ==> 대량의 data 처리 시 사용 
# ----------------------------------------------
keys = ['a', 'b', 'c', 'd']

x = {key : value for key, value in dict.fromkeys(keys).items()}
# dict.fromkeys(keys).items() ==> 'a':None, 'b' :None, 'c':None에서
# item으로 뽑으면 ('a',None) ('b',None) ('c',None)
print(x)