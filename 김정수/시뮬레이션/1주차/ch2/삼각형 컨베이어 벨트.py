n, t = tuple(map(int, input().split()))
l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    temp = l[n-1]

    for i in range(n-1, 0, -1):
        l[i] = l[i-1]
    l[0] = d[n-1]

    temp2 = r[n-1]
    for i in range(n-1,0,-1):
        r[i]=r[i-1]
    r[0] = temp

    for i in range(n-1,0,-1):
        d[i] = d[i-1]
    d[0] = temp2

for elem in l:
    print(elem, end=" ")
print()

for elem in r:
    print(elem, end=" ")
print()

for elem in d:
    print(elem, end=" ")