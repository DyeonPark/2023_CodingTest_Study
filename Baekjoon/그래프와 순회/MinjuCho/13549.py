# 문제 풀이 링크: https://velog.io/@cuppizza/백준-13549-숨바꼭질-3-C-파이썬-BFS-최단거리
# 실행 시간: 180ms 메모리: 41124KB
from queue import deque
def teleport(cur, sec):
    while cur<=100000 and visited[cur] == -1:
        q.append(cur)
        visited[cur] = sec
        if cur == K:
            print(visited[cur])
            exit()
        cur *= 2
        
N, K = map(int, input().strip().split())
visited = [-1 for _ in range(100002)]
d = [-1, 1]
q = deque()

q.append(N)
visited[N] = 0
teleport(N*2, 0)
while q:
    cur = q.popleft()
    for offset in d:
        if cur+offset < 0 or cur+offset >=100002:
            continue
        if visited[cur+offset] != -1:
            continue
        q.append(cur+offset)
        visited[cur+offset] = visited[cur] + 1
        teleport((cur+offset)*2, visited[cur+offset])
print(visited[K])
