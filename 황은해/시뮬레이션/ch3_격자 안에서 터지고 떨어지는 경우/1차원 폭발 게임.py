# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
numbers = [int(input()) for _ in range(n)]


# 주어진 시작점에 대하여 부분 수열의 끝 위치를 반환합니다.
def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx + 1, len(numbers)):
        if numbers[end_idx] != curr_num:
            return end_idx - 1
        
    return len(numbers) - 1


while True:
    did_explode = False
    curr_idx = 0
    
    while curr_idx < len(numbers):
        end_idx = get_end_idx_of_explosion(curr_idx, numbers[curr_idx])
        
        if end_idx - curr_idx + 1 >= m:
            # 연속한 숫자의 개수가 m개 이상이면
            # 폭탄이 터질 수 있는 경우 해당 부분 수열을 잘라내고
            # 폭탄이 터졌음을 기록해줍니다.
            del numbers[curr_idx:end_idx + 1]
            did_explode = True
        else:
            # 주어진 시작 원소에 대하여 폭탄이 터질 수 없는 경우
            # 다음 원소에 대하여 탐색하여 줍니다.
            curr_idx = end_idx + 1

    if not did_explode:
        break

print(len(numbers))
for number in numbers:
    print(number)