# 문제 풀이 링크: https://velog.io/@cuppizza/백준-2206-벽-부수고-이동하기-파이썬-C-BFS-최단거리
# 실행 시간: 7020ms 메모리: 195252KB
from queue import deque
N, M = map(int, input().split())

graph=[]
for i in range(N):
    graph.append(list(map(int, input())))

# offset
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
route = [[[0, 0] for _ in range(M)] for __ in range(N)]
route[0][0][0] = 1
# BFS
q = deque()
q.append((0,0,0))
while q:
    x, y, z = q.popleft()
    # 목표 지점 먼저 도착 시 출력
    if x == N-1 and y == M-1:
        print(route[x][y][z])
        exit()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        # 이동 가능, 방문 X
        if graph[nx][ny] == 0 and route[nx][ny][z] == 0:
            route[nx][ny][z] = route[x][y][z]+1
            q.append((nx, ny, z))
        # 벽, 벽 부수기 기회 O
        elif graph[nx][ny] == 1 and z == 0:
            route[nx][ny][1] = route[x][y][0]+1
            q.append((nx, ny, 1))
# 목표 지점까지 가능한 이동 경로가 없을 경우
print(-1)



## 벽 무제한으로 깨기 (틀린 풀이)
##from queue import deque
##N, M= map(int, input().split())
##graph = []
##for _ in range(N):
##    graph.append(list(input()))
##    
##dx = [-1, 1, 0, 0]
##dy = [0, 0, -1, 1]
##
##def makeBreak(x, y):
##    possible = []
##    for d in range(4):
##        nx = x+dx[d]
##        ny = y+dy[d]
##        if nx < 0 or nx >= N or ny < 0 or ny >= M:
##            continue
##        if int(graph[nx][ny]) >= 1:
##            continue
##        possible.append((nx, ny))
##
##    print("possible" , possible)
##    return possible
##
##
##q = deque()
##q.append((0, 0))
##graph[0][0] = '1'
##dis = 1
### DFS
##while len(q)!=0:
##    print("Q:",q)
##    x, y = q.pop()
##    dis += 1
##    for g in graph:
##        print(g)
##    print("-"*10)
##    for d in range(4):
##        Nx = x+dx[d]
##        Ny = y+dy[d]
##        if Nx < 0 or Nx >= N or Ny < 0 or Ny >= M:
##            continue
##        if int(graph[Nx][Ny]) > 1:
##            continue
##        elif int(graph[Nx][Ny]) == 0:
##            q.append((Nx, Ny))
##            graph[Nx][Ny] = str(int(graph[x][y])+1)
##        else:
##            possible = makeBreak(Nx, Ny)
##            if len(possible) > 0:
##                for px, py in possible:
##                    q.appendleft((px, py))
##                    graph[px][py] = str(int(graph[x][y])+2)
##                graph[Nx][Ny] = str(int(graph[x][y])+1)
##                dis += 1
##if int(graph[-1][-1]) == 0:
##    print(-1)
##else:
##    print(int(graph[-1][-1]))
