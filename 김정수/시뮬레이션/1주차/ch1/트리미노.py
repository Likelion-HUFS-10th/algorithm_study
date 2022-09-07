# 변수 선언 및 입력

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 가능한 모든 모양을 전부 적어둠
shapes = [
    [[1,1,0],
    [1,0,0],
    [0,0,0]],

    [[1,1,0],
    [0,1,0],
    [0,0,0]],

    [[1,0,0],
    [1,1,0],
    [0,0,0]],

    [[0,1,0],
    [1,1,0],
    [0,0,0]],

    [[1,1,1],
    [0,0,0],
    [0,0,0]],

    [[1,0,0],
    [1,0,0],
    [1,0,0]],
]

# 주어진 위치에 대하여 가능한 모든 모양을 탐색하여 최대 합을 반환
def get_max_sum(x,y):
    max_sum=0
    for i in range(6):
        is_possible=True
        sum_of_nums=0
        for dx in range(0,3):
            for dy in range(0,3):
                if shapes[i][dx][dy] == 0:
                    continue
                if x + dx >= n or y + dy >= m:
                    is_possible = False
                else:
                    sum_of_nums += grid[x+dx][y+dy]
        if is_possible:
            max_sum = max(max_sum, sum_of_nums)

    return max_sum

ans = 0

# 격자의 각 위치에 대하여 탐색하여줍니다.
for i in range(n):
    for j in range(m):
        ans = max(ans, get_max_sum(i,j))

print(ans)