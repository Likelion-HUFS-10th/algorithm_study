k,n=map(int, input().split())

temp=[]
def backtracking(depth):
    if depth>=n:
        cnt=1
        for i in range(n-1):
            if temp[i]==temp[i+1]:
                cnt+=1
                if cnt>=3:
                    return          
            else:
                cnt=1
        print(*temp)
        return
    for i in range(1,k+1):
        temp.append(i)
        backtracking(depth+1)
        temp.pop()
backtracking(0)
