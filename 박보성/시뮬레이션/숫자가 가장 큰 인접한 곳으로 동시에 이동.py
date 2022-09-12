n,m,t=map(int,input().split())
matrix=list(list(map(int, input().split())) for _ in range(n))
check=list(list(0 for _ in range(n)) for _ in range(n))
next_check=list(list(0 for _ in range(n)) for _ in range(n))

for _ in range(m):
    r,c=map(int, input().split())
    check[r-1][c-1]=1

for _ in range(t):
    for r in range(n):
        for c in range(n):
            if check[r][c]>=1:
                maximum=-float("inf")
                if 0<=r-1<n and 0<=c<n:
                    if matrix[r-1][c]>maximum:
                        maximum=matrix[r-1][c]
                        y=r-1
                        x=c
                if 0<=r+1<n and 0<=c<n:
                    if matrix[r+1][c]>maximum:
                        maximum=matrix[r+1][c]
                        y=r+1
                        x=c
                if 0<=r<n and 0<=c-1<n:
                    if matrix[r][c-1]>maximum:
                        maximum=matrix[r][c-1]
                        y=r
                        x=c-1
                if 0<=r<n and 0<=c+1<n:
                    if matrix[r][c+1]>maximum:
                        maximum=matrix[r][c+1]
                        y=r
                        x=c+1
                next_check[y][x]+=1
    for r in range(n):
        for c in range(n):
            if next_check[r][c]!=1:
                next_check[r][c]=0
    check=next_check
    next_check=list(list(0 for _ in range(n)) for _ in range(n))
cnt=0
for r in range(n):
    for c in range(n):
        if check[r][c]==1:
            cnt+=1
print(cnt)
