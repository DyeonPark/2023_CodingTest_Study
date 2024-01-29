'''
그냥 생각해보면 bfs로 풀면서 
- 4방향 탐색 후보 결정할 때 현재 노드 웨이트보다 적은 애를 선택하는 조건을 추가해주고
- 힙큐로 둬서 항상 더 가중치 적은 애가 우선적으로 탐색되도록 하면 될 것 같은데
- 탐색하면서는 moving 횟수가 아닌 현재까지의 가중치 summation 들고 이동하고.

- 아 문제 잘못읽었다 이게 가능한 모든 경로의 수를 구하는거구나

'''

def _print(graph):
    for g in graph:
        print(g, end = '\n')
    print()

def _init_():
    global graph
    graph = [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]]

def submit_1():
    '''
    initial approah 
    - just dfs
    - 경우의 수가 비효율적으로 많이 추가되므로 시간초과(이전 방문 여부 고려하지 않음, dp X)
    '''
    iteration = 0
    _init_()
    q = [(0, 0)]
    ans = 0
    while q:
        sx, sy = q.pop()
        if sx == n-1 and sy == m-1:
            ans+=1
        for dx, dy in move:
            iteration += 1; 
            x, y = sx+dx, sy+dy
            if 0<=x<n and 0<=y<m and graph[sx][sy] > graph[x][y]:      
                q.append((x, y))
    return ans, iteration

def with_visited():
    _init_()
    iteration = 0
    q = [(0, 0)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    ans = 0
    while q:
        sx, sy = q.pop()
        if sx == n-1 and sy == m-1:
            ans+=1
        for dx, dy in move:
            iteration += 1; 
            x, y = sx+dx, sy+dy
            if 0<=x<n and 0<=y<m and graph[sx][sy] > graph[x][y]:  
                if visited[x][y] > 0:
                    visited[x][y]+=1   
                    continue
                else:                  
                    visited[x][y] = visited[sx][sy]      
                q.append((x, y))

    return ans, iteration

def dfs(sx, sy):
    '''
    종료조건
    - 도착지점 ) 1 리턴
    - 이미 방문했던 지점 ) 해당 dp값 리턴
    4방향 탐색 -> 다음 탐색 노드의 dfs(x, y) 값 넣어줘야함 
    '''
    _print(dp)
    if sx==n-1 and sy == m-1:
        return 1
    if dp[sx][sy] != -1:
        return dp[sx][sy]
    
    path = 0
    for x, y in move:
        nx, ny = sx + x, sy + y
        if 0<=nx<n and 0<=ny<m and graph[sx][sy] > graph[nx][ny]:
            path += dfs(nx, ny)
    dp[sx][sy] = path
    return path


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dp = [[-1 for _ in range(m)] for _ in range(n)]

ans = dfs(0, 0)
print(ans)

