MAX_N = 50

# 변수 선언 및 입력
t = int(input())
n, m = 0, 0
marbles = []
marble_cnt = [
    [0 for _ in range(MAX_N + 1)]
    for _ in range(MAX_N + 1)
]

# 입력으로 주어진 방향을 정의한 dx, dy에 맞도록
# 변환하는데 쓰이는 dict를 정의합니다.
mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}


# 해당 위치가 격자 안에 들어와 있는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 해당 구슬이 1초 후에 어떤 위치에서 어떤 방향을 보고 있는지를 구해
# 그 상태를 반환합니다.
def move(marble):
    # 구슬이 벽에 부딪혔을 때의 처리를 간단히 하기 위해
    # dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록 설정합니다.
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
    x, y, move_dir = marble
    
    # 바로 앞에 벽이 있는지를 판단합니다.
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    
    # Case 1 : 벽이 없는 경우에는 그대로 한 칸 전진합니다.
    if in_range(nx, ny):
        return (nx, ny, move_dir)
    # Case 2 : 벽이 있는 경우에는 방향을 반대로 틀어줍니다.
    # 위에서 dx, dy를 move_dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록
    # 설정해놨기 때문에 간단하게 처리가 가능합니다.
    else:
        return (x, y, 3 - move_dir)
    

# 구슬을 전부 한 번씩 움직여봅니다.
def move_all():
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble)


# 해당 구슬과 충돌이 일어나는 구슬이 있는지 확인합니다.
# 이를 위해 자신의 현재 위치에 놓은 구슬의 개수가
# 자신을 포함하여 2개 이상인지 확인합니다.
def duplicate_marble_exist(target_idx):
    target_x, target_y, _ = marbles[target_idx]
    
    return marble_cnt[target_x][target_y] >= 2
    

# 충돌이 일어나는 구슬을 전부 지워줍니다.
def remove_duplicate_marbles():
    global marbles
    
    # Step2-1 : 각 구슬의 위치에 count를 증가 시킵니다.
    for x, y, _ in marbles:
        marble_cnt[x][y] += 1

    # Step2-2 : 충돌이 일어나지 않은 구슬만 전부 기록합니다.
    remaining_marbles = [
        marble
        for i, marble in enumerate(marbles)
        if not duplicate_marble_exist(i)
    ]
    
    # Step2-3 : 나중을 위해 각 구슬의 위치에 적어놓은 count 수를 다시 초기화합니다.
    for x, y, _ in marbles:
        marble_cnt[x][y] -= 1
    
    # Step2-4 : 충돌이 일어나지 않은 구슬들로 다시 채워줍니다.
    marbles = remaining_marbles


# 조건에 맞춰 시뮬레이션을 진행합니다.
def simulate():
    # Step1
    # 구슬을 전부 한 번씩 움직여봅니다.
    move_all()
    
    # Step2
    # 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 지워줍니다.
    remove_duplicate_marbles()


for _ in range(t):
    # 새로운 테스트 케이스가 시작될때마다 기존에 사용하던 값들을 초기화해줍니다.
    marbles = []
    
    # 입력
    n, m = tuple(map(int, input().split()))
    for _ in range(m):
        x, y, d = tuple(input().split())
        x, y = int(x), int(y)
        marbles.append((x, y, mapper[d]))
    
    # 2 * n번 이후에는 충돌이 절대 일어날 수 없으므로
    # 시뮬레이션을 총 2 * n번 진행합니다.
    for _ in range(2 * n):
        simulate()
    
    # 출력
    print(len(marbles))