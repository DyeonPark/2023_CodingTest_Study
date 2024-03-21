from collections import deque

"""
Solve with plain list
- make conveyor belt in list 
- and keep track of start, end point by put_idx, down_idx
"""
class Solution:
    def __init__(self, n, k, a) -> None:
        self.n = n*2
        self.k = k
        self.a = a # 각 칸 내구도
        self.robot_idx_q = deque([])
        self.put_idx = 0
        self.down_idx = n-1

    def rotate_belt(self) -> None:
        """ 벨트가 각 칸 취에 있는 로봇과 한 칸 회전 """
        print(f"1. rotate belt with robot.")

        # self.put_idx = (self.put_idx+1)%self.n
        if self.put_idx == 0: self.put_idx = self.n-1
        else: self.put_idx -= 1
        if self.down_idx == 0: self.down_idx = self.n-1
        else: self.down_idx -= 1

        if self.robot_idx_q:
            # q version
            end_condition = self.robot_idx_q[-1]
            while self.robot_idx_q:
                i = self.robot_idx_q.popleft()
                if i != self.down_idx: self.robot_idx_q.append(i)
                if i == end_condition: break

        print(f" -> {self.put_idx, self.down_idx} rb:{self.robot_idx_q}")
            
    def move_robot(self) -> None:
        """ 가장 먼저 올라간 로봇부터 앞으로 한 칸 이동
        - 이동할 수 있는 조건 : 이동하려는 칸에 로봇이 없고 내구도가 1 이상임 """
        print(f"2. start to move robot")

        if not self.robot_idx_q: return
        
        last_idx = self.robot_idx_q[-1]
        while self.robot_idx_q :
            current_robot = self.robot_idx_q.popleft()
            move_one_idx = (current_robot+1) % self.n
            if move_one_idx not in self.robot_idx_q and self.a[move_one_idx] >= 1:
                self.a[move_one_idx]-=1
                if move_one_idx != self.down_idx : 
                    self.robot_idx_q.append(move_one_idx)
            else:
                self.robot_idx_q.append(current_robot)

            if current_robot == last_idx: break

        print(f"  -> {self.robot_idx_q}")

    def put_robot(self) -> None:
        """ 올리는 위치에 로봇 올리기 (if 내구도[올리는위치) !=0) """
        print(f"3. put robot at {self.put_idx} on the {self.a}")
        if self.a[self.put_idx] != 0:
            self.robot_idx_q.append(self.put_idx)
            self.a[self.put_idx] -= 1

    def check_the_durability(self) -> bool:
        num_of_zero = 0
        for d in self.a: 
            if d == 0: num_of_zero+=1
        print(f"\t-> durability status: {self.a}")
        return num_of_zero >= self.k
    
    def execute(self):
        idx = 1
        while True:
            print(f"\n#{idx}")
            self.rotate_belt()
            self.move_robot()
            self.put_robot()
            if self.check_the_durability(): return idx
            idx+=1
            print(f"robot:{self.robot_idx_q}")
        

class ReferencedSolution:
    """
    Missing Point
    - belt, robot 둘 다 큐로 구현한다.
    - deque모듈에 rotate 메소드가 있어서 포인터롤 tracking하지 않고 리스트 자체를 회전시켜버릴 수 있다.

    """
    def robot_on_the_belt(self, n, k, a):
        # 벨트, 로봇 deuqe rotate  
        zero_cnt, ans = -1, 0
        belt = deque(a)
        robot = deque([False for _ in range(len(a))])
        while True:
            belt.rotate(1)
            robot.rotate(1)
            robot[n-1] = False
            for i in range(n-2, -1, -1): # 먼저 올라간 로봇부터 움직여야 함 -> 거꾸로 돌아야함
                if robot[i] and not robot[i+1] and belt[i+1]>=1:
                    robot[i] = False
                    robot[i+1] = True
                    belt[i+1] -= 1
            robot[n-1] = False
            if belt[0] != 0:
                robot[0] = True
                belt[0] -= 1
            ans += 1
            if belt.count(0) >= k: break
        return ans


n, k = map(int, input().split()) # 칸 개수, 종려 조건(내구도 0인칸 개수
a =list(map(int, input().split()) )
# n, k, a = 3, 2, [1, 2, 1, 2, 1, 2]
# n, k, a = 3, 6, [10, 10, 10, 10, 10, 10]
# n, k, a = 4, 5, [10, 1, 10, 6, 3, 4, 8, 2]
# n, k, a = 5, 8, [100, 99, 60, 80, 30, 20, 10, 89, 99, 100] 
# answer = Solution(n, k, a).execute()
answer = ReferencedSolution().robot_on_the_belt(n, k, a)
print(answer)


