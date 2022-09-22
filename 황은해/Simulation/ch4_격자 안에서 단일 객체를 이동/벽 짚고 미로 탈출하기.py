import sys

DIR_NUM = 4

# 변수 선언 및 입력
n = int(input())
curr_x, curr_y = tuple(map(int, input().split()))
a = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

# 미로 탈출이 불가능한지 여부를 판단하기 위해
# 동일한 위치에 동일한 방향으로 진행했던 적이 있는지를
# 표시해주는 배열입니다.
visited = [
    [
        [False for _ in range(DIR_NUM)]
        for _ in range(n + 1)
    ]
    for _ in range(n + 1)
]
elapsed_time = 0

# 처음에는 우측 방향을 바라보고 시작합니다.
curr_dir = 0


# 범위가 격자 안에 들어가는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 해당 위치에 벽이 있으면 이동이 불가합니다.
def wall_exist(x, y):
    return in_range(x, y) and a[x][y] == '#'


# 조건에 맞춰 움직여봅니다.
def simulate():
    global curr_x, curr_y, curr_dir, elapsed_time
    
    # 현재 위치에 같은 방향으로 진행한 적이 이미 있었는지 확인합니다.
    # 이미 한 번 겪었던 상황이라면, 탈출이 불가능 하다는 의미이므로 
    # -1을 출력하고 프로그램을 종료합니다.
    if visited[curr_x][curr_y][curr_dir]:
        print(-1)
        sys.exit(0)
    
    # 현재 상황이 다시 반복되는지를 나중에 확인하기 위해
    # 현재 상황에 해당하는 곳에 visited 값을 True로 설정합니다.
    visited[curr_x][curr_y][curr_dir] = True
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
    
    # Step1
    
    # 바라보고 있는 방향으로 이동하는 것이 불가능한 경우에는
    # 반 시계 방향으로 90' 방향을 바꿉니다.
    if wall_exist(next_x, next_y):
        curr_dir = (curr_dir - 1 + 4) % 4
    
    # Step2
    
    # Case1
    # 바라보고 있는 방향으로 이동하는 것이 가능한 경우 중
    # 바로 앞이 격자 밖이라면 탈출합니다.
    elif not in_range(next_x, next_y):
        curr_x, curr_y = next_x, next_y
        elapsed_time += 1
    
    # Case 2 & Case 3
    # 바로 앞이 격자 안에서 이동할 수 있는 곳이라면
    else:
        # 그 방향으로 이동했다 가정헀을 때 바로 오른쪽에 짚을 벽이 있는지 봅니다.
        rx = next_x + dxs[(curr_dir + 1) % 4]
        ry = next_y + dys[(curr_dir + 1) % 4]
        
        # Case2
        # 그대로 이동해도 바로 오른쪽에 짚을 벽이 있다면
        # 해당 방향으로 한 칸 이동합니다.
        if wall_exist(rx, ry):
            curr_x, curr_y = next_x, next_y
            elapsed_time += 1
        
        # Case3
        # 그렇지 않다면 2칸 이동후 방향을 시계방향으로 90' 방향을 바꿉니다.
        else:
            curr_x, curr_y = rx, ry
            curr_dir = (curr_dir + 1) % 4
            elapsed_time += 2


for i in range(1, n + 1):
    given_row = input()
    for j, elem in enumerate(given_row, start = 1):
        a[i][j] = elem

# 격자를 빠져나오기 전까지 계속 반복합니다.
while in_range(curr_x, curr_y):
    # 조건에 맞춰 움직여봅니다.
    simulate()

print(elapsed_time)