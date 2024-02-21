#include<stdio.h>
#include <algorithm>
const int INF = 0x6f6f6f6f;
int dp[501][501];
int main(void)
{
	int N;
	scanf("%d", &N);
	int matrix[501][2];
	for (int i = 1; i <= N; ++i)
	{
		scanf("%d %d", &matrix[i][0], &matrix[i][1]);
	}
	for (int i = 1; i <= N-1; ++i)
	{
		for (int j = 1; i + j <= N; ++j)
		{
			dp[j][i+j] = INF;
			for (int k = j; k <= i + j; ++k)
			{
				dp[j][i + j] = std::min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j]
													+ matrix[j][0] * matrix[k][1] * matrix[i + j][1]);
			}
		}
	}
	printf("%d", dp[1][N]);
}