n,t=map(int, input().split())
upper_belt=list(map(int, input().split()))
lower_belt=list(map(int, input().split()))[::-1]


for _ in range(t):
    lower_belt.append(upper_belt.pop())
    upper_belt.insert(0, lower_belt.pop(0))
print(*upper_belt)
print(*lower_belt[::-1])
