K, N = map(int, input().split())
answer= []

def print_answer():
    for ele in answer:
        print(ele, end=' ')
    print()

def permutation(level):
    if level == N+1:
        print_answer()
        return
    
    for k in range(1, K+1):
        # print(f'k={k}')
        if answer[-2:] == [k] * 2:
            continue
        answer.append(k)
        permutation(level+1)
        answer.pop()

    return

permutation(1)