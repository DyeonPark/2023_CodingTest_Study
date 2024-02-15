# 문제 풀이 링크 : https://velog.io/@cuppizza/백준-1260-DFS와-BFS-파이썬-C
# 실행 시간: 600ms 메모리: 37864KB
from queue import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
while M:
    M -= 1
    vertex, edge = map(int, input().split())
    graph[vertex].append(edge)
    graph[edge].append(vertex)
    
# 같은 방문 가능 정점은 작은 것부터
for i in range(N):
    graph[i+1].sort()
    
visited = [False for _ in range(N+1)]
q = deque()
q.append(V)
# DFS
while len(q)!=0:
    cur = q.pop()
    if visited[cur] == False:
        visited[cur] = True
        print(cur, end = ' ')
    # 같은 방문 가능 정점 스택 순서로 삽입
    for idx in range(len(graph[cur])-1, -1, -1):
        if visited[graph[cur][idx]] == False:
            q.append(graph[cur][idx])
print()

visited = [False for _ in range(N+1)]
q.append(V)
# BFS
while len(q)!=0:
    cur = q.popleft()
    if visited[cur] == False:
        visited[cur] = True
        print(cur, end = ' ')
    for v in graph[cur]:
        if visited[v] == False:
            q.append(v)
