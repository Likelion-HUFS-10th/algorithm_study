n = int(input())
arr = [int(input()) for _ in range(n)]
remove_list = [list(map(int, input().split())) for _ in range(2)]

for (s, e) in remove_list:
    arr = arr[0:s-1] + arr[e:]
print(len(arr))
for ele in arr:
    print(ele)