n, t = map(int, input().split())
grid = [list(map(str, input().split())) for _ in range(2)]

for _ in range(t):
    temp = []
    for row in grid:
        temp.append(row[-1])
        for i in range(n-1, 0, -1):
            row[i] = row[i - 1]
    
    for row in grid:
        row[0] = temp.pop()

for row in grid:
    print(" ".join(row))
