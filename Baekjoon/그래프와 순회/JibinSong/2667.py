def dfs(x, y):
  # 방문 기록
  visited[x][y] = 1
  # 동서남북 확인
  for i in range(4):
    next_x = x + dx[i]
    next_y = y + dy[i]
    # 경계를 넘지 않는지, 배추가 있는지 확인
    # print("x, y", next_x, next_y)
    if 0 <= next_x <= n - 1 and 0 <= next_y <= n - 1 and arr[next_x][
        next_y] and not visited[next_x][next_y]:
      num_home[-1] += 1
      dfs(next_x, next_y)

  return


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
# 지도
arr = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
# print("visited", visited)
# 단지 수
cnt = 0
# 집 개수 리스트
num_home = []

# 지도 0,0부터 순회하며 연결된 집 개수 세기
for i in range(n):
  for j in range(n):
    # 집이 있고, 이전에 방문한 적이 없으면,
    if (not visited[i][j]) and arr[i][j]:
      # 단지 개수 세기
      cnt += 1
      num_home.append(1)
      # print(f"i:{i}, j:{j}, num_home", num_home)
      dfs(i, j)

print(cnt)
num_home.sort()
for i in num_home:
  print(i)
