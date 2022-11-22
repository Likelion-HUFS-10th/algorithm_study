from collections import deque
q = deque()
n, m = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
order = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if in_range(x, y) and graph[x][y] == 1 and not visited[x][y]:
        return True
    else: return False

def push(x, y):
    global order
    answer[x][y] = order
    order += 1
    visited[x][y] = True
    q.append((x, y))

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            next_x, next_y = x+dx, y+dy

            if can_go(next_x, next_y):
                # print(next_x, next_y)
                push(next_x, next_y)

push(0, 0)
bfs()
if visited[n-1][m-1]:
    print(1)
else: print(0)