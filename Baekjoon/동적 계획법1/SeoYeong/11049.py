"""
항상 순서대로 곱셈할 수 있는 크기만 주어짐
0 5 3
1 3 2
2 2 6
dp[i] : i-1, i를 하는데 필요한 연산

"""

n = int(input())
m_sizes = []
for i in range(n):
    r, c = map(int, input().split())
    if i == 0: 
        m_sizes.append(r)
        m_sizes.append(c)
        continue
    m_sizes.append(c)

# n, m_sizes = 3, [5, 3, 2, 6]
# n, m_sizes = 4, [5, 4, 6, 2, 7]

inf = 2**32
dp = [[inf for _ in range(n)] for _ in range(n)]# n*n dp 배열 생성, 대각선 기준 위쪽만 체움

for i in range(n): dp[i][i] = 0

for gap in range(1, n):
    print(f"\nnow gap is {gap}")
    for i in range(n-gap):
        j = i+gap
        print(f"calculate {i} to {j}")
        for k in range(i, j):
            p = dp[i][k] + dp[k+1][j] + m_sizes[i-1] * m_sizes[k] * m_sizes[j]
            print(f"{i}-{k} {k+1}-{j} {dp[i][j]}, {p}")
            if dp[i][j] > p: dp[i][j] = p
print(dp[0][-1])