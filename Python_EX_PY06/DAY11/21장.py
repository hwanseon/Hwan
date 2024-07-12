import turtle as t
t.shape('turtle')
# t.forward(100)
# t.rt(90)
# t.forward(100)
# t.rt(90)
# t.forward(100)
# t.rt(90)
# t.fd(100)

# 4각형 그리기 
# for i in range(4) :
#     t.fd(100)
#     t.rt(90)

# 5각형 그리기
# for i in range(5) :
#     t.fd(100) 
#     t.rt(360/5)

# n = int(input())
# for i in range(n) :
#     t.fd(100)
#     t.rt(360/n)

# t.color('red')
# t.begin_fill()
# for i in range(5) :
#     t.fd(100) 
#     t.rt(360/5)
# t.end_fill()

# 원 그리기
# t.circle(120) # 반지름
# n = 60
# t.speed('fastest') # 거북이 속도를 가장 빠르게
# for i in range(n) :
#     t.circle(120)
#     t.rt(360/n)

# n = 60
# t.speed('nomal') # 거북이 속도를 가장 느리게 = slowest
# for i in range(n) :
#     t.circle(120)
#     t.rt(360/n)

# t.speed("fastest")
# for i in range(300) :
#     t.forward(i) 
#     t.rt(91)

# 연습문제 : 오각별 그리기 p240
# n = 5
# for i in range(n) :
#     t.fd(100)
#     t.rt((360/n)*2)
#     t.fd(100)
#     t.left(360/n)
# t.mainloop()

# 심사문제 : 별 그리기 p239
n = input()
cnt, line = n.split()
cnt, line = int(cnt), int(line) 
for c in range(cnt) :
    t.fd(line)
    t.rt((360/cnt)*2)
    t.fd(line)
    t.lt(360/cnt)

t.mainloop()
