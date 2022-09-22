n=int(input())

def backtracking(visited):
    if len(visited)==n:
        print(*visited)
        return
    for i in range(1,n+1):
        if i not in visited:
            visited.append(i)
            backtracking(visited)
            visited.pop()
backtracking([])
