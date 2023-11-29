def dfs(x, y):
  # 현재 위치 방문 처리
  visited[x][y] = 1
  # 동서남북으로 이동
  for i in range(4):
    next_x = x + dx[i]
    next_y = y + dy[i]
    # 경계를 넘어가는지 배추가 있는지 확인
    # print("next_x", next_x, "next_y", next_y)
    if (0 <= next_x <= n - 1) and (
        0 <= next_y <=
        m - 1) and arr[next_x][next_y] and not visited[next_x][next_y]:
      dfs(next_x, next_y)  # 인접한 배추 방문 기록 남기기
  return


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for i in range(t):
  # m: 가로, n: 세로, k: 배추 개수
  m, n, k = map(int, input().split())
  # 배추밭
  arr = [[0 for _ in range(m)] for _ in range(n)]
  # 방문 기록
  visited = [[0 for _ in range(m)] for _ in range(n)]
  # 배추밭에 배추 기록
  for _ in range(k):
    a, b = map(int, input().split())
    arr[b][a] = 1
  # print(arr)
  # print(visited)
  cnt = 0  # 지렁이 수
  # 0,0 부터 시작해서 인접한 배추로 연결된 배추 그룹이 몇 개인지 확인
  for i in range(n):
    for j in range(m):
      # 배추 있는지, 방문한 적 있는지 확인
      if arr[i][j] and (not visited[i][j]):
        # 배추 있고, 방문한 적 없으면 지렁이 추가
        cnt += 1
        # print(f"i{i}, j{j}, cnt{cnt}")
        # dfs로 인접한 배추들 방문 처리하기
        dfs(i, j)
        # print(visited)

  print(cnt)
