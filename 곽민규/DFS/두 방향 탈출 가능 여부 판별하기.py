n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if in_range(x, y) and grid[x][y] == 1 and not visited[x][y]:
        return True
    else: return False

def dfs(x, y):
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x+dx, y+dy

        if can_go(next_x, next_y):
            # print(next_x, next_y)
            visited[next_x][next_y] = 1
            dfs(next_x, next_y)

visited[0][0] = 1
dfs(0, 0)
# print(grid)
# print(visited)
print(visited[n-1][m-1])