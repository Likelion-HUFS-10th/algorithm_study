n,m,k=map(int, input().split())

matrix=list(list(map(int ,input().split())) for _ in range(n))

def check():
    if n==1:
        if m:
            matrix[0][0]=1
            return
    for r in range(n):
        flag=True
        for c in range(k-1,k+m-1):
            if matrix[r][c]:
                flag=False
                break
        if not flag:
            for c in range(k-1,k+m-1):
                matrix[r-1][c]=1
            return
    for c in range(k-1,k+m-1):
        matrix[n-1][c]=1
check()
for m in matrix:
    print(*m)
