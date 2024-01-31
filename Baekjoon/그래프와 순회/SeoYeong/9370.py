def dijkstra(start, end):
    # 현재 노드에서 가장 가까운데 먼저 방문탐색
    import heapq
    hq = []
    heapq.heappush(hq, (0, [start], start)) # 현재 거리, 현재 노드까지 경로, 현재 노드
    distance = [inf for _ in range(n+1)]
    distance[start] = 0
    while hq:
        sw, spath, sv = heapq.heappop(hq)
        print('\n')
        # print(sw, spath, sv)
        if sv == end: return spath
        if distance[sv] < sw: continue
        for nw, nv in graph[sv]:
            print(f"({sw}, {spath}, {sv}), ({nw}, {nv})")
            w = distance[sv] + nw
            next_path = spath
            if w < distance[nv]:
                distance[nv] = w
                next_path.append(nv)
                heapq.heappush(hq, (w, next_path, nv))
    return 
            
def solution():
    # t 각각에 대해 optimal_path 받아와서 (g, h) 있으면 result에 append
    result = []
    for t in arrival_candidates:
        path = dijkstra(s, t)
        print(f"get optimal path from {s} to {t} : {path}")
        for i in range(len(path)-1):
            if (path[i]==g and path[i+1]==h) or (path[i]==h and path[i+1]==g):
                result.append(t)
    print(result)

testcase = int(input())
inf = 1e10
for _ in range(testcase):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((z, y))
        graph[y].append((z, x))
    arrival_candidates = [int(input()) for _ in range(t)]

    solution()


