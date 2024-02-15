# pypy3 통과 python 3 시간초과
import sys, copy
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
dp = [[[0]*3 for _ in range(M)] for __ in range(N)]
for y in range(M):
    for z in range(3):
        dp[0][y][z] = arr[0][y]
for x in range(1,N):
    for y in range(M):
        for z in range(3):
            if (y==0 and z==0) or (y==M-1 and z==2):
                dp[x][y][z] = int(1e9)
            else:
                a=int(1e9)
                b=int(1e9)
                c=int(1e9)
                if y>=1:
                    a=min(dp[x-1][y-1][1] , dp[x-1][y-1][2])
                b=min(dp[x-1][y][0] , dp[x-1][y][2])
                if y<=M-2:
                    c=min(dp[x-1][y+1][0] , dp[x-1][y+1][1])
                if z==0:
                    dp[x][y][0] = arr[x][y] + a
                elif z==1:
                    dp[x][y][1] = arr[x][y] + b
                else:
                    dp[x][y][2] = arr[x][y] + c

print(min(dp[-1][y][z] for y in range(M) for z in range(3)))
