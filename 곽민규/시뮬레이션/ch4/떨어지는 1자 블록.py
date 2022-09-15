n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

for i in range(n): # 열에 해당하는 행마다 부딫히는지 판단
    count, x, y = 0, 0, 0
    for j in range(k-1, k+m-1): # 열 공간 확보
        if grid[i][j] == 0:
            count += 1
        else:
            break
    # print(f'count:{count}')
    if count < m:
        x = i - 1
        y = k - 1
        # print(x,y)
        break
    elif count == m:
        x = i
        y = k - 1
        # print(x,y)
    else:
        continue

for i in range(y, y+m):
    grid[x][i] = 1

for row in grid:
    print(*row)

