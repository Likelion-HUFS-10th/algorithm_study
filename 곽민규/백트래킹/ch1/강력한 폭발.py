n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
field = [[0]*n for _ in range(n)]

result = 0
bomb = 0
bomb_list = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb += 1
            bomb_list.append([i, j])

def explode_or_cleanup(num, x, y, v):
    field[x][y] += v
    if num == 1:
        dxs, dys = [-2, -1, 1, 2], [0, 0, 0, 0]
    elif num == 2:
        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    else:
        dxs, dys = [-1, -1, +1, +1], [-1, +1, -1, +1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            field[nx][ny] += v

def print_answer():
    exploded = 0
    global result
    for i in range(n):
        for j in range(n):
            if field[i][j] >= 1:
                exploded += 1
    result = max(exploded, result)

# Phase = (bomb)개
def explode(phase):
    # 탈출 로직 = 그리드 안 1의 개수만큼 돌았을 때
    if phase == bomb + 1:
        print_answer()
        return

    # 각 폭탄 경우마다 칠할 수 있는 곳은 1로 바꿔놓기

    i, j = bomb_list[phase-1]
    # print(i, j)
    for num in range(1, 4):
        # print(f'num:{num}')
        explode_or_cleanup(num, i, j, 1)
        # print('explode')
        # print(field)
        explode(phase + 1)
        # print('cleanup')
        explode_or_cleanup(num, i, j, -1)# cleanup logic
        # print(field)
    # print()
    return

# print(bomb_list)
explode(1)
print(result)