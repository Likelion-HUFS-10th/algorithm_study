n, m = map(int, input().split())
col = [int(input()) for _ in range(n)]

def listing():
    tmp = 0
    result = []
    for num in col:
        # print(f'num:{num}')
        # print(f'tmp:{tmp}')
        # print(f'result:{result}')
        li = []
        if tmp == num: # 이전 값과 비교해서 같으면
            li.extend(result.pop())
            li.append(num) # 이전 값과 동일한 현재 값도 li에 추가
            # print(li)
            result.append(li) # li를 result에 갱신 
            # print(result)
        else: # 현재와 이전 값이 다른 경우 : 시퀀스 시작 전, 시퀀스 종료 이후
            tmp = num # 이전 값을 현재 값으로 초기화
            result.append([num])
            # print(result)
    return result
    
def conditional_explode(li, m):
    global col
    r = []
    for num in li:
        if len(num) < m:
            r.extend(num)
    # print(r)
    if col == r:
        return False
    else:
        col = r
        return True


def simulation():
    li = listing()
    # print(li)
    return conditional_explode(li, m)

while True:
    simulation()
    if not simulation():
        break

print(len(col))
for num in col:
    print(num)
