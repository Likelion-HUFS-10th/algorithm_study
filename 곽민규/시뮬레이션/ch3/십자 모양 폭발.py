n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
result = []
bomb = grid[r-1][c-1]

# 폭탄 폭파
def explode():
    for i in range(bomb):
        x, y = r-1, c-1
        # 0 x-0, y / x+0, y / x, y-0 / x, y+0
        # 1 x-1, y / x+1, y / x, y-1 / x, y+1
        # 2 x-2, y / x+2, y / x, y-2 / x, y+2
        if x-i >= 0:
            grid[x-i][y] = 0
        if x + i < n:
            grid[x+i][y] = 0
        if y - i >= 0:
            grid[x][y-i] = 0
        if y + i < n:
            grid[x][y+i] = 0

def gravity(n):
    cols = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cols[i].append(grid[j][i])
    # 2 0 0 5 -> 
    # 4 0 0 0 -> 4000 / 4 0 00, 0+4+00 / 04 0 0, 0+04+0 / 004 0, 0+004 
    # print(cols)
    
    for col in cols:
        for i, n in enumerate(col):
            if n == 0:
                col = [col[i]] + col[:i] + col[i+1:]
        # print(col)
        result.append(col)

explode()
gravity(n)
for i in range(n):
    for j in range(n):
        print(result[j][i], end=" ")
    print()



        
