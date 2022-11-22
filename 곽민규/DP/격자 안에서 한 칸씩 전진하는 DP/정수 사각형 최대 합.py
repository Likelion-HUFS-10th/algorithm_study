import sys

INT_MIN = -sys.maxsize

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

def initialize():
    dp[0][0] = a[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + a[i][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + a[0][i]

initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + a[i][j]
# print(dp)
ans = INT_MIN
for j in range(n):
    ans = max(ans, dp[n-1][j])

print(ans)