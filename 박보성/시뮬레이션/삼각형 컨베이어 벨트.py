n,t=map(int, input().split())
upper_belt=list(map(int, input().split()))
middle_belt=list(map(int, input().split()))
lower_belt=list(map(int, input().split()))[::-1]

for _ in range(t):
    middle_belt.insert(0, upper_belt.pop())
    lower_belt.append(middle_belt.pop())
    upper_belt.insert(0, lower_belt.pop(0))

print(*upper_belt)
print(*middle_belt)
print(*lower_belt[::-1])
