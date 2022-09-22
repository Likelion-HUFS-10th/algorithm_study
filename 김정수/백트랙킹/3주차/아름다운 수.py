n = int(input())
ans = 0
seq = list()

def is_beautiful():
    i = 0
    while i < n:
        if i + seq[i] - 1 >= n:
            return False
        for j in range(i, i+seq[i]):
            if seq[j] != seq[i]:
                return False

        i += seq[i]

    return True

def count_beautiful_seq(cnt):
    global ans

    if cnt == n:
        if is_beautiful():
            ans += 1
        return

    for i in range(1,5):
        seq.append(i)
        count_beautiful_seq(cnt+1)
        seq.pop()

count_beautiful_seq(0)
print(ans)