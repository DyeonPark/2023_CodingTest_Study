# 문제 풀이 링크: https://velog.io/@cuppizza/백준-16928-뱀과-사다리-게임-C-파이썬-BFS-최단거리
# 실행 시간: 100ms 메모리: 36888KB
from queue import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
ladders = {}
snakes = {}
for i in range(n):
    x, y = map(int, input().strip().split())
    ladders[x] = y
for i in range(m):
    u, v = map(int, input().strip().split())
    snakes[u] = v
ladders_keys = set(ladders.keys())
snakes_keys = set(snakes.keys())
graph = [0 for _ in range(101)]
# BFS
q = deque([1])
graph[1] = 1
while q:
    cur = q.popleft()
    for i in range(1, 7):
        if cur + i <= 100 and graph[cur + i] == 0:
            graph[cur + i] = graph[cur] + 1
            if cur + i in ladders_keys and graph[ladders[cur + i]] == 0:
                graph[ladders[cur + i]] = graph[cur + i]
                q.append(ladders[cur + i])
                continue
            elif cur + i in snakes_keys and graph[snakes[cur + i]] == 0:
                graph[snakes[cur + i]] = graph[cur + i]
                q.append(snakes[cur + i])
                continue
            elif (cur + i in ladders_keys and graph[ladders[cur + i]] != 0) \
                 or (cur + i in snakes_keys and graph[snakes[cur + i]] != 0):
                continue
            q.append(cur + i)
print(graph[100] - 1)
