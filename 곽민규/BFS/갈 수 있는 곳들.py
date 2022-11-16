from collections import deque
q = deque()
n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
answer = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and grid[x][y] == 0 and not visited[x][y]

for _ in range(k):
    x, y = tuple(map(int, input().split()))
    q.append((x-1, y-1))

count = 0
def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    global count 
    while q:
        # print(f'q:{q}')
        x, y = q.popleft()
        # print(x, y)
        if can_go(x, y):
            visited[x][y] = True
            count += 1
            for dx, dy in zip(dxs, dys):
                nx, ny = x+dx, y+dy
                if can_go(nx, ny):
                    q.append((nx, ny))

bfs()
print(count)