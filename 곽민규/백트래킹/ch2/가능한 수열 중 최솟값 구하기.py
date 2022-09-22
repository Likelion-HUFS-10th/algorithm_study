from math import ceil
import sys
n = int(input())
nums = [4, 5, 6]
result, answer = [], []

def print_answer():
    for ele in result:
        print(ele, end="")


# 중복 부분수열 최대 길이 = n // 2
flag = False
def add(phase):
    global flag
    if phase == n+1:
        print_answer()
        sys.exit(0)
        return

    for num in nums:
        for i in range(ceil(len(result)/2)):
            # print(f'i:{i}')
            s1, e1 = len(result)-(2*i+1), len(result)-i
            s2, e2 = e1, len(result)
            # print(result[s1:e1], result[s2:e2]+[num])
            if result[s1:e1] == result[s2:e2]+[num]:
                flag = True
                break
            else:
                flag = False
        if flag:
            continue
        result.append(num)
        # print(f'result:{result}')
        add(phase+1)
        result.pop()
    
    return

add(1)

# print(answer)
# 4
# 4 -> 1 (4:4x) 5 or 6
# 45 -> 1 (5:5x list[-1:0] == list[0:0]+num) 4 or 6
# 454 -> 2 (4:4x 45:45x list[-3:-1] == list[-1:0]+num) 6
# 4546 -> 2 (6:6x 54:64(65)o) 4 or 5
# 45464 -> 3 (4:4x 46:46x 454:645o list[-5:-2] == list[-2:0]+num) 5
# 454645 -> 3 (5:5x 64:54(56)o 546:454(456)o) -> 4 or 6
# 4546454 -> (4:4x 45:45x 464:546o 4546:4546x) -> none
# list[길이-1:길이] == list[길이:길이]+num
# list[길이-3:길이-1] == list[길이-1:길이]+num
# list[길이-5:길이-2] == list[길이-2:길이]+num