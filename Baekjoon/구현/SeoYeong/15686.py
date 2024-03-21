"""
치킨거리 = 가장 가까운 치킨집까지 거리
도시의 치킨거리 = 도시 내 각 집의 치킨 거리 합
distance between (x1, y1), (x2, y2) = abs(x1-x2)+abs(y1-y2)
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 2
0 빈칸, 1 집, 2 치킨집
살릴 치킨집 최대 m개 고르기
- 0개 선택, 1개 ..m개

처음에 각 집에 대해 각 치킨집에 대한 거리 계산해놓는게 낫나? - 이 경우 자료구조 어떻게 할건데?
- 조합에 따라 가장 가까운 치킨집이 없어질 수 있으니까
아니 반대로 각 치킨집에 대해서 가장 가까운 집 좌표값 갖고있는게 나을 것 같은데
- c1 : [d1, d2, d3, d4], c2:[d1, d2, d3, d4], ...


시간제한 1초면 모든 combination(심지어 comb 개수도 0부터 m까지 다 해봐야됨)다 하는거 시간초과날것
- 시간복잡도 줄일 수 있는 방법 고안 필요
- 
"""

from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 1e10

# [1] 치킨 전체 좌표값 받기
house, chicken = [], []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1: house.append((i, j))
        elif board[i][j] == 2: chicken.append((i, j))

h, c = len(house), len(chicken)
print(chicken) # [(1, 2), (2, 2), (4, 4)]

# 치킨집, 집 좌표 key, 고유 index 값 value인 사전 생성
chicken_idx_dic = {c: i for i, c in enumerate(chicken)}
house_idx_dic = {h: i for i, h in enumerate(house)}

# print(f"chicken index dic:{chicken_idx_dic}, house index dic:{house_idx_dic}")

# c*h 짜리 배열 만들어서 각 행에 i 번째 치킨집의 각 집까지의 거리 저장
chicken_house_distance = [[0 for _ in  range(h)] for _ in range(c)]
for (cx, cy) in chicken:
    for (hx, hy) in house:
        ci, hi = chicken_idx_dic[(cx, cy)], house_idx_dic[(hx, hy)]
        chicken_house_distance[ci][hi] = abs(cx-hx)+abs(cy-hy)

# print(f"chicken house distance array:\n{chicken_house_distance}")

# [2] 그 중 m개 선택하는 조합
for i in range(1, m+1): # 살리는 치킨집 개수
    comb = list(combinations(chicken, i))  # 해당 개수만큼 치킨집에서 선택하는 조합
    for c in comb:
        tmp = [chicken_house_distance[chicken_idx_dic[c[x]]] for x in range(i)]
        tmp2 = [min(x) for x in list(map(list, zip(*tmp)))]
        ans = min(ans, sum(tmp2))
print(ans)

    
