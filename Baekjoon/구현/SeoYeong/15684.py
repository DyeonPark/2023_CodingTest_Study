"""
세로선 개수 n, 가로선 개수 m, 세로선마다 가로선을 놓을 수 있는 위치 h
for m : 가로선 정보 (a, b : b~b+1번 세로선을 a번 점선 위치에서 연결했다는 뜻)

가로선을 추가해서 i번 세로선이 i 번이 나오도록 하려고 할때,추가해야하는 가로선 개수 최솟값?
# pypi 로 제출 시 맞음
"""
def is_start_end_same() -> bool:
    for i in range(n):
        start_num = i
        for j in range(h):
            # 지금 i가 각 start point 즉 열 element임
            # [jj[start_num] 봐야됨
            if ladder[j][start_num] == 1: start_num+=1
            elif ladder[j][start_num-1] == 1: start_num -=1
        if start_num != i: return False
    return True

def dfs(x, y, cnt):
    """ backtracking """
    global ans
    # if (x, y, cnt) in visited: return
    # visited.add((x, y, cnt))
    # 가로선을 현 시점 최솟값인 ans보다 많이 만듬 : 이후 학인할 필요 X
    if ans <= cnt : return
    # 현 cnt가 정답이 될 수 있는 경우는 지금 사다리 놔본 상태에서 is_start_end_same 만족하는지 여부임
    if is_start_end_same(): 
        ans = min(ans, cnt)
        return
    if cnt == 3: return

    # 현재 x행부터 h-1까지, n-2까지
    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n-1):
        # for j in range(n-1): # 위의 방법으로 시간을 2212ms->1700ms 로 단축 가능
            if ladder[i][j] == 0:
                ladder[i][j] = 1
                dfs(i, j+2, cnt+1)
                ladder[i][j] = 0


n, m, h = map(int, input().split())
ladder = [[0 for _ in range(n)] for _ in range(h)]
ans = 4

for _ in range(m):
    a, b = list(map(int, input().split()))
    ladder[a-1][b-1] = 1

# visited = set()
dfs(0, 0, 0)
if ans == 4: print(-1)
else: print(ans)
