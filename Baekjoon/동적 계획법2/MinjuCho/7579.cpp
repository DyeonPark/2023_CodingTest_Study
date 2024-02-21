#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main(void)
{
	int N, M, sum = 0;
	scanf("%d %d", &N, &M);

	vector<int> m(N+1), c(N+1);
	for (int i = 1; i <= N; ++i)
	{
		scanf("%d", &m[i]);
	}
	for (int i = 1; i <= N; ++i)
	{
		scanf("%d", &c[i]);
		sum += c[i];
	}

	vector<vector<int>> dp(N + 1, vector<int>(sum + 1, 0));
	for (int i = 1; i <= N; ++i)
	{
		for (int j = 0; j <= sum; ++j)
		{
			if (j - c[i] >= 0)
			{
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c[i]] + m[i]);
			}
			dp[i][j] = max(dp[i - 1][j], dp[i][j]);
		}
	}
	for (int j = 0; j <= sum; ++j)
	{
		if (dp[N][j] >= M)
		{
			printf("%d", j);
			break;
		}
	}
}