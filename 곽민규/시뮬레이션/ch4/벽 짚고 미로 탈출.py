n = int(input())
x, y = tuple(map(int, input().split()))
x -= 1
y -= 1
grid = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
visited[x][y] = 1
count, d = 0, 0

def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def next_path(x, y, d):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 0-동 1-남 2-북 3-서
    nx, ny = x + dxs[d], y + dys[d]
    return nx, ny

def rotate(d):
    """
    동쪽으로 움직일 수 있으면 오른쪽인 남쪽을 확인,
    남쪽으로 움직일 수 있으면 오른쪽인 서쪽을 확인,
    서쪽으로 움직일 수 있으면 오른쪽인 북쪽을 확인,
    북쪽으로 움직일 수 있으면 오른쪽인 동쪽을 확인하기 때문에
    d값만 1씩 증가시켜주면
    path함수의 dx dy가 자동으로 오른쪽을 바라보게 됨
    """
    d = (d + 1) % 4 
    return d

def is_right_wall(x, y, d):
    d = rotate(d)
    nx, ny = next_path(x, y, d)
    return is_in_range(nx, ny) and grid[nx][ny] == '#' # 

def move():
    global x, y, d, count, visited
    nx, ny = next_path(x, y, d)
    if not is_in_range(nx, ny): # 앞이 출구임
        count += 1
        return True
    visited[x][y] += 1
    if visited[x][y] > 10:
        count = -1
        return True
    if grid[nx][ny] == '.': # 앞으로 이동 가능
        if is_right_wall(nx, ny, d): # 짚을 벽이 있을 때
            x, y = nx, ny
            count += 1
        else:
            x, y = nx, ny
            count += 1
            d = rotate(d)
            x, y = next_path(x, y, d)
            count += 1
    else: # 앞이 벽에 막혀있음
        d = rotate(d+2) # 2번 더 회전하면 왼쪽으로 설정
    
    return False

def simulation():
    global x, y, d, count
    while not move():
        pass

simulation()
print(count)