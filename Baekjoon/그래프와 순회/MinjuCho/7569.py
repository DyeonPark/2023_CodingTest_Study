# 문제 풀이 링크: https://velog.io/@cuppizza/백준-7569-토마토-C-파이썬
# 방문 여부 따로 저장 X, 저장된 거리값으로 방문 여부 확인 -> 실행 시간 및 메모리 절약
# 실행 시간 : 3840ms 메모리: 52860KB
from queue import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
next_visit = deque()
tomato = []
for i in range(h):
    temp = []
    for j in range(n):
        row = list(map(int, input().strip().split()))
        for k in range(m):
            if row[k] == 1:
                next_visit.append((i, j, k))
        temp.append(row)
    tomato.append(temp)

dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

while next_visit:
    z, x, y = next_visit.popleft()
    for d in range(6):
        nz = z+dz[d]
        nx = x+dx[d]
        ny = y+dy[d]
        if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if tomato[nz][nx][ny] != 0:
            continue
        tomato[nz][nx][ny] = tomato[z][x][y] + 1
        next_visit.append((nz, nx, ny))
result = -1
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 0:
                print(-1)
                exit(0)
        result = max(result, max(tomato[z][x]))
print(result - 1)

# 입력과 동시에 첫 방문 좌표 저장 -> 실행 시간 및 메모리 절약
# 실행 시간 : 3952ms 메모리: 61824KB
from queue import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
visited = [[[0] * m for _ in range(n)] for __ in range(h)]
next_visit = deque()
tomato = []
for i in range(h):
    temp = []
    for j in range(n):
        row = list(map(int, input().strip().split()))
        for k in range(m):
            if row[k] == 1:
                next_visit.append((i, j, k))
                visited[i][j][k] = 1
        temp.append(row)
    tomato.append(temp)

dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

while next_visit:
    z, x, y = next_visit.popleft()
    for d in range(6):
        nz = z+dz[d]
        nx = x+dx[d]
        ny = y+dy[d]
        if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if tomato[nz][nx][ny] != 0 or visited[nz][nx][ny] == 1:
            continue
        visited[nz][nx][ny] = 1
        tomato[nz][nx][ny] = tomato[z][x][y] + 1
        next_visit.append((nz, nx, ny))
result = -1
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 0:
                print(-1)
                exit(0)
        result = max(result, max(tomato[z][x]))
print(result - 1)

# bfs로 최단 거리 구하듯 거리 저장, 방문은 따로 처리, 최장 거리값을 구하여 날짜 수를 센다.
# 실행 시간 : 3968ms 메모리: 61956KB

from queue import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for __ in range(h)]
visited = [[[0] * m for _ in range(n)] for __ in range(h)]
next_visit = deque()
dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 1:
                next_visit.append((z, x, y))
                visited[z][x][y] = 1
while next_visit:
    z, x, y = next_visit.popleft()
    for d in range(6):
        nz = z+dz[d]
        nx = x+dx[d]
        ny = y+dy[d]
        if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if tomato[nz][nx][ny] != 0 or visited[nz][nx][ny] == 1:
            continue
        visited[nz][nx][ny] = 1
        tomato[nz][nx][ny] = tomato[z][x][y] + 1
        next_visit.append((nz, nx, ny))
result = -1
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato[z][x][y] == 0:
                print(-1)
                exit(0)
        result = max(result, max(tomato[z][x]))
print(result - 1)

# 시간 초과 풀이 (bfs임에도 큐 깊은 복사 때문, 방문을 2로 처리하고 따로 거리값을 구하자 않음)
# from queue import deque
# from copy import deepcopy
# import sys
# input = sys.stdin.readline
# m, n, h = map(int, input().strip().split())
# tomato = []
# next_visit = deque()
# for i in range(h):
#     temp = []
#     for j in range(n):
#         row = list(map(int, input().strip().split()))
#         for k in range(m):
#             if row[k] == 1:
#                 next_visit.append((i, j, k))
#         temp.append(row)
#     tomato.append(temp)
# dz = [0, 0, 0, 0, -1, 1]
# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, -1, 1, 0, 0]

# result = -1
# while next_visit:
#     result += 1
#     cur_visit = deepcopy(next_visit)
#     next_visit = deque()
#     while cur_visit:
#         z, x, y = cur_visit.popleft()
#         if tomato[z][x][y] != 0:
#             continue
#         tomato[z][x][y] = 1
#         for d in range(6):
#             nz = z+dz[d]
#             nx = x+dx[d]
#             ny = y+dy[d]
#             if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if tomato[nz][nx][ny] != 0:
#                 continue
#             next_visit.append((nz, nx, ny))

# for z in range(h):
#     for x in range(n):
#         for y in range(m):
#             if tomato[z][x][y] == 0:
#                 print(-1)
#                 exit(0)
# print(result)