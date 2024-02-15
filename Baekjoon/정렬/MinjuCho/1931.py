# 문제 풀이 링크: https://velog.io/@cuppizza/백준-1931-회의실-배정-파이썬-C-그리디-정렬
# 실행 시간: 284ms 메모리: 59068KB
import sys
input = sys.stdin.readline
n = int(input().strip())
demand = []
for i in range(n):
  demand.append(list(map(int, input().strip().split())))
  
demand.sort(key=lambda x:(x[1], x[0]))
result = [demand[0]]

for i in range(1, n):
  if result[-1][1] <= demand[i][0]:
    result.append(demand[i])
print(len(result))