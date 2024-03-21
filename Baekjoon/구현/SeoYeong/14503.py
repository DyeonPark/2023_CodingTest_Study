"""
현재 칸 청소되지 않은 경우 현재 칸 청소
동서남북 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
    2-1. 현재 방향 유지한 채로 한 칸 후진할 수 있는 경우 한 칸 후진, 1번으로
    2-2. 후진할 수 없다면(현재 방향 기준 뒤 칸이 벽) 멈춤
동서남북 4칸 중 청소되지 않은 빈칸이 있는 경우
    3-1. 반시계 방향으로 90도 회전
    3-2. 현재 방향 기준으로 양쪽 칸이 청소되지 않은 빈 칸인 경우 한칸 전진
    3-3. 1번으로

- 청소되지 않은 빈칸 과 청소된 빈칸을 구분해야한다.

"""
def _print(room):
    for i in range(len(room)):
        print()
        for j in range(len(room[0])):
            if (i, j) in log: print('A', end='')
            else: print(room[i][j], end='')
    print()

def bfs(n, m, r, c, d):
    from collections import deque

    answer = 0
    q = deque([(r, c)])
    while q:
        sx, sy = q.popleft()
        # 현재 칸 청소되지 않은 빈칸 -> 청소
        if room[sx][sy] == 0: 
            answer +=1
            room[sx][sy] = -1

        # 주변 4칸 청소되지 않은 빈칸 있는지 체크
        flag = False
        for dx, dy in dir_dic.values():
            nx, ny = sx+dx, sy+dy
            flag |= 0<=nx<n and 0<=ny<m and room[nx][ny]==0

        # 현재 칸 주변 4칸 다 1
        if not flag:
            # 현재 방향 유지한채로 한 칸 후진할 수 있는 경우 후진, 없으면 리턴
            nx, ny = sx + dir_dic[(d+2)%4][0], sy + dir_dic[(d+2)%4][1]
            if 0>nx or nx>=n or 0>ny or ny>=m or room[nx][ny] == 1:
                return answer
            else:
                q.append((nx, ny))
        else:
            while True:
                d = list(dir_dic.keys())[d-1] # 반시계 방향으로 90도 회전
                # 현재 방향 기준 앞이 0인 경우
                nx, ny = sx + dir_dic[d][0], sy + dir_dic[d][1]
                if 0<=nx<n and 0<=ny<m and room[nx][ny] == 0:
                    q.append((nx, ny))
                    break

    return answer

n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 로봇청소기 처음 좌표, 바라보는 방향 d = [북, 동, 남, 서]
dir_dic = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}

room = [list(map(int, input().split())) for _ in range(n)] # 1: 벽, 0: 청소되지 않은 빈칸
ans = bfs(n, m, r, c, d)
print(ans)