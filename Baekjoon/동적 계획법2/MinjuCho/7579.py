import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
m = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))
s = sum(c)
dp = [[0 for _ in range(s+1)] for __ in range(N)]
for i in range(N):
    for j in range(s+1):
        if j - c[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i]] + m[i])
        dp[i][j] = max(dp[i][j], dp[i-1][j])
for j in range(s+1):
    if dp[N-1][j] >= M:
        print(j)
        break
