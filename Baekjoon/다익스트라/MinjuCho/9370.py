# 문제 풀이 링크: https://velog.io/@cuppizza/백준-9370-미확인-도착지-C-파이썬-다익스트라-최단경로
# 실행 시간: 316ms 메모리: 45476KB
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(st, distance):
    pq = []
    heapq.heappush(pq, (0, st))
    distance[st] = 0
    while pq:
        curW, curP = heapq.heappop(pq)
        if distance[curP] != curW:
            continue
        for nxtW, nxtP in adj[curP]:
            if distance[curP] + nxtW < distance[nxtP]:
                distance[nxtP] = distance[curP] + nxtW
                heapq.heappush(pq, (distance[nxtP], nxtP))
    return distance

T = int(input().strip())
while T:
    T-=1
    n, m, t = map(int, input().strip().split())
    s, g, h = map(int, input().strip().split())
    adj = [[] for _ in range(n+1)]
    while m:
        m-=1
        a, b, d = map(int, input().strip().split())
        adj[a].append((d, b))
        adj[b].append((d, a))
    dest = []
    while t:
        t-=1
        dest.append(int(input().strip()))
    S = [INF for _ in range(n+1)]
    G = [INF for _ in range(n+1)]
    H = [INF for _ in range(n+1)]
    S = dijkstra(s, S)
    G = dijkstra(g, G)
    H = dijkstra(h, H)
    for terminal in dest[:]:
        if S[g]+G[h]+H[terminal] != S[terminal] and S[h]+H[g]+G[terminal] != S[terminal]:
            dest.remove(terminal)
    for real_terminal in sorted(dest):
        print(real_terminal, end=' ')
    print()
