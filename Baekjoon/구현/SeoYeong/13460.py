""" Probelm Statement
. 빈칸, # 장애물(공 이동 불가), 0 구멍 R 빨간구슬위치 B 파란구슬위치
빨간 구슬만 구멍에서 빼낼 수 있을 때까지 움직이는 최소 횟수 구하기
- 10 넘으면 -1 출력

- 기울여서 움직이기 때문에, 한 칸씩 이동하는게 아니라 빈 칸 끝 막힌 부분까지 움직이는게 한번의 움직임이다.
- 굳이 벽을 1, 길을 0으로 차환해서 저장해둘 필요가 았을까ㅓ? : 없을듯 그냥 전체 그래프 길이 m인 n개의 문자열 갖는 리스트로 만들기
"""

class DFS:
    def __init__(self) -> None:
        self.di, self.dj = [-1, 1, 0, 0], [0, 0, -1, 1]
        self.n, self.m = map(int, input().split())
        self.board = [list(input()) for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == 'R': self.ri, self.rj = i, j
                if self.board[i][j] == 'B': self.bi, self.bj = i, j
        self.ans = 11
        

class DFSReferencedSolution(DFS):
    def __init__(self) -> None:
        super().__init__()

        self.visited = set() # 시간 효율 높이기 - 이미 n값에 파랑, 빨강 구슬 좌표 시도해본경우 가지치기
        self.dfs(1, self.ri, self.rj, self.bi, self.bj)
        if self.ans == 11: self.ans = -1
        print(self.ans)


    def print_board(self):
        for b in self.board: print(b)


    def move(self, i, j, dir):
        """dir 방향으로 들어온 좌표 끝까지 이동시키는 함수"""
        back = -1
        for cnt in range(1, 12):
            i+=self.di[dir]; j+=self.dj[dir]
            x = self.board[i][j]
            if x == '#': return cnt+back
            elif x == 'O': return cnt
            elif x == 'R' or x == 'B': back-=1


    def dfs(self, n, ri, rj, bi, bj):
        if (n, ri, rj, bi, bj) in self.visited: return
        self.visited.add((n, ri, rj, bi, bj))

        if n>10: return 
        # 4방향 이동 처리
        for dir in range(4):            
            # [1] dir 방량으로 각 구슬의 이동 거리 측정
            r_mvcnt = self.move(ri, rj, dir) 
            b_mvcnt = self.move(bi, bj, dir)
            # 둘 다 갇혀서 못움직이는 경우 => 진행 불가, 다음 후보군으로 continue
            if r_mvcnt == 0 and b_mvcnt==0: continue

            # [2] 계산한 거리 기반으로 각 구슬 다음 위치 좌표 계산
            nri, nrj = ri+self.di[dir]*r_mvcnt, rj+self.dj[dir]*r_mvcnt
            nbi, nbj = bi+self.di[dir]*b_mvcnt, bj+self.dj[dir]*b_mvcnt

            # [3] 해당 좌표가 구멍인 경우 처리
            # 파란 구슬이 구멍이면 실패
            if self.board[nbi][nbj] == 'O': continue
            else:
                # 빩강 구슬만 구멍이면 성공
                if self.board[nri][nrj] == 'O': 
                    self.ans = min(self.ans, n)
                    return
            # 
            self.board[ri][rj], self.board[bi][bj] = '.', '.'
            self.board[nri][nrj], self.board[nbi][nbj] = 'R', 'B'

            self.dfs(n+1, nri, nrj, nbi, nbj)

            self.board[nri][nrj], self.board[nbi][nbj] = '.', '.'
            self.board[ri][rj], self.board[bi][bj] = 'R', 'B'


DFSReferencedSolution()


class DFSMySolution(DFS):
    def dfs_first_trial(self, x, y, cnt, dir, bx, by):
        """ 
        - x, y : 햔재 삘간 공 좌표
        - cnt : 현재 시점 무빙 횟수
        - dir : 이전 움직였을 때의 방향
        4방향 이동할때 이전 방향과 동일하면 move count 하면 안되고 그냥 움직여야함
            - 파란 공, 빨간 공 서로 위치 고려
        """
        global ans
        visited = set()
        next_bx, next_by = bx+self.dx[dir], by+self.dy[dir]
        # if 0<=next_bx<n and 0<=next_by<m and (next_bx, next_by) != (x, y) and 

        if x<0 or y<0 or x>=n or y>=m or \
        (x==bx and y==by) or\
        cnt>10 or (x, y) in visited: return 

        if (x, y) == (self.end_x, self.end_y): 
            if cnt < ans: ans = cnt
            return
        
        visited.add((x, y))
        
        for i in range(4):
            """ TODO move blue marble as well """
            nx, ny = x+self.dx[i], y+self.dy[i]
            if i == dir: self.dfs(nx, ny, cnt, i)
            else: self.dfs(nx, ny, cnt+1, i)

        visited.discard((x, y))




class BFSSolution:
    def __init__(self) -> None:
        n, m = map(int, input().split())
        self.board = [(input()) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if self.board[i][j] == 'R' : rx, ry = i, j
                elif self.board[i][j] == 'B': bx, by = i, j
                elif self.board[i][j] == 'O': end_x, end_y = i, j
        self.board[rx][ry], self.board[bx][by] = '.', '.'

        ans =11
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        visited = set()
        self.bfs(rx, ry, bx, by, end_x, end_y)

    def bfs(self, rx, ry, bx, by, end_x, end_y):
        """
        bfs로 접근하면 매 move마다 불가능한 위치일 때마다 바로바로 탐색을 종료할 수 있는데,
        dfs로 접근하면 첫 포인트에서 될 수 있는데까지 끝까지 탐색하다가 불가한 해일경우 다른 위치를 탐색하기 때문에,
        최소 횟수를 구하는데에 적합하지 않고, BFS로 접근해본다.
        """
        from collections import deque

        red_visited = set()
        blue_visited = set()
        q = deque([(rx, ry, bx, by, 0)])
        while q:
            rx, ry, bx, by, cnt, dir = q.popleft()
            """ 둘 중 하나가 X면 리턴, 둘이 좌표값 똑같으면 무시 """
            if self.board[rx][ry] == 'X' or self.board[bx][by] == 'X' or (rx==bx and ry==by): continue

            """ 둘 중 하나 종료 조건 만나면 
            - red -> blue 기울인 방향으로 다 움직였을때 가능하면 -1, 불가하면 cnt 출력, 리턴 
            - blue 가 종료조건이면 -1"""
            if (rx, ry) == (end_x, end_y):
                flag = False
                while True:
                    bx, by = bx + self.dx[dir], by+self.dx[dir]
                    if self.board[bx][by] == 'X': break
                    if self.board[bx][by] == 'O' : flag = True; break
                if flag : return -1
                else: return cnt
            if (bx, by) == (end_x, end_y): return -1
            
            """ visited에 없고, .이면 탐색"""
            """ 4방향 탐색(한칸씩 이동)
                - 0 ) x좌표 smaller marble move first
                - 1 ) x좌표 bigger marble move first
                - 2 ) y좌표 smaller marble move first
                - 3 ) y좌표 bigger marble move first """
            for i in range(4):
                nrx, nry, nbx, nby = rx+self.dx[i], ry+self.dy[i], bx+self.dx[i], by+self.dy[i]
                # 가려는 위치가 벽이면 멈춰 일단
                if self.board[nrx][nry] == 'X': nrx, nry = rx, ry
                if self.board[nbx][nby] == 'X': nbx, nby = bx, by
                # 가려는 위치가 전에 아떤 구슬 있었던 자리먄
                if (nrx, nry) == (bx, by) or (nbx, nby) == (rx, ry):
                    # 그 전 구슬 이동했는지 검사
                    pass


        



# n, m, board = 5, 5, [['#####'], ['#..B#'], ['#.#.#'], ['#RO.#'], ['#####']] # 
# n, m, board = 7, 7, [['#######'], ['#...RB#'], ['#.#####'], ['#.....#'], ['#####.#'], ['#O....#'], ['#######']]
# n, m, board = 7, 7, [['#######'], ['#..R#B#'], ['#.#####'], ['#.....#'], ['#####.#'], ['#O....#'], ['#######']] 
# n, m, board = 10, 10, [['##########'], ['#R#...##B#'], ['#...#.##.#'], ['#####.##.#'], ['#......#.#'], ['#.######.#'], ['#.#....#.#'], ['#.#.#.#..#'], ['#...#.O#.#'], ['##########']]
# n, m, board = 3, 7, [['#######'], ['#R.O.B#'], ['#######']]
# n, m, board = 10, 10, [['##########'], ['#R#...##B#'], ['#...#.##.#'], ['#####.##.#'], ['#......#.#'], ['#.######.#'], ['#.#....#.#'], ['#.#.##...#'], ['#O..#....#'], ['##########']]
# n, m, board = 3, 10, [['##########'], ['#.O....RB#'], ['##########']]
