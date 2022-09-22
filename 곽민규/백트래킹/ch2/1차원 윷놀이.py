n, m, k = map(int, input().split())
distance = list(map(int, input().split()))
player = [1] * k
result = 0

def print_answer():
    candidate = 0
    global result
    for i in player:
        if i >= m:
            candidate += 1
    result = max(result, candidate)
    # print(result)

def jump(phase):
    # 탈출 로직
    if phase == n + 1:
        print_answer()
        return
    
    # 반복 로직
    # '1번, 2번, 1번, 2번 말을 고른다'
    d = distance[phase - 1]
    # print(f'{phase}번째 {d}칸')
    
    for i in range(k):
        # if sum(i) >= m:
        #     continue
        player[i] += d
        # print(f'말:{player}')
        jump(phase+1)
        player[i] -= d
        # print(f'cleanup:{player}')
    
    return

jump(1)
print(result)