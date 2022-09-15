n=int(input())

answer=[]
def backtracting(pair):
    
    if len(pair)==n:
        answer.append(pair.copy())     
        return 
    elif len(pair)>n:
        return
    for i in range(1,5):
        if len(pair)+i<=n:
            pair.extend([i]*i)
            backtracting(pair)
            for _ in range(i):
                pair.pop()
backtracting([])
print(len(answer))
