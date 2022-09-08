# 변수 선언 및 입력
n, t = tuple(map(int, input().split()))
l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    # Step 1
    # 왼쪽에서 가장 오른쪽에 있는 숫자를 따로 temp값에 저장
    temp = l[n - 1]
    
    # Step 2
    # 왼쪽에 있는 숫자들을 완성합니다. 
    # 벨트를 기준으로 오른쪽에서부터 채워넣고, 
    # 맨 왼쪽 숫자는 아래에서 가져옴.
    for i in range(n - 1, 0, -1):
        l[i] = l[i - 1]
    l[0] = d[n - 1]
    
    # Step 3
    # 오른쪽에 있는 숫자들을 완성합니다. 
    # 벨트를 기준으로 마찬가지로 오른쪽에서부터 채워넣고,
    # 맨 왼쪽 숫자는 이전 단계에서 미리 저장해놨던 temp값을 가져옴.
    temp2 = r[n - 1]
    for i in range(n - 1, 0, -1):
        r[i] = r[i - 1]
    r[0] = temp
    
    # Step 4
    # 아래에 있는 숫자들을 완성합니다. 
    # 마찬가지로 벨트를 기준으로 오른쪽에서부터 채워넣고,
    # 맨 왼쪽 숫자는 이전 단계에서 미리 저장해놨던 temp값을 가져옴.
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp2
    
# 출력
for elem in l:
    print(elem, end=" ")
print()

for elem in r:
    print(elem, end=" ")
print()

for elem in d:
    print(elem, end=" ")