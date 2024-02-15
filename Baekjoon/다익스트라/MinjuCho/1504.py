# 문제 풀이 링크: https://velog.io/@cuppizza/백준-1504-특정한-최단-경로-C-파이썬-다익스트라
# 실행 시간: 588ms 메모리: 4268KB
import sys
import heapq
input = sys.stdin.readline
N, E = map(int, input().strip().split())
adj = [[] for _ in range(N+1)]
while E:
    E-=1
    a, b, c = map(int, input().strip().split())
    adj[a].append((c, b))
    adj[b].append((c, a))
v1, v2 = map(int, input().strip().split())

def dijkstra(route):
    mini = 0
    for i in range(3):
        st = route[i]
        en = route[i+1]
        d = [int(1e9) for _ in range(N+1)]
        d[st] = 0
        heap = []
        heapq.heappush(heap, (0, st))
        while heap:
            curW, cur = heapq.heappop(heap)
            if d[cur] != curW:
                continue
            for nxtW, nxt in adj[cur]:
                if d[nxt] <= d[cur] + nxtW:
                    continue
                d[nxt] = d[cur] + nxtW
                heapq.heappush(heap, (d[nxt], nxt))
        if d[en] == int(1e9):
            mini = int(1e9)
            return mini
        mini += d[en]
    return mini

r1 = [1, v1, v2, N]
min1 = dijkstra(r1)
r2 = [1, v2, v1, N]
min2 = dijkstra(r2)

if min1 == int(1e9) and min2 == int(1e9):
    print(-1)
elif min1 <= min2:
    print(min1)
else:
    print(min2)
