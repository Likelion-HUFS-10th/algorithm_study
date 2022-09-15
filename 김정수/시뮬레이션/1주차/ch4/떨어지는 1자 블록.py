n, m, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def all_blank(row, col_s, col_e):
    return all([
        not grid[row][col]
        for col in range(col_s, col_e + 1)
    ])



def get_target_row():
    for row in range(n - 1):
        if not all_blank(row + 1, k, k + m - 1):
            return row

    return n - 1
        

k -= 1

target_row = get_target_row()


for col in range(k, k + m):
    grid[target_row][col] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()