n,m=map(int, input().split())
matrix=list(list(map(int, input().split())) for _ in range(n))

dx=[1,1,0,-1,-1,0,-1,1]
dy=[0,1,1,0,-1,-1,1,-1]
for _ in range(m):
    idx=1
    while idx<=n**2:
        flag=False
        for r in range(n):
            for c in range(n):
                if matrix[r][c]==idx:
                    maximum=-float("inf")
                    x=c
                    y=r
                    for i in range(8):
                        if 0<=r+dy[i]<n and 0<=c+dx[i]<n:
                            if matrix[r+dy[i]][c+dx[i]]>maximum:
                                maximum=matrix[r+dy[i]][c+dx[i]]
                                x=c+dx[i]
                                y=r+dy[i]
                    matrix[r][c],matrix[y][x]=matrix[y][x],matrix[r][c]
                    flag=True
                    break
            if flag:
                break
        idx+=1
for m in matrix:
    print(*m)
