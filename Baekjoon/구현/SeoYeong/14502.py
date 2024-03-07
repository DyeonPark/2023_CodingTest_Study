def count_clean():
    """
    spread virus in given graph(after construct 3 walls)
    return the number of clean area
    """
    import copy
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    stack = copy.deepcopy(virus)
    visited = set()
    spread_num = 0
    while stack:
        vx, vy = stack.pop()
        for dx, dy in move:
            nx, ny = vx+dx, vy+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and (nx, ny) not in visited :
                spread_num+=1
                visited.add((nx, ny))
                stack.append((nx, ny))
    
    return spread_num
        

def trial_one_brute():
    """
    2 좌표, 0 좌표 받기
    1. 전체 0 좌표 중 3개 선택 (xC3)
    2. xC3개의 경우의 수에 대해 바이러스 spread
    3. 안전구역 넓이 최댓값 계속 업데이트
    """
    from itertools import combinations

    ans = len(empty) # 각 경우에서 가장 적게 퍼진 개수 count
    for (x1, y1), (x2, y2), (x3, y3) in combinations(empty, 3):
        graph[x1][y1], graph[x2][y2], graph[x3][y3] = 1, 1, 1
        spread_num = count_clean()
        if ans > spread_num: 
            ans = spread_num
            # print(f"({x1},{y1}),({x2},{y2}),({x3},{y3}) => {spread_num}")
        graph[x1][y1], graph[x2][y2], graph[x3][y3] = 0, 0, 0

    return len(empty)-3-ans

n, m = map(int, input().split())
graph, virus, empty = [], [], []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2: virus.append([i, j])
        elif graph[i][j] == 0: empty.append([i, j])

# print(f"input - virus={virus}, empty 개수={len(empty)}")

ans = trial_one_brute()
print(ans)