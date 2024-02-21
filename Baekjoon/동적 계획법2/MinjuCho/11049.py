import sys
input = sys.stdin.readline
N = int(input().strip())
matrix = [[]]
for i in range(1, N+1):
    matrix.append(list(map(int, input().strip().split())))
dp=[[0 for _ in range(N+1)] for __ in range(N+1)]
INF = int(1e9)
for i in range(1, N):
    j = 1
    while i+j <= N:
        dp[j][i+j] = INF
        for k in range(j, i+j):
            dp[j][i+j] = min(dp[j][i+j], dp[j][k] + dp[k+1][i+j] + matrix[j][0] * matrix[k][1] * matrix[i+j][1])
        j+=1
print(dp[1][N])
