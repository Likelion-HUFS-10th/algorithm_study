n=int(input())
matrix=list(list(map(int, input().split())) for _ in range(n))

answer=0
def backtracking(visited):
    global answer

    if len(visited)==n:
        cnt=0
        for i in range(n):
            cnt+= matrix[i][visited[i]]
        answer=max(answer,cnt)
        return
    for i in range(n):
        if i not in visited:
            visited.append(i)
            backtracking(visited)
            visited.pop()
backtracking([])
print(answer)
