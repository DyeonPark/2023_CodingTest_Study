"""
n*n board,  
- 높이 1, 길이 L인 경사로 놓아서 path 만들 수 있다.
- path 는 한 행/열 전부 같은 높이 또는 경사로 놓아서 높이 같아지는 경우다.
- 경사로는 경사면이 완벽하게 지면에 닿아야 하고, L개의 칸이 같은 높이로 이어져있어야한다.

ex1. L=2
ex2. L=2
ex3. L=3
ex4. L=1
"""
    
def is_this_path(i):
    slobe = [] # 이미 경사로 놓은 칸인지 확인하기 위한 배열 
    for j in range(1, n):
        # 왼쪽 값이랑 같으면 다음 진행
        if board[i][j-1] == board[i][j]: pass
        else:
            # 왼쪽 값이랑 차이
            diff = board[i][j-1]-board[i][j]
            # 1 차이 나는 경우 경사로를 놔서 길을 만들 수 있는지 확인
            if abs(diff) == 1:
                # left<right 인 경우 이전 값 확인, left>right인 경우 이후 값 확인해야함. 이를 위한 조정값
                adjust_val = 1 if diff == -1 else 0
                # 같은지 확인할 비교 기준값
                standard_val = board[i][j-adjust_val]
                # 이전/이후 값 같은지 확인
                for k in range(h):
                    nj = j + (k+adjust_val)*diff
                    # 범위 밖이거나 이미 경사로 놨거나 기준 값이랑 다르면 길 실패
                    if nj<0 or nj>=n or nj in slobe or board[i][nj] != standard_val: return False
                    slobe.append(nj)
            # 왼쪽 값이랑 차이가 1보다 큰 경우 길 실패
            else:
                return False
    return True
            
def find_path():
    global ans
    for i in range(n):
        # 각 가로 한 줄씩 길 되는지 확인
        if is_this_path(i): ans+=1
    

n, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
find_path()
board = list(map(list, zip(*board)))
find_path()
print(ans)