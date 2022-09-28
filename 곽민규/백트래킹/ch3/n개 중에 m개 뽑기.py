N, M = map(int, input().split())

def print_answer(answer):
    for ele in answer:
        print(ele, end=" ")
    print()

def choose(phase, answer):
    if phase == M+1 and len(answer) == M:
        print_answer(answer)
        return
    
    # print(f'phase:{phase}')
    for i in range(1, N+1):
        # print(f'i:{i}')
        if i < phase:
            continue
        if len(answer) > 0 and i <= answer[-1]:
            continue
        answer.append(i)
        # print(answer)
        choose(phase+1, answer)
        answer.pop()

    return

choose(1, [])