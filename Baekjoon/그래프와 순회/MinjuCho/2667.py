# 문제 풀이 링크: https://velog.io/@cuppizza/백준-2667-단지번호붙이기-파이썬-C
# 실행 시간: 96ms 메모리: 37048KB
# 1인 좌표만 따로 기록, DFS, 방문한 좌표는 단지수+1로 만들기, 단지 수는 변수 따로
from queue import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[0 for __ in range(N)] for _ in range(N)]
pos = {}
# 2차원 그래프 생성 시 집 좌표 저장
for i in range(N):
    row = list(map(int, input().strip()))
    for j in range(N):
        graph[i][j] = row[j]
        if row[j] == 1:
            pos[(i, j)] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
houses = []
num = 2
for px, py in pos.keys():
    # 방문한 적 없을 때만 단지 수 매기기
    if graph[px][py] != 1:
        continue
    count = 0
    q = deque()
    q.append((px, py))
    while q:
        x, y = q.pop()
        # 방문한 적 없을 때만 집의 수 세기
        if graph[x][y] != 1:
            continue
        graph[x][y] = num
        count += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] != 1:
                continue
            q.append((nx, ny))
    num += 1
    houses.append(count)
print(num - 2)
houses.sort()
for house in houses:
    print(house)

# 실행 시간: 96ms 메모리: 37872KB
# 모든 좌표 검색, BFS, 방문한 좌표는 0으로 만들기, 단지 수는 배열 길이로
from queue import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
houses = []
for px in range(N):
    for py in range(N):
        # 방문한 적 없을 때만 단지 수 매기기
        if graph[px][py] != 1:
            continue
        q = deque()
        q.append((px, py))
        graph[px][py] = 0
        count = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if graph[nx][ny] == 1:
                    # 방문한 적 없을 때만 집의 수 세기
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    count += 1
        houses.append(count)
houses.sort()
print(len(houses))
for house in houses:
    print(house)
