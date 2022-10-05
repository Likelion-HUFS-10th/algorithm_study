n,m=map(int,input().split())
matrix=list(list(map(int, input().split())) for _ in range(n))

def check(start_x,size_x, start_y, size_y):
    for x in range(start_x,start_x+size_x):
        for y in range(start_y,start_y+size_y):
            if matrix[y][x]<=0:
                return False
    return True

max_cnt=-1
for start_x in range(m):
    for start_y in range(n):    
        for size_x in range(m-start_x+1):
            for size_y in range(n-start_y+1):
                if check(start_x,size_x, start_y, size_y):
                    if max_cnt<size_x*size_y:
                        max_cnt=size_x*size_y
                        # print(start_x,size_x, start_y, size_y)
if max_cnt>0:
    print(max_cnt)
else:
    print(-1)
