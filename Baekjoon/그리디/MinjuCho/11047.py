# 문제 풀이 링크: https://velog.io/@cuppizza/백준-11047-동전-0-C-파이썬-그리디
# 실행 시간: 40ms 메모리: 31120KB
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input().strip()))
result = 0
for i in range(n-1, -1, -1):
    result += k // coins[i]
    k %= coins[i]
print(result)
