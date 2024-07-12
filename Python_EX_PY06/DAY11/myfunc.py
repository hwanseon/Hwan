def add (n1, n2) : return n1 + n2

print(__name__) # 메인이라고 표시해주는 것 (실행시키면 nmae => main으로 변경)
print("TEST")
print(f'add => {add(10, 3)}')

# # 현재 이 파일이 실행 중인 경우
if __name__ =='_u_main__' :
    print(__name__) 
    print("TEST")
    print(f'add => {add(10, 3)}')