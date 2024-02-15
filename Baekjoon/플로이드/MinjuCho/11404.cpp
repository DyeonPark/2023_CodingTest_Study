// 문제 풀이 링크: https://velog.io/@cuppizza/백준-11404-플로이드-C-파이썬-플로이드
// 실행 시간: 32ms 메모리: 1228KB
#include <vector>
#include <stdio.h>

const int INF = 0x3f3f3f3f;
using namespace std;
int main(void)
{
	int n, m;
	scanf("%d %d", &n, &m);
	vector<vector<int>> adj(n + 1, vector<int>(n + 1, INF));
	while (m--)
	{
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		if (c < adj[a][b])
		{
			adj[a][b] = c;
		}
	}
	for (int i = 1; i <= n; ++i)
	{
		adj[i][i] = 0;
	}
	for (int i = 1; i <= n; ++i)
	{
		for (int s = 1; s <= n; ++s)
		{
			for (int t = 1; t <= n; ++t)
			{
				if (adj[s][i] + adj[i][t] < adj[s][t])
				{
					adj[s][t] = adj[s][i] + adj[i][t];
				}
			}
		}
	}
	for (int x = 1; x <= n; ++x)
	{
		for (int y = 1; y <= n; ++y)
		{
			if (adj[x][y] == INF)
			{
				printf("0 ");
				continue;
			}
			printf("%d ", adj[x][y]);
		}
		printf("\n");
	}
}