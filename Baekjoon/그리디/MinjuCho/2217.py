# 문제 풀이 링크: https://velog.io/@cuppizza/백준-2217-로프-C-파이썬-그리디-정렬
# 실행 시간: 140ms 메모리: 35364KB
import sys
input = sys.stdin.readline
n = int(input().strip())
ropes = []
for i in range(n):
    ropes.append(int(input().strip()))
ropes.sort()
result = 0
sum_ropes = 0
for i in range(n-1, -1, -1):
    sum_ropes += ropes[i]
    result = max(result, ropes[i] * (n-1-i+1))
print(result)
