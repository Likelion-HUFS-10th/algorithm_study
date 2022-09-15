MAX_N = 50


t = int(input())
n, m = 0, 0
marbles = []
marble_cnt = [
    [0 for _ in range(MAX_N + 1)]
    for _ in range(MAX_N + 1)
]


mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}



def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n



def move(marble):
    
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
    x, y, move_dir = marble
    
    
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    
    
    if in_range(nx, ny):
        return (nx, ny, move_dir)
    
    else:
        return (x, y, 3 - move_dir)
    


def move_all():
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble)



def duplicate_marble_exist(target_idx):
    target_x, target_y, _ = marbles[target_idx]
    
    return marble_cnt[target_x][target_y] >= 2
    


def remove_duplicate_marbles():
    global marbles
    
    
    for x, y, _ in marbles:
        marble_cnt[x][y] += 1

    
    remaining_marbles = [
        marble
        for i, marble in enumerate(marbles)
        if not duplicate_marble_exist(i)
    ]
    
    
    for x, y, _ in marbles:
        marble_cnt[x][y] -= 1
    
    
    marbles = remaining_marbles



def simulate():
    
    move_all()
    
    
    remove_duplicate_marbles()


for _ in range(t):
    
    marbles = []
    
    
    n, m = tuple(map(int, input().split()))
    for _ in range(m):
        x, y, d = tuple(input().split())
        x, y = int(x), int(y)
        marbles.append((x, y, mapper[d]))
    
    
    for _ in range(2 * n):
        simulate()
    
   
    print(len(marbles))