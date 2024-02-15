// 문제 풀이 링크: https://velog.io/@cuppizza/백준-1504-특정한-최단-경로-C-파이썬-다익스트라
// 실행 시간: 72ms 메모리: 4812KB
#include <stdio.h>
#include <vector>
#include <queue>
#define weight first
#define vertex second

const int INF = 0x3f3f3f3f;
using namespace std;

int n, e, a, b, c, v1, v2;
vector<pair<int, int>> adj[801];
vector<int> must_visit;
int dijkstra()
{
    int minimum = 0;
    for (int i = 0; i < must_visit.size() - 1; ++i)
	{
		int st = must_visit[i];
		int d[801];
		fill(d, d + n + 1, INF);
		d[st] = 0;
		priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
		pq.push({ 0, st });

		while (!pq.empty())
		{
			pair<int, int> cur = pq.top(); pq.pop();
			if (d[cur.vertex] != cur.weight)
			{
				continue;
			}
			for (pair<int, int> next : adj[cur.vertex])
			{
				if (d[next.vertex] <= d[cur.vertex] + next.weight)
				{
					continue;
				}
				d[next.vertex] = d[cur.vertex] + next.weight;
				pq.push({ d[next.vertex] , next.vertex });
			}
		}
		// protect overflow
		if (d[must_visit[i + 1]] == INF)
		{
			minimum = INF;
			return minimum;
		}
		else
		{
			minimum += d[must_visit[i + 1]];
		}
	}
    return minimum;
}

int main(void)
{
	scanf("%d %d", &n, &e);
	while (e--)
	{
		pair<int, int> temp;
		scanf("%d %d %d", &a, &b, &c);
		adj[a].push_back({ c, b });
		adj[b].push_back({ c, a });
	}
	scanf("%d %d", &v1, &v2);
	
    must_visit = { 1, v1, v2, n };
    int minimum = dijkstra();
	
	must_visit = { 1, v2, v1, n };
	int second_minimum = dijkstra();

	if (minimum == INF && second_minimum == INF)
	{
		printf("-1");
		return 0;
	}
	if (minimum <= second_minimum)
	{
		printf("%d", minimum);
	}
	else
	{
		printf("%d", second_minimum);
	}
}

// 실행 시간: 108ms 메모리: 4796KB
#include <stdio.h>
#include <vector>
#include <queue>
#define weight first
#define vertex second

const int INF = 0x3f3f3f3f;
using namespace std;
int main(void)
{
	int n, e, a, b, c, v1, v2;
	vector<pair<int, int>> adj[801];
	scanf("%d %d", &n, &e);
	while (e--)
	{
		pair<int, int> temp;
		scanf("%d %d %d", &a, &b, &c);
		adj[a].push_back({ c, b });
		adj[b].push_back({ c, a });
	}
	scanf("%d %d", &v1, &v2);
	
	vector<int> must_visit = { 1, v1, v2, n };
	int minimum = 0;
	
	for (int i = 0; i < must_visit.size() - 1; ++i)
	{
		int st = must_visit[i];
		int d[801];
		fill(d, d + n + 1, INF);
		d[st] = 0;
		priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
		pq.push({ 0, st });

		while (!pq.empty())
		{
			pair<int, int> cur = pq.top(); pq.pop();
			if (d[cur.vertex] != cur.weight)
			{
				continue;
			}
			for (pair<int, int> next : adj[cur.vertex])
			{
				if (d[next.vertex] <= d[cur.vertex] + next.weight)
				{
					continue;
				}
				d[next.vertex] = d[cur.vertex] + next.weight;
				pq.push({ d[next.vertex] , next.vertex });
			}
		}
		// protect overflow
		if (d[must_visit[i + 1]] == INF)
		{
			minimum = INF;
			break;
		}
		else
		{
			minimum += d[must_visit[i + 1]];
		}
	}
	
	must_visit = { 1, v2, v1, n };
	int second_minimum = 0;
	for (int i = 0; i < must_visit.size() - 1; ++i)
	{
		int st = must_visit[i];
		int d[801];
		fill(d, d + n + 1, INF);
		d[st] = 0;
		priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
		pq.push({ 0, st });

		while (!pq.empty())
		{
			pair<int, int> cur = pq.top(); pq.pop();
			if (d[cur.vertex] != cur.weight)
			{
				continue;
			}
			for (pair<int, int> next : adj[cur.vertex])
			{
				if (d[next.vertex] <= d[cur.vertex] + next.weight)
				{
					continue;
				}
				d[next.vertex] = d[cur.vertex] + next.weight;
				pq.push({ d[next.vertex] , next.vertex });
			}
		}
		// protect overflow
		if (d[must_visit[i + 1]] == INF)
		{
			second_minimum = INF;
			break;
		}
		else
		{
			second_minimum += d[must_visit[i + 1]];
		}
	}

	if (minimum == INF && second_minimum == INF)
	{
		printf("-1\n");
		return 0;
	}
	if (minimum <= second_minimum)
	{
		printf("%d\n", minimum);
	}
	else
	{
		printf("%d\n", second_minimum);
	}
}

/*
// 틀린 풀이
// 틀렸던 이유: 최소가 저장된 것이 v1인지 v2인지 모른 채로 무조건 v1 -> n 최단경로를 구했으므로

#include <stdio.h>
#include <vector>
#include <queue>
#define weight first
#define vertex second

const int INF = 0x3f3f3f3f;
using namespace std;
int main(void)
{
	int n, e, a, b, c, v1, v2;
	vector<pair<int, int>> adj[801];
	scanf("%d %d", &n, &e);
	while (e--)
	{
		pair<int, int> temp;
		scanf("%d %d %d", &a, &b, &c);
		adj[a].push_back({ c, b });
		adj[b].push_back({ c, a });
	}
	scanf("%d %d", &v1, &v2);
							// 0  1   2  3   4   5
	vector<int> must_visit = { 1, v1, 1, v2, v1, n };
	int minimum = 0;
	int shortest = v1;

	for (int i = 0; i < must_visit.size() - 1; ++i)
	{
		if (i == 1)
		{
			continue;
		}
		else if (i == 4)
		{
			must_visit[i] = shortest;
		}
		int st = must_visit[i];
		int d[801];
		fill(d, d + n + 1, INF);
		d[st] = 0;
		priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
		pq.push({ 0, st });

		while (!pq.empty())
		{
			pair<int, int> cur = pq.top(); pq.pop();
			if (d[cur.vertex] != cur.weight)
			{
				continue;
			}
			for (pair<int, int> next : adj[cur.vertex])
			{
				if (d[next.vertex] <= d[cur.vertex] + next.weight)
				{
					continue;
				}
				d[next.vertex] = d[cur.vertex] + next.weight;
				pq.push({ d[next.vertex] , next.vertex });
			}
		}
		if (i != 2)
		{
			if (i == 3 && (minimum == INF || d[must_visit[i + 1]] == INF))
			{
				printf("-1");
				return 0;
			}
			minimum += d[must_visit[i + 1]];
		}
		else if(minimum >= d[must_visit[i + 1]])
		{
			minimum = d[must_visit[i + 1]];
			shortest = v2; // must_visit[i + 1]
		}
	}
	printf("%d", minimum);
}
*/