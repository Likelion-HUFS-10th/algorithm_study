SHIFT_RIGHT = 0
SHIFT_LEFT = 1

# 변수 선언 및 입력
n, m, q = tuple(map(int, input().split()))
a = [
    [0 for _ in range(m + 1)]
    for _ in range(n + 1)
]


# row 줄의 원소들을 dir 방향에 따라 한 칸 밀어줍니다.
# dir이 0인 경우 오른쪽으로
# dir이 1인 경우 왼쪽으로 밀어야 합니다.
def shift(row, curr_dir):
    # 오른쪽으로 밀어야 하는 경우 
    if curr_dir == SHIFT_RIGHT:
        a[row].insert(1, a[row].pop())
    else:
        a[row].insert(m, a[row].pop(1))

def has_same_number(row1, row2):
    return any([
        a[row1][col] == a[row2][col]
        for col in range(1, m + 1)
    ])


# 주어진 방향으로부터 반대 방향의 값을 반환합니다.
def flip(curr_dir):
    return SHIFT_RIGHT if curr_dir == SHIFT_LEFT else SHIFT_LEFT


# 조건에 맞춰 움직여봅니다.
# dir이 SHIFT_RIGHT 인 경우 오른쪽으로
# dir이 SHIFT_LEFT 인 경우 왼쪽으로 밀어야 합니다.
def simulate(start_row, start_dir):
    # Step1
    # 바람이 처음으로 불어 온 행의 숫자들을 해당 방향으로 밀어줍니다.
    shift(start_row, start_dir)
    
    # 그 이후부터는 반전된 방향에 영향을 받으므로, 방향을 미리 반전시켜 줍니다.
    start_dir = flip(start_dir)
    
    # Step2
    # 위 방향으로 전파를 계속 시도해봅니다.
    curr_dir = start_dir
    for row in range(start_row, 1, -1):
        # 인접한 행끼리 같은 숫자를 가지고 있다면
        # 위의 행을 한 칸 shift 하고
        # 방향을 반대로 바꿔 계속 전파를 진행합니다.
        if has_same_number(row, row - 1):
            shift(row - 1, curr_dir)
            curr_dir = flip(curr_dir)
        # 같은 숫자가 없다면 전파를 멈춥니다.
        else:
            break
    
    # Step3
    # 아래 방향으로 전파를 계속 시도해봅니다.
    curr_dir = start_dir
    for row in range(start_row, n):
        # 인접한 행끼리 같은 숫자를 가지고 있다면
        # 아래 행을 한 칸 shift하고
        # 방향을 반대로 바꿔 계속 전파를 진행합니다.
        if has_same_number(row, row + 1):
            shift(row + 1, curr_dir)
            curr_dir = flip(curr_dir)
        # 같은 숫자가 없다면 전파를 멈춥니다.
        else:
            break


for row in range(1, n + 1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start = 1):
        a[row][col] = num

for _ in range(q):
    r, d = tuple(input().split())
    r = int(r)
    
    # 조건에 맞춰 움직여봅니다
    simulate(r, SHIFT_RIGHT if d == 'L' else SHIFT_LEFT)


for row in range(1, n + 1):
    for col in range(1, m + 1):
        print(a[row][col], end = " ")
    print()