n, m, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
pieces = [1 for _ in range(k)]

ans = 0


def calc():
    score = 0
    for piece in pieces:
        score += (piece >= m)

    return score


def find_max(cnt):
    global ans

    ans = max(ans, calc())

    if cnt == n:
        return

    for i in range(k):

        if pieces[i] >= m:
            continue

        pieces[i] += nums[cnt]
        find_max(cnt + 1)
        pieces[i] -= nums[cnt]


find_max(0)
print(ans)