n=int(input())

flag=False
def backtracking(check):
    global flag
    if n==1:
        return print(4)
    if flag:
        return
    for start in range(len(check)):
        for end in range(start,len(check)-1):
            string=check[start:end+1]
            if check[end+1:end+1+end-start+1]==string:
                return
    if len(check)==n:
        flag=True
        print(check)
        return
    for i in range(4,7):
        backtracking(check+str(i))
backtracking("")
