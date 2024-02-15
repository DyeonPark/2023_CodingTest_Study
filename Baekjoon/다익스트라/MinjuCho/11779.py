import sys
import heapq
input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
adj=[[] for _ in range (n+1)]
while m:
    m -= 1
    u, v, w = map(int, input().strip().split())
    adj[u].append((w, v))
st, en = map(int, input().strip().split())

d = [int(1e9) for _ in range(n+1)]
pre = [0 for _ in range(n+1)]
d[st] = 0
pq = []
heapq.heappush(pq, (0, st))
while pq:
    curW, curV = heapq.heappop(pq)
    if d[curV] != curW:
        continue
    for nextW, nextV in adj[curV]:
        if d[nextV] <= d[curV] + nextW:
            continue
        d[nextV] = d[curV] + nextW
        heapq.heappush(pq, (d[nextV], nextV))
        pre[nextV] = curV
path=[]
curPath = en
while curPath != st:
    path.append(curPath)
    curPath = pre[curPath]
path.append(curPath)
print(d[en])
print(len(path))
for i in range(len(path)-1, -1, -1):
    print(path[i], end = ' ')
