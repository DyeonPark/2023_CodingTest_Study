import heapq
def dijkstra(start, end):
    # 현재 노드에서 가장 가까운데 먼저 방문탐색
    hq = []
    heapq.heappush(hq, (0, tuple([start]), start)) # 현재 거리, 현재 노드까지 경로, 현재 노드
    distance = [inf for _ in range(n+1)]
    distance[start] = 0
    while hq:
        sw, spath, sv = heapq.heappop(hq)
        if sv == end: return sw, spath
        if distance[sv] < sw: continue
        for nw, nv in graph[sv]:
            w = distance[sv] + nw
            if w < distance[nv]:
                distance[nv] = w
                heapq.heappush(hq, (w, spath+(nv,), nv))
    return 

def dijkstra_without_path(start, end):
    hq = []
    heapq.heappush(hq, (0, start))
    distance = [inf for _ in range(n+1)]
    distance[start] = 0
    while hq:
        sw, sv = heapq.heappop(hq)
        if sv == end : return sw
        if distance[sv] < sw: continue
        for nw, nv in graph[sv]:
            w = distance[sv] + nw
            if w < distance[nv]:
                distance[nv] = w
                heapq.heappush(hq, (w, nv))

def solution():
    # t 각각에 대해 s->t optimal_path 받아와서 (g, h) 있으면 result에 append
    result = []
    for t in arrival_candidates:
        w1, p1 = dijkstra(s, t)
        if (g, h) in p1:
            result.append(t)
        else:
            w2 = 0
            if g == t: 
                w2 += dijkstra_without_path(s, g)
            elif h == t:
                w2 += dijkstra_without_path(s, g) + dijkstra_without_path(h, t)
            else:
                w2 += dijkstra_without_path(s, g) + dijkstra_without_path(h, t) + g_h
            if w2 <= w1:
                result.append(t)
    print(' '.join(map(str, sorted(result))))

testcase = int(input())
inf = 1e10
for _ in range(testcase):
    n, m, t = map(int, input().split()) # 교차로 개수, 도로 개수, 목적지 후보 개수
    s, g, h = map(int, input().split()) # 출발지, 듀오가 g-h를 잇는 edge 지나감
    graph = [[] for _ in range(n+1)]    
    for _ in range(m):                 
        x, y, z = map(int, input().split()) # x-y 사이 길이 z짜리 양방향 도로 존재
        if (x, y) in [(g, h), (h, g)]:
            g_h = z
        graph[x].append((z, y))
        graph[y].append((z, x))
    # 목적지 후보들(t개)
    arrival_candidates = [int(input()) for _ in range(t)]

    solution()


"""

1
6 7 3
1 4 5
1 2 1
2 4 2
2 3 2
3 5 3
4 5 3
5 6 4
2 6 9
5
3
6
ans : 5 6

================

1
5 5 2
1 2 3
1 4 3
4 5 3
1 2 2
2 3 2
3 5 2
3
5
ans : 3 5

=================

1
4 4 1
1 3 4
1 2 3
2 4 4
1 3 4
3 4 3
4
ans : 4

================

1
5 4 2
1 2 3
1 2 1
2 3 1
3 4 1
2 5 1
4 5
ans : 4

==================

1
6 6 2
1 2 3
1 2 1
2 3 2
3 4 1
4 5 2
1 6 4
6 5 1
4
5
ans : 4

=============

3
5 5 1
1 3 5
1 2 1
2 4 2
2 3 2
3 5 3
4 5 3
5
5 5 1
1 4 5
1 2 1
2 4 2
2 3 2
3 5 3
4 5 3
5
6 7 3
1 4 5
1 2 1
2 4 2
2 3 2
3 5 3
4 5 3
5 6 4
2 6 9
5
3
6
ans : 5 / 5 / 5 6

===============

1
3 3 1
1 2 3
1 3 1
2 3 1
1 2 2
2
ans : 2

================

1
4 4 1
1 1 3
1 2 1
1 3 3
3 4 1
2 4 1
3
ans : 3

==========

1
4 4 1
1 1 4
1 2 1
1 4 3
4 3 1
2 3 1
4
ans : 4

"""
