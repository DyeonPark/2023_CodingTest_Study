# 문제 풀이 링크: https://velog.io/@cuppizza/백준-1012-유기농-배추-C-파이썬
# 실행 시간: 120ms 메모리: 37872KB
from queue import deque
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
T = int(input())
while T:
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for __ in range(n)]
    pos = []
    # 배추 심기
    while k:
        y, x = map(int, input().split())
        graph[x][y] = 1
        pos.append((x, y))
        k-=1
    # 배추 좌표마다 DFS
    count = 0
    for posx, posy in pos:
        # 방문한 적 있으면 skip
        if graph[posx][posy] != 1:
            continue
        q = deque()
        q.append((posx, posy))
        while q:
            x, y = q.pop()
            graph[x][y] = 2
            for d in range(4):
                nx = x+dx[d]
                ny = y+dy[d]
                if nx < 0 or nx >=n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                else:
                    continue
        count += 1
    print(count)
    T -= 1
