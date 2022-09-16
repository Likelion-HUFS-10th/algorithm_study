K, N = map(int, input().split())
answer = []

def print_answer():
    for ele in answer:
        print(ele, end = ' ')
    print()

def choose(curr_num):
    if curr_num == N+1:
        print_answer()
        return
    
    for k in range(1, K+1):
        answer.append(k)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)