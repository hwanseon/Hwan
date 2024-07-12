# --------------------------------------------------------------
# 내장함수
# --------------------------------------------------------------
## 정수 관련 내장함수 
## 2진수(컴퓨터), 8진수, 10진수(사람), 16진수(프로그램)
## 숫자표현 
## [10진수] 0 ~ 9       0 1 2 3 4 5 6 7 8 9 10 11 ....... 19 20 21 ...
## [8진수]  0 ~ 7       0 1 2 3 4 5 6 7 10 11 12 ..... 17 20 ...
## [2진수]  0, 1        0 1 10 11 100 101 111 ....
## [16진수] 0 ~ 9, A ~ F, 0 1 2 3 4 5 6 7 8 9 A B C ... F 10 .... FF 100
# bin(정수) ==> 정수 -> 2진수 변환해주는 내장함수 ===> 0b2진수 str타입
print(4, bin(4), type(bin(4)))

# oct(정수) ==> 정수 -> 8진수 변환해주는 내장함수 ===> 0o8진수 str 타입
print(4, oct(4), type(oct(4)))
print(8, oct(8), type(oct(8)))

# hex(정수) ==> 정수 -> 16진수 변환해주는 내장함수 ===> 0x16진수 str 타입
print(4, hex(4), type(hex(4)))
print(8, hex(8), type(hex(8)))
print(17, hex(17), type(hex(17)))

# 16진수 ==> 10진수 변환해주는 내장함수 int()
print(int('0b10', base = 0))