# 문제 풀이 링크: https://velog.io/@cuppizza/백준-2606-바이러스-파이썬-C
# 실행 시간: 104ms 메모리: 37268KB
from queue import deque
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    vertex, edge = map(int, input().split())
    graph[vertex].append(edge)
    graph[edge].append(vertex)
    
nodes = [False for _ in range(N+1)]
nodes[1] = True
result = 0
q = deque()
q.append(1)
while len(q)!=0:
    v = q.popleft()
    for edge in graph[v]:
        if nodes[edge] == False:
            result += 1
            nodes[edge] = True
            q.append(edge)
print(result)
