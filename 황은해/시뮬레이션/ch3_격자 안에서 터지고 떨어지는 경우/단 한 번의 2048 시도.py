NONE = -1

# 변수 선언 및 입력
n = 4
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]


# grid를 시계방향으로 90' 회전시킵니다.
def rotate():
    # next_grid를 0으로 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    # 90' 회전합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n - j - 1][i]
    
    # next_grid를 grid에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


# 아래로 숫자들을 떨어뜨립니다.
def drop():
    # next_grid를 0으로 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    # 아래 방향으로 떨어뜨립니다.
    for j in range(n):
        # 같은 숫자끼리 단 한번만
        # 합치기 위해 떨어뜨리기 전에
        # 숫자 하나를 keep해줍니다.
        keep_num, next_row = NONE, n - 1
        
        for i in range(n - 1, -1, -1):
            if not grid[i][j]:
                continue
            
            # 아직 떨어진 숫자가 없다면, 갱신해줍니다.
            if keep_num == NONE:
                keep_num = grid[i][j];
            
            # 가장 최근에 관찰한 숫자가 현재 숫자와 일치한다면
            # 하나로 합쳐주고, keep 값을 비워줍니다.
            elif keep_num == grid[i][j]:
                next_grid[next_row][j] = keep_num * 2
                keep_num = NONE
                
                next_row -= 1
            
            # 가장 최근에 관찰한 숫자와 현재 숫자가 다르다면
            # 최근에 관찰한 숫자를 실제 떨어뜨려주고, keep 값을 갱신해줍니다.
            else:
                next_grid[next_row][j] = keep_num
                keep_num = grid[i][j]
                
                next_row -= 1
        
        # 전부 다 진행했는데도 keep 값이 남아있다면
        # 실제로 한번 떨어뜨려줍니다.
        if keep_num != NONE:
            next_grid[next_row][j] = keep_num
            next_row -= 1
    
    # next_grid를 grid에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


# move_dir 방향으로 기울이는 것을 진행합니다.
# 회전을 규칙적으로 하기 위해
# 아래, 오른쪽, 위, 왼쪽 순으로 dx, dy 순서를 가져갑니다.
def tilt(move_dir):
    # Step 1.
    # move_dir 횟수만큼 시계방향으로 90'회전하는 것을 반복하여
    # 항상 아래로만 숫자들을 떨어뜨리면 되게끔 합니다.
    for _ in range(move_dir):
        rotate()

    # Step 2.
    # 아래 방향으로 떨어뜨립니다.
    drop()
    
    # Step 3.
    # 4 - move_dir 횟수만큼 시계방향으로 90'회전하는 것을 반복하여
    # 처음 상태로 돌아오게 합니다. (총 360' 회전)
    for _ in range(4 - move_dir):
        rotate()


dir_char = input()

# 아래, 오른쪽, 위, 왼쪽 순으로 
# mapper를 지정합니다.
dir_mapper = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}

# 기울입니다.
tilt(dir_mapper[dir_char])

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()