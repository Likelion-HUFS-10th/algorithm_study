# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
numbers = [
    int(input())
    for _ in range(n)
]


# 주어진 시작점에 대하여
# 부분 수열의 끝 위치를 반환합니다.
def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx + 1, len(numbers)):
        if numbers[end_idx] != curr_num:
            return end_idx - 1
        
    return len(numbers) - 1


while True:
    did_explode = False
    
    for curr_idx, number in enumerate(numbers):
        # 각 위치마다 그 뒤로 폭탄이 m개 이상 있는지 확인합니다.
			
		# 이미 터지기로 예정되어있는 폭탄은 패스합니다.
        if number == 0:
            continue
        # curr_idx로부터 연속하여 같은 숫자를 갖는 폭탄 중 
		# 가장 마지막 위치를 찾아 반환합니다.
        end_idx = get_end_idx_of_explosion(curr_idx, number)
        
        if end_idx - curr_idx + 1 >= m:
            # 연속한 숫자의 개수가 m개 이상인 경우 폭탄이 터졌음을 기록해줍니다.
            # 터져야 할 폭탄들에 대해 터졌다는 의미로 0을 채워줍니다.
            numbers[curr_idx:end_idx + 1] = [0] * (end_idx - curr_idx + 1)
            did_explode = True
        
    # 폭탄이 터진 이후의 결과를 계산하여 반영해줍니다.
    numbers = list(filter(lambda x: x > 0, numbers))
    
    # 더 이상 폭탄이 터지지 않는다면 종료합니다.
    if not did_explode:
        break

print(len(numbers))
for number in numbers:
    print(number)