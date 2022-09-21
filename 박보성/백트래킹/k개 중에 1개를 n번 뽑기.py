k,n=map(int, input().split())

answer=[]
def backtracting(depth, pair):
    if depth>=n:
        answer.append(pair.copy())     
        return 
    for i in range(1,k+1):
        pair.append(i)
        backtracting(depth+1, pair)
        pair.pop()
backtracting(0,[])
for a in answer:
    print(*a)
