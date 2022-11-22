from collections import deque
q = deque()
n, m = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    return in_range(x, y) and graph[x][y] != 0 and not visited[x][y]

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y]+1)

push(0, 0, 0)
bfs()
# if step[n-1][m-1] > 0:
#     print(step[n-1][m-1])
# else:
#     print(-1)
print(step[-1][-1] if step[-1][-1] else -1)