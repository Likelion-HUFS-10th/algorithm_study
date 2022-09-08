n=int(input())
matrix=list(list(map(int, input().split())) for _ in range(n))
r,c=map(int, input().split())

dx=[1,0,-1,0]
dy=[0,-1,0,1]

d=matrix[r-1][c-1]
matrix[r-1][c-1]=0
for i in range(4):
    for j in range(d):
        x=c+dx[i]*j-1
        y=r+dy[i]*j-1
        if 0<=x<n and 0<=y<n:
            matrix[y][x]=0

answer=list(list(0 for _ in range(n)) for _ in range(n))
for c in range(n):
    column=list()
    for r in range(n):
        if matrix[r][c]:
            column.append(matrix[r][c])
    
    for r in range(n-1,-1,-1):
        if not column:
            break
        answer[r][c]=column.pop()
for m in answer:
    print(*m)
