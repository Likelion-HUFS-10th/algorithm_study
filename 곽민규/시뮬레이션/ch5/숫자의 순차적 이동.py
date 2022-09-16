n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def find_x_y(t):
    # 1부터 n*n까지 각각의 x, y 좌표를 찾음
    for i in range(n):
        for j in range(n):
            if grid[i][j] == t:
                x, y = i, j
    return x, y

def biggest_coordinate(x, y):
    # 찾은 좌표를 바탕으로 인접한 8방향의 숫자를 수집함
    # x, y -> x-1, y-1 / x-1, y / x-1, y+1 / x, y-1 / x, y+1 / x+1, y-1 / x+1, y / x+1, y+1
    # -1, 0, +1 3x3 조합 돌리고 0 + 0일 때만 제외
    dxs, dys = [-1, 0, 1], [-1, 0, 1]
    max_num, mx, my = -1, -1, -1
    for dx in dxs:
        for dy in dys:
            nx, ny = x+dx, y+dy
            if dx == 0 and dy == 0:
                continue
            elif 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] > max_num:
                    max_num = grid[nx][ny]
                    mx, my = nx, ny
                    # print(max_num)
    return mx, my

def change(x, y, mx, my, t):
    # 인접한 위치에서 가장 큰 숫자 좌표로 격자 교환
    grid[x][y] = grid[mx][my]
    grid[mx][my] = t

def move():
    for t in range(1, n*n+1):
        x, y = find_x_y(t)
        # print(x, y)
        mx, my = biggest_coordinate(x, y)
        # print(mx, my)
        change(x, y, mx, my, t)
        
for _ in range(m):
    move()

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()