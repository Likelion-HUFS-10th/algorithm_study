n, m = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
answer = 0

def make_combinations(phase, count, curr_val):
    global answer
    
    if count == m:
        answer = max(answer, curr_val)
        return

    if phase == n:
        return

    make_combinations(phase+1, count, curr_val)
    make_combinations(phase+1, count+1, curr_val ^ nums[phase])

make_combinations(0, 0, 0)
print(answer)