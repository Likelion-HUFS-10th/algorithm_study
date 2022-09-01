n,m=map(int,input().split())
matrix=list(list(map(int,input().split())) for _ in range(n))

cnt=-float("inf")
for i in range(n):
    for j in range(m):
        try:
            cnt=max(cnt,matrix[i+1][j]+matrix[i-1][j]+matrix[i][j]) 
        except:
            pass

for i in range(n):
    for j in range(m):
        try:
            cnt=max(cnt,matrix[i][j+1]+matrix[i][j-1]+matrix[i][j])
        except:
            pass

dx=[0,1,0,-1,0]
dy=[1,0,-1,0,1]
for i in range(n):
    for j in range(m):
        for k in range(4):
            try:
                cnt=max(cnt,matrix[i+dx[k]][j+dy[k]]+matrix[i+dx[k+1]][j+dy[k+1]]+matrix[i][j]) 
            except:
                pass
print(cnt)
