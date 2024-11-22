mabangjin = int(input("홀수차 배열의 크기를 입력하세요 : "))

# 3, 5, 7, 9인지 확인하는 함수
def holsu():
    if mabangjin in [3, 5, 7, 9]: 
        print("Magic Square", f"({mabangjin}x{mabangjin})")
    else:
        print("3, 5, 7, 9 중에 하나의 숫자를 입력하세요.")
        exit()

# 마방진 함수 
def print_result():
    rows = mabangjin
    cols = mabangjin
    x = mabangjin // 2
    y = 0
    hang = [[0] * cols for _ in range(rows)]
    
    num = 1
    while num <= rows * cols:
        hang[y][x] = num
        num += 1
        new_y = (y - 1) % rows
        new_x = (x + 1) % cols
        if hang[new_y][new_x] != 0:
            y = (y + 1) % rows
        else:
            y = new_y
            x = new_x

    for row in hang:
        print("\t".join(map(str, row)))

holsu()
print_result()
