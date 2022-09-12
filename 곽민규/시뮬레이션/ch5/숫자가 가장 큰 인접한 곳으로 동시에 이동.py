n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
marbles = [list(map(int, input().split())) for _ in range(m)]
count = [[0] * n for _ in range(n)]
next_count = [[0] * n for _ in range(n)]

for r, c in marbles:
    x, y = r-1, c-1
    count[x][y] = 1

def move(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    max_bubble, mx, my = -1, -1, -1
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] > max_bubble:
                max_bubble = grid[nx][ny]
                mx, my = nx, ny
    
    next_count[mx][my] += 1

def simulate():
    for i in range(n):
        for j in range(n):
            next_count[i][j] = 0
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

def remove_and_count():
    result = 0
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0
            elif count[i][j] == 1:
                result += 1
    return result

for _ in range(t):
    simulate()
    result = remove_and_count()

print(result)
