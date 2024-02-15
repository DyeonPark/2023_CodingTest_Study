// 문제 풀이 링크: https://velog.io/@cuppizza/백준-1753-최단경로-C-파이썬-다익스트라-우선순위-큐
// 실행 시간: 152ms 메모리: 13196KB
#include <vector>
#include <queue>
#include <stdio.h>

#define weight first
#define vertex second
using namespace std;

int V, E, st;
const int INF = 0x3f3f3f3f;
vector<pair<int, int>> adj[200001];
int d[200001];

int main(void)
{
	scanf("%d", &V);
	scanf("%d", &E);
	scanf("%d", &st);
	while (E--)
	{
		int u, v, w;
		scanf("%d", &u);
		scanf("%d", &v);
		scanf("%d", &w);
		adj[u].push_back({ w, v });
	}

	// 첫 노드 0, 나머지 INF
	fill(d, d + V + 1, INF);
	d[st] = 0;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, st });
	while (!pq.empty())
	{
		pair<int, int> cur = pq.top();
		pq.pop();
		// 이미 최단거리 존재 시 skip
		if (cur.weight != d[cur.vertex])
		{
			continue;
		}
		for (pair<int, int> next : adj[cur.vertex])
		{
			// 이미 최단거리 일 때
			if (d[next.vertex] <= d[cur.vertex] + next.weight)
			{
				continue;
			}
			d[next.vertex] = d[cur.vertex] + next.weight;
			pq.push({ d[next.vertex], next.vertex });
		}
	}

	for (int i = 1; i <= V; ++i)
	{
		if (d[i] == INF)
		{
			printf("INF\n");
			continue;
		}
		printf("%d\n", d[i]);
	}
}

// 실행 시간: 956ms 메모리: 14104KB
#include <vector>
#include <queue>
#include <iostream>

#define weight first
#define vertex second
using namespace std;

int V, E, st;
const int INF = 0x3f3f3f3f;
vector<pair<int, int>> adj[200001];
int d[200001];

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> V >> E >> st;
	while (E--)
	{
		int u, v, w;
		cin >> u >> v >> w;
		adj[u].push_back({ w, v });
	}

	// 첫 노드 0, 나머지 INF
	fill(d, d + V + 1, INF);
	d[st] = 0;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, st });
	while (!pq.empty())
	{
		pair<int, int> cur = pq.top();
		pq.pop();
		// 이미 최단거리 존재 시 skip
		if (cur.weight != d[cur.vertex])
		{
			continue;
		}
		for (pair<int, int> next : adj[cur.vertex])
		{
			// 이미 최단거리 일 때
			if (d[next.vertex] <= d[cur.vertex] + next.weight)
			{
				continue;
			}
			d[next.vertex] = d[cur.vertex] + next.weight;
			pq.push({ d[next.vertex], next.vertex });
		}
	}

	for (int i = 1; i <= V; ++i)
	{
		if (d[i] == INF)
		{
			cout << "INF" << endl;
			continue;
		}
		cout << d[i] << endl;
	}
}