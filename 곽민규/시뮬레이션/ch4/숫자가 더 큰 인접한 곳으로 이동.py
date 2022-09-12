n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r -= 1
c -= 1
start = grid[r][c]
result = [start]

def four_direction(r, c):
    subs = [[0] * n for _ in range(4)]
    if 0 <= r-1 < n and grid[r-1][c]:
        subs[0] = [grid[r-1][c], r-1, c]
    if 0 <= r+1 < n and grid[r+1][c]:
        subs[1] = [grid[r+1][c], r+1, c]
    if 0 <= c-1 < n and grid[r][c-1]:
        subs[2] = [grid[r][c-1], r, c-1]
    if 0 <= c+1 < n and grid[r][c+1]:
        subs[3] = [grid[r][c+1], r, c+1]
    subs = [sub for sub in subs if sub[0] > start]
    return subs

while len(four_direction(r, c)) > 0:
    start, r, c = four_direction(r, c)[0]
    result.append(start)
    # print(start, r, c)
print(*result)

