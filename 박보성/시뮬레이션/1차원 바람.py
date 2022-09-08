n,m,q=map(int, input().split())

matrix=list(list(map(int, input().split())) for _ in range(n))

for _ in range(q):
    r,d=input().split()
    r=int(r)
    #해당 줄
    if d=="L":
        matrix[r-1]=[matrix[r-1].pop()]+matrix[r-1][:m]
    else:
        matrix[r-1]=matrix[r-1][1:]+[matrix[r-1].pop(0)]
    #위로 진행
    before_d=d
    for i in range(r-2,-1,-1):
        flags=True
        for j in range(m):
            if matrix[i][j]==matrix[i+1][j]:
                if before_d=="R":
                    matrix[i]=[matrix[i].pop()]+matrix[i][:m]
                    before_d="L"
                else:
                    matrix[i]=matrix[i][1:]+[matrix[i].pop(0)]
                    before_d="R"
                flags=False
                break
        if flags:
            break
    #아래로 진행
    before_d=d
    for i in range(r,n):
        flags=True
        for j in range(m):
            if matrix[i][j]==matrix[i-1][j]:
                if before_d=="R":
                    matrix[i]=[matrix[i].pop()]+matrix[i][:m]
                    before_d="L"
                else:
                    matrix[i]=matrix[i][1:]+[matrix[i].pop(0)]
                    before_d="R"
                flags=False
                break
        if flags:
            break
for m in matrix:
    print(*m)
