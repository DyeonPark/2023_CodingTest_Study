// 문제 풀이 링크: https://velog.io/@cuppizza/백준-1956-운동-C-파이썬-플로이드
// 실행 시간: 132ms 메모리: 1756KB
#include<stdio.h>
#include<vector>

using namespace std;
const int INF = 0x3f3f3f3f;
int main(void)
{
	int v, e;
	scanf("%d %d", &v, &e);
	vector<vector<int>> adj(v + 1, vector<int>(v + 1, INF));
	while (e--)
	{
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);
		if (c < adj[a][b])
		{
			adj[a][b] = c;
		}
	}
	for (int i = 1; i <= v; ++i)
	{
		for (int s = 1; s <= v; ++s)
		{
			for (int t = 1; t <= v; ++t)
			{
				if (adj[s][i] + adj[i][t] < adj[s][t])
				{
					adj[s][t] = adj[s][i] + adj[i][t];
				}
			}
		}
	}
	int shortcycle = INF;
	for (int s = 1; s <= v; ++s)
	{
		for (int t = 1; t <= v; ++t)
		{
			if (adj[s][t] != INF && adj[t][s] != INF && adj[s][t] + adj[t][s] < shortcycle)
			{
				shortcycle = adj[s][t] + adj[t][s];
			}
		}
	}
	if (shortcycle == INF)
	{
		printf("-1");
	}
	else
	{
		printf("%d", shortcycle);
	}
}