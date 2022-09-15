NONE = -1

n = 4
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]



def rotate():
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n - j - 1][i]
    
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]



def drop():
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    
    for j in range(n):
        
        keep_num, next_row = NONE, n - 1
        
        for i in range(n - 1, -1, -1):
            if not grid[i][j]:
                continue
            
            
            if keep_num == NONE:
                keep_num = grid[i][j];
            
            
            elif keep_num == grid[i][j]:
                next_grid[next_row][j] = keep_num * 2
                keep_num = NONE
                
                next_row -= 1
            
            
            else:
                next_grid[next_row][j] = keep_num
                keep_num = grid[i][j]
                
                next_row -= 1
        
        
        if keep_num != NONE:
            next_grid[next_row][j] = keep_num
            next_row -= 1
    
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]



def tilt(move_dir):
    
    for _ in range(move_dir):
        rotate()

    
    drop()
    
    
    for _ in range(4 - move_dir):
        rotate()


dir_char = input()

dir_mapper = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}


tilt(dir_mapper[dir_char])

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()