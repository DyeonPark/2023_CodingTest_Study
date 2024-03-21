"""
ti = [3, 5, 1, 1, 2, 4, 2] : 각 상담에 소요되는 기간 수
pi = [10, 20, 10, 20, 15, 40, 200] : 각 상담 단가

어차피 DFS, Brute Force로 다 해야됨

"""
class Solution:
    def __init__(self, n, session) -> None:
        self.n = n
        self.session = session
        self.result = 0

    def dp(self):
        """
        44ms
        dp[i] = i번째 날부터 퇴사일까지의 최대 이익
        - iterate in reverse (n-1 ~ 0)
            - if i+session[i][0] > n+1 : which means end date of the new session exceed the date of the quit
                - dp[i] = dp[i+1]
            - else
                - dp[i] = max(dp[i+1], dp[i+session[i][0]] + session[i][1])
        """
        dp = [0 for _ in range(self.n+1)]
        for i in range(self.n-1, -1, -1):
            if i + self.session[i][0] > self.n:
                dp[i] = dp[i+1]
            else:
                dp[i] = max(dp[i+1], dp[i+session[i][0]]+session[i][1])
        return max(dp)


    def brute_force(self):
        """
        56ms
        def backtrack(day : current day, profit : current profit)
            - recursive function
            - base case
                - if day == n+1: 
                    result = max(result, profit)
                    return
            - start two options, whether choose today's session or not
            - choose
                - if day + session[day][0] <= n+1:
                    - backtrack(day+session[day][0], profit+session[day][1])
            - not choose
                - backtrack(day+1, profit)
        
        result = 0
        backtrack(0, 0)
        """
        def backtrack(day, profit):
            if day == self.n: 
                self.result = max(profit, self.result)
                return
            
            # choose the current session
            if day + self.session[day][0] <= self.n:
                backtrack(day+self.session[day][0], profit+self.session[day][1])
            # not cboose the current session
            backtrack(day+1, profit)

        backtrack(0, 0)
        return self.result


class MySolution:
    def dfs(self, i, end_date, profit):
        """ recursion
        base case : 
            - if t[i] is already booked so that the council cannot be started
            - i is at the end of the quit day
            - if t[i] will exceed the day of quiting
        
        start the session or not, take the max of each case and save it to dp[i]
        """
        ti, pi = session[i][0], session[i][1]
        if i <= end_date or i >= len(session) or i+ti >= len(session): return profit # 현재 날짜 기준 아직 end_date 안됨
        # start the session or not -> return max value
        return max(self.dfs(i+1, i+ti, profit+pi), self.dfs(i+1, i, profit))


    def dfs_explaiend(self, i, end_date, profit):
        """
        i : 현재 날짜
        end_date : 예약된 상담 언제 끝나는지
        profit : 현재 기준 profit
        """
        print(f"{'  '*i}{end_date}, {profit}")
        ti, pi = session[i][0], session[i][1]

        if i >= len(session):
            print("already quir")
            return profit
        elif i+ti >= len(session):
            print("can't quit if i start the session")
            return profit
        
        if i < end_date: # previous session is not finished - only case that don't contain this session
            self.dfs_explaiend(i+1, i, profit)
        else:
            max(self.dfs_explaienddfs(i+1, i+ti, profit+pi), self.dfs_explaiend(i+1, i, profit))

        # return max(case1, case2)


n = int(input())
session = [list(map(int, input().split())) for _ in range(n)]

s = Solution(n, session)
dp_result = s.dp()
bf_result = s.brute_force()
print(dp_result, bf_result)