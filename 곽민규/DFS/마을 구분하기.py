n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
town_count, people_count = [], 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def dfs(x, y):
    global people_count
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] != 0 and not visited[nx][ny]:
            # print(f'nx, ny = {nx, ny}')
            people_count += 1
            # print(f'people:{people_count}')
            visited[nx][ny] += people_count
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            # grid에서 1이면서 not visited[i][j]인 좌표가 스타트 지점
            # print(f'i, j = {i, j}')
            visited[i][j] = 1
            people_count = 1
            dfs(i, j)
            # print(people_count)
            town_count.append(people_count)

print(len(town_count))
for town in sorted(town_count):
    print(town)