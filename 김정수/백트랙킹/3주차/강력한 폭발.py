n = int(input())
bomb_type = [
    [0 for _ in range(n)]
    for _ in range(n)
]
bombed = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0

bomb_pos = list()


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def bomb(x, y, b_type):

    bomb_shapes = [
        [],
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]

    for i in range(5):
        dx, dy = bomb_shapes[b_type][i];
        nx, ny = x + dx, y + dy
        if in_range(nx, ny):
            bombed[nx][ny] = True

def calc():
    for i in range(n):
        for j in range(n):
            bombed[i][j] = False

    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                bomb(i, j, bomb_type[i][j])


    cnt = 0
    for i in range(n):
        for j in range(n):
            if bombed[i][j]:
                cnt += 1

    return cnt


def find_max_area(cnt):
    global ans

    if cnt == len(bomb_pos):
        ans = max(ans, calc())
        return

    for i in range(1, 4):
        x, y = bomb_pos[cnt]

        bomb_type[x][y] = i
        find_max_area(cnt + 1)
        bomb_type[x][y] = 0


for i in range(n):
    given_row = list(map(int, input().split()))
    for j, bomb_place in enumerate(given_row):
        if bomb_place:
            bomb_pos.append((i, j))

find_max_area(0)

print(ans)