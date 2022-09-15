OUT_OF_GRID = (-1, -1)


n, m = tuple(map(int, input().split()))
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]


def get_pos(move_num):
    for i in range(n):
        for j in range(n):
            for num in grid[i][j]:
                if num == move_num:
                    return (i, j)


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n



def next_pos(pos):
    dxs = [-1, -1, -1,  0, 0,  1, 1, 1]
    dys = [-1,  0,  1, -1, 1, -1, 0, 1]
    
    x, y = pos
    
    
    max_val, max_pos = -1, OUT_OF_GRID
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            for num in grid[nx][ny]:
                if num > max_val:
                    max_val, max_pos = num, (nx, ny)
    
    return max_pos


def move(pos, next_pos, move_num):
    (x, y), (nx, ny) = pos, next_pos
    
    
    to_move = False
    for num in grid[x][y]:
        if num == move_num:
            to_move = True
        
        if to_move:
            grid[nx][ny].append(num)
    
    
    while grid[x][y][-1] != move_num:
        grid[x][y].pop()
    grid[x][y].pop()


def simulate(move_num):
    
    pos = get_pos(move_num)
    max_pos = next_pos(pos)
    if max_pos != OUT_OF_GRID:
        move(pos, max_pos, move_num)


for i in range(n):
    given_row = list(map(int, input().split()))
    for j, num in enumerate(given_row):
        grid[i][j].append(num)


move_nums = list(map(int, input().split()))
for move_num in move_nums:
    simulate(move_num)

for i in range(n):
    for j in range(n):
        if not grid[i][j]:
            print("None", end="")
        else:
            for num in grid[i][j][::-1]:
                print(num, end=" ")
        print()