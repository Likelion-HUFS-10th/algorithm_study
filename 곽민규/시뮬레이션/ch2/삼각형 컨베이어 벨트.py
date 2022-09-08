n, t = map(int, input().split())
first_belt = list(map(str, input().split()))
second_belt = list(map(str, input().split()))[::-1]
third_belt = list(map(str, input().split()))[::-1]

for _ in range(t):
    second_belt.append(first_belt.pop())
    third_belt.append(second_belt.pop(0))
    first_belt.insert(0, third_belt.pop(0))
print(*first_belt)
print(*second_belt[::-1])
print(*third_belt[::-1])