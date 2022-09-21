n = int(input())
answer, result = [], []

def beautiful_number(answer):
    # print('enter')
    if len(answer) == n:
        # print(answer)
        result.append(answer)
        # print('exit')
        return
    elif len(answer) > n:
        # print('exit')
        return

    for i in range(1, 5):
        # print(f'i:{i}')
        # print(f"answer:{answer}")
        if len(answer) + i <= n:
            # 1은 무조건1개, 2는 무조건 2개, 3은 무조건 3개 연속임
            answer.extend([i] * i)
            beautiful_number(answer)
            for _ in range(i):
                answer.pop()
            
    # print('exit')
    return

beautiful_number(answer)
print(len(result))
# Credits to 보성형님