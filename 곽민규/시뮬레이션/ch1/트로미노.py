n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
seq = [0 for _ in range(3)]

def max_seq():
    result = 0
    for i in seq:
        result += i
    return result

def max_apple(row, col):
    square, min_cell = 0, float('inf')
    for i in range(row, row+2):
        for j in range(col, col+2):
            min_cell = min(min_cell, grid[i][j])
            square += grid[i][j]
    return square - min_cell

max_sum = 0

# stick
for row in range(n):
    for col in range(m):
        if col + 2 >= m:
            continue
        seq = grid[row][col:col+3]
        max_sum = max(max_sum, max_seq())

for col in range(m):
    for row in range(n):
        if row + 2 >= n:
            continue
        for i in range(row, row+3):
            seq.pop()
            seq.insert(0,grid[i][col])
        max_sum = max(max_sum, max_seq())

# apple
for row in range(n):
    for col in range(m):
        if row + 1 >= n or col + 1 >= m:
            continue
        max_sum = max(max_sum, max_apple(row, col))

print(max_sum)
