n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def find_pos(num):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                return (i, j)


def next_pos(pos):
    dxs = [-1, -1, -1,  0, 0,  1, 1, 1]
    dys = [-1,  0,  1, -1, 1, -1, 0, 1]
    
    x, y = pos
    
    
    max_val = -1
    max_pos = (-1, -1)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] > max_val:
            max_val, max_pos = grid[nx][ny], (nx, ny)
    
    return max_pos


def swap(pos, next_pos):
    (x, y), (nx, ny) = pos, next_pos
    grid[x][y], grid[nx][ny] = grid[nx][ny], grid[x][y]


def simulate():
    
    for num in range(1, n * n + 1):
        pos = find_pos(num)
        max_pos = next_pos(pos)
        swap(pos, max_pos)



for _ in range(m):
    simulate()

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()