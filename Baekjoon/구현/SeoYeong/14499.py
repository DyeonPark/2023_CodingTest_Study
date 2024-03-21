"""
n * m map, 주사위 처음 놓여진 좌표 x, y, 명령 개수 k
for n: 지도에 쓰여있는 수 (x, y) 값은 항상 0
이동하는 명령(1234 동-서-북-남)
-> 이동할때마다 주사위 윗 면에 쓰여있는 수 출력(바깥으로 이동시키려고 하는 경우 무시)
"""
from collections import deque

class Reference_Solution:
    def roll_the_dice(self):
        def turn(direction):
            a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
            if direction == 1 : change = [d, b, a, f, e, c]
            elif direction == 2 : change = [c, b, f, a, e, d]
            elif direction == 3 : change = [e, a, c, d, f, b]
            else: change = [b, f, c, d, a, e]
            for i in range(6): dice[i] = change[i]

        n, m, x, y, _ = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        orders = list(map(int, input().split()))
        dice = [0 for _ in range(6)]
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        nx, ny = x, y
        for order in orders:
            nx, ny = nx+dx[order-1], ny+dy[order-1]
            # print(f"order:{order} nx:{nx} ny:{ny}")

            if nx<0 or ny<0 or nx>=n or ny>=m: 
                # print("out of range")
                nx, ny = nx-dx[order-1], ny-dy[order-1]
                continue

            turn(order)
            if board[nx][ny] ==0: board[nx][ny] = dice[-1]
            else:
                dice[-1] = board[nx][ny]
                board[nx][ny] = 0
            print(dice[0])

"""
2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2
동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

"""


Reference_Solution().roll_the_dice()


class MySolution:
    def roll_the_dice():
        n, m, x, y, k = map(int, input().split())
        graph = [list(map(int, input().split)) for _ in range(n)]
        move_dic = {1:[1, 0], 2:[-1, 0], 3:[0, 1], 4:[0, -1]}
        # orders = [move_dic[x] for x in list(map(int, input().split))]
        orders = list(map(int, input().split))

        dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        updown = deque([1, 5, 6, 2])
        side = deque([1, 3, 4])
        cur_dice_down_side = 1

        for order in orders:
            nx, ny = x+move_dic[order][0], y+move_dic[order][1]
            if nx<0 or ny<0 or nx>=n or ny>=m: pass

            if order in [1, 2]:
                if order == 1: side.rotate(1)
                else: side.rotate(-1)

            if order in [3, 4]:
                if order == 3: updown.rotate(-1)
                else: updown.rotate(1)
                dice[updown[0]] = graph[nx][ny]

            graph[nx][ny] = 0

