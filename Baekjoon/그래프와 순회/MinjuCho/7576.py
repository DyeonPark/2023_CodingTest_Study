# 문제 풀이 링크: https://velog.io/@cuppizza/백준-7576-토마토-C-파이썬
# 실행 시간: 4140ms 메모리: 106320KB
import copy
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [[0 for _ in range(m)] for __ in range(n)]
next_pos = []

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == -1:
            graph[i][j] = -1
        elif row[j] == 1:
            graph[i][j] = 1
            next_pos.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = -1
while next_pos:
    cur_pos = copy.deepcopy(next_pos)
    next_pos = []
    while cur_pos:
        x, y = cur_pos.pop()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                next_pos.append((nx, ny))
    cnt += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()

print(cnt)