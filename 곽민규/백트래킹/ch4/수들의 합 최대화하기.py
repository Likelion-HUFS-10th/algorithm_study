n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
candidate = {}
max_sum = 0

def calc_answer():
    global max_sum
    # print(candidate)
    # print(max_sum, sum(candidate.values()))
    max_sum = max(max_sum, sum(candidate.values()))

def circulate_matrix(phase):
    # 탈출 로직
    if phase == n:
        calc_answer()
        return
    # 반복 로직
    for i in range(n):
        if i in candidate.keys():
            continue
        candidate[i] = matrix[phase][i]
        circulate_matrix(phase+1)
        del candidate[i]
    return

circulate_matrix(0)
print(max_sum)