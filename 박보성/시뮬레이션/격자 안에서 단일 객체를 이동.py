n,c,r=map(int, input().split())
matrix=list(list(map(int, input().split())) for _ in range(n))

x=r-1
y=c-1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
answer=[matrix[y][x]]
while True:
    flag=True
    for i in range(4):
        if 0<=x+dx[i]<n and 0<=y+dy[i]<n:
            if matrix[y+dy[i]][x+dx[i]]>matrix[y][x]:
                x=x+dx[i]
                y=y+dy[i]
                flag=False
                answer.append(matrix[y][x])
                break
    if flag:
        break
print(*answer)
