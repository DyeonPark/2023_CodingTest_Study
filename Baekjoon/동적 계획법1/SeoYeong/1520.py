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

def submit_1():
    q = [(0, 0)]
    ans = 0
    while q:
        sx, sy = q.pop()
        if sx == n-1 and sy == m-1:
            ans+=1
        for dx, dy in move:
            x, y = sx+dx, sy+dy
            if 0<=x<n and 0<=y<m and graph[sx][sy] > graph[x][y]:                  
                q.append((x, y))
    return ans
                

# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
n, m, graph = 4, 5, [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]]

ans = submit_1()
print('ans : ', ans)
