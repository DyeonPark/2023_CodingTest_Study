# 문제 풀이 링크: https://velog.io/@cuppizza/백준-7562-나이트의-이동-파이썬-C
# 실행 시간: 1292ms 메모리: 36996KB
from queue import deque
import sys
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 1, 2]
dy = [-2, -1, 1, 2, -2, -1, 2, 1]

def bfs():
    # input
    n = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())

    if sx == ax and sy == ay:
        print(0)
        return
    
    graph = [[0 for __ in range(n)] for _ in range(n)]
    # bfs
    graph[sx][sy] = 1
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x+dx[d]
            ny = y+dy[d]
            if nx == ax and ny == ay:
                print(graph[x][y])
                return
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != 0:
                continue
            q.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
            
testCase = int(input())
while testCase:
    testCase -= 1
    bfs()
