CCW = 0
CW = 1

# 변수 선언 및 입력:
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def shift(x, y, k, l, move_dir):
    if move_dir == CCW:
        dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
        move_nums = [k, l, k, l]
    else:
        dxs, dys = [-1, -1, 1, 1], [-1, 1, 1, -1]
        move_nums = [l, k, l, k]
    
    # Step1. temp 배열에 grid 값을 복사합니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = grid[i][j]

    # Step2. 기울어진 직사각형의 경계를 쭉 따라가면서
    #        숫자를 한 칸씩 밀었을 때의 결과를
    #        temp에 저장합니다.
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            nx, ny = x + dx, y + dy
            temp[nx][ny] = grid[x][y]
            x, y = nx, ny
    
    # Step3. temp값을 grid에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]



x, y, m1, m2, m3, m4, d = tuple(map(int, input().split()))
shift(x - 1, y - 1, m1, m2, d)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()