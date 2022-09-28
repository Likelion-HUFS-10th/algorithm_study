n = int(input())
visited = [False] * (n + 1)
answer = []

def print_answer():
    for ele in answer:
        print(ele, end=" ")
    print()

def choose(phase):
    if phase == n+1:
        print_answer()
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)

        choose(phase+1)

        answer.pop()
        visited[i] = False

choose(1)