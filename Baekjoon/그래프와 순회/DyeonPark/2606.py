import sys
from collections import defaultdict, deque

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
visited = [False] * (N + 1) # 방문(감염) 정보를 저장

coms = defaultdict(list) # 연결 정보를 저장
for _ in range(int(input())):
  A, B = map(int, input().split())
  coms[A].append(B)
  coms[B].append(A)

queue = deque([1]) # 시작 
visited[1] = True

### BFS를 이용하는 경우
while queue:
  front = queue.popleft() # queue의 가장 앞 원소 front 가져오기
  connect_list = [i for i in coms[front]] # front와 연결된 컴퓨터 목록 가져오기

  for c in connect_list: # 연결된 컴퓨터 목록에 대해서 방문한 적이 없다면 전파
    if not visited[c]:
      visited[c] = True
      queue.append(c)

### DFS를 이용하는 경우
def dfs(k):
  visited[k] = True
  for c in coms[k]:
    if not visited[c]:
      dfs(c)

dfs(1)

# 결과 출력
print(sum(visited) - 1) # 1을 제외한 감염된 컴퓨터의 수