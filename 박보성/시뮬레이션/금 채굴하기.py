n,m=map(int, input().split())
matrix=list(list(map(int,input().split())) for _ in range(n))

def search(x,y,k):
    global cnt, cost

    if 0<=x<n and 0<=y<n and matrix[x][y]==1:
        cnt+=1
    if 0<=x<n and 0<=y<n:
        cost+=1

    for i in range(1,k+1):
        if 0<=x<n and 0<=y+i<n and matrix[x][y+i]==1:
            cnt+=1
        if 0<=x<n and 0<=y+i<n:
            cost+=1

        if 0<=x<n and 0<=y-i<n and matrix[x][y-i]==1:
            cnt+=1
        if 0<=x<n and 0<=y-i<n:
            cost+=1
max_cnt=0
for i in range(n):
    for j in range(n):
        k=0
        cost=0
        while cost<n**2:
            cnt=0
            cost=0

            search(i,j,k)
            num=0
            copy_k=k
            while True:
                copy_k-=1
                num+=1        
                if copy_k<0:
                    break
                search(i+num,j,copy_k)
                search(i-num,j,copy_k)

            if k**2+(k+1)**2<=m*cnt and cnt>max_cnt:
                # print(cost, k, k**2+(k+1)**2,cnt*m, i, j)
                max_cnt=cnt
            k+=1       
print(max_cnt)
