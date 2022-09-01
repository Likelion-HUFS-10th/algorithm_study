n=int(input())

matrix=list(list(map(int, input().split())) for _ in range(n))

answer=-float("inf")
if n>3:
    for i in range(n-2):
        for j in range(n-2):
            cnt=0
            for x in range(i,i+3):
                for y in range(j,j+3):
                    if matrix[x][y]==1:
                        cnt+=1
            answer=max(answer,cnt)
    print(answer)
elif n==3:
    cnt=0
    for x in range(3):
        for y in range(3):
            if matrix[x][y]==1:
                cnt+=1
    answer=max(answer,cnt)
    print(answer)
