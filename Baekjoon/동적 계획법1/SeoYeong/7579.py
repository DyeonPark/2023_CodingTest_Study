"""
  0 1 2 3 4 5 6 7 8 9 10 
  #
"""

def solution():
    n, m = map(int, input().split())
    memory = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    # n * sum_of_cost
    dp = [[0 for _ in range(sum(cost)+1)] for _ in range(n+1)]

    answer = sum(cost)+1
    for i in range(1, n):
        for w in range(1, sum(cost)):
            # 현재 cost[i]가 w보다 작거나 같을 때 -> 업데이트 되는지 확인
            if cost[i] <= w: 
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost[i]]+memory[i])
            # 현재 cost[i]가 w보다 클 때 : 현재 cost가 현재 앱을 비활성화하기 위해 필요한 cost보다 적음
            else:
                dp[i][w] = dp[i-1][w]

            if dp[i][w] >= m:
                answer = min(answer, w)
    print(dp)
    return answer
# answer = solution()
# print(answer-1)


def solution_args(n, m, memory, cost):
    dp = [[0 for _ in range(sum(cost)+1)] for _ in range(n+1)]

    answer = sum(cost)+1
    for i in range(1, n+1):
        for w in range(sum(cost)+1):
            # 현재 cost[i]가 w보다 작거나 같을 때 -> 업데이트 되는지 확인
            if cost[i-1] <= w: 
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost[i-1]]+memory[i-1])
            # 현재 cost[i]가 w보다 클 때 : 현재 cost가 현재 앱을 비활성화하기 위해 필요한 cost보다 적음
            else:
                dp[i][w] = dp[i-1][w]

            if dp[i][w] >= m:
                answer = min(answer, w)
    for d in dp: print(d)
    print(answer)

solution_args(5, 60, [30, 10, 20, 35, 40], [3, 0, 3, 5, 4]) # 6
solution_args(5, 60, [20, 30, 10, 20, 30], [0, 0, 1, 2, 3]) # 1
# solution_args(100, 100, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
# 10000
solution_args(3, 10000000 ,[9999999, 1, 5], [3, 1, 0]) #3
solution_args(1, 10, [10], [5]) #5