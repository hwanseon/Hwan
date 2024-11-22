mabangjin = int(input("홀수차 배열의 크기를 입력하세요 : "))

# 3, 5, 7, 9인지 확인하는 함수
def holsu () :
    if mabangjin in [3, 5, 7, 9] : 
        print("Magic Square", f"({mabangjin}x{mabangjin})")

    else :
        print("3, 5, 7, 9 중에 하나의 숫자를 입력하세요.")

# 마방진 함수 
def print_result () :
    rows = mabangjin
    cols = mabangjin
    x1 = int(mabangjin / 2)
    y = 0
    hang = []
    for row in range(rows):
        yeol = []
        for col in range(cols) :
            yeol.append(0)
        hang.append(yeol)
    
    hang[y][x1] = 1
    
    i = 2

    while i <= rows * cols :
        
        if hang[y-1][x1+1] == 0 :
            hang[y-1][x1+1] = i


        elif y == -1:
            hang[rows-1][x1+1] = i


        elif x1 == cols :
            hang[rows-1][0] = i

        elif hang[y-1][x1+1] in hang:
            hang[y+1][x1+1] = i
        
        i += 1
        
        if i == rows*cols + 1 :
            break

    for a in hang :
        print(a)

holsu()
print_result()