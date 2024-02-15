// 문제 풀이 링크: https://velog.io/@cuppizza/백준-9370-미확인-도착지-C-파이썬-다익스트라-최단경로
// 실행 시간: 48ms 메모리: 2476KB
#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
#define weight first
#define vertex second
const int INF = 0x3f3f3f3f;
using namespace std;
vector<vector<pair<int, int>>> adj;
void dijkstra(vector<int>& d, int st)
{
	d[st] = 0;
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, st });
	while (!pq.empty())
	{
		pair<int, int> cur = pq.top(); pq.pop();
		if (cur.weight != d[cur.vertex])
		{
			continue;
		}
		for (pair<int, int> next : adj[cur.vertex])
		{
			if (d[cur.vertex] + next.weight < d[next.vertex])
			{
				d[next.vertex] = d[cur.vertex] + next.weight;
				pq.push({ d[next.vertex], next.vertex });
			}
		}
	}
}

int main(void)
{
	int T;
	scanf("%d", &T);
	while (T--)
	{
		int n, m, t, s, g, h;
		scanf("%d %d %d", &n, &m, &t);
		scanf("%d %d %d", &s, &g, &h);

		adj.clear();
		adj.resize(n + 1);
		while (m--)
		{
			int a, b, c;
			scanf("%d %d %d", &a, &b, &c);
			adj[a].push_back({ c, b });
			adj[b].push_back({ c, a });
		}
		vector<int> terminator, real_terminator;
		while (t--)
		{
			int node;
			scanf("%d", &node);
			terminator.push_back(node);
		}
        vector<int> S(n + 1, INF), G(n + 1, INF), H(n + 1, INF);
        dijkstra(S, s);
        dijkstra(G, g);
        dijkstra(H, h);
		for (int node : terminator)
		{
			bool have_direct_path = false;
			if (S[node] == S[g] + G[h] + H[node] || S[node] == S[h] + H[g] + G[node])
			{
				have_direct_path = true;
			}
			if (have_direct_path)
			{
				real_terminator.push_back(node);
			}
		}
		sort(real_terminator.begin(), real_terminator.end());
		for (int n : real_terminator)
		{
			printf("%d ", n);
		}
		printf("\n");
	}
}

//#include <stdio.h>
//#include <queue>
//#include <vector>
//#include <algorithm>
//#define weight first
//#define vertex second
//const int INF = 0x3f3f3f3f;
//using namespace std;
//int main(void)
//{
//	int T;
//	scanf("%d", &T);
//	while (T--)
//	{
//		int n, m, t, s, g, h;
//		scanf("%d %d %d", &n, &m, &t);
//		scanf("%d %d %d", &s, &g, &h);
//		
//		vector<pair<int, int>> adj[2001];
//		while (m--)
//		{
//			int a, b, c;
//			scanf("%d %d %d", &a, &b, &c);
//			adj[a].push_back({ c, b });
//			adj[b].push_back({ c, a });
//		}
//		vector<int> terminator, real_terminator;
//		while (t--)
//		{
//			int node;
//			scanf("%d", &node);
//			terminator.push_back(node);
//		}
//		for (int node : terminator)
//		{
//			int pre1[2001];
//			vector<int> route = { s, g, h, node }, real_route;
//			bool can_go1 = true;
//			for (int i = 0; i < 3; ++i)
//			{
//				int d[2001];
//				fill(d, d + 2001, INF);
//				d[route[i]] = 0;
//				priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
//				pq.push({ 0, route[i] });
//				while (!pq.empty())
//				{
//					pair<int, int> cur = pq.top(); pq.pop();
//					if (cur.weight != d[cur.vertex])
//					{
//						continue;
//					}
//					for (pair<int, int> next : adj[cur.vertex])
//					{
//						if (d[cur.vertex] + next.weight < d[next.vertex])
//						{
//							d[next.vertex] = d[cur.vertex] + next.weight;
//							pq.push({ d[next.vertex], next.vertex });
//							pre1[next.vertex] = cur.vertex;
//						}
//					}
//				}
//				if (d[route[i + 1]] == INF)
//				{
//					can_go1 = false;
//				}
//			}
//			if (can_go1)
//			{
//				int curNode = node;
//				while (curNode != s)
//				{
//					real_route.push_back(curNode);
//					curNode = pre1[curNode];
//					printf("curNode: %d\n", curNode);
//				}
//				real_route.push_back(curNode);
//				if (route.size() != real_route.size())
//				{
//					can_go1 = false;
//				}
//			}
//
//			int pre2[2001];
//			real_route.clear();
//			route = { s, h, g, node };
//			bool can_go2 = 0;
//
//			for (int i = 0; i < 3; ++i)
//			{
//				int d[2001];
//				fill(d, d + 2001, INF);
//				d[route[i]] = 0;
//				priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
//				pq.push({ 0, route[i] });
//				while (!pq.empty())
//				{
//					pair<int, int> cur = pq.top(); pq.pop();
//					if (cur.weight != d[cur.vertex])
//					{
//						continue;
//					}
//					for (pair<int, int> next : adj[cur.vertex])
//					{
//						if (d[cur.vertex] + next.weight < d[next.vertex])
//						{
//							d[next.vertex] = d[cur.vertex] + next.weight;
//							pq.push({ d[next.vertex], next.vertex });
//							pre2[next.vertex] = cur.vertex;
//						}
//					}
//				}
//				if (d[route[i + 1]] == INF)
//				{
//					can_go2 = false;
//				}
//			}
//			if (can_go2)
//			{
//				int curNode = node;
//				while (curNode != s)
//				{
//					real_route.push_back(curNode);
//					curNode = pre2[curNode];
//				}
//				real_route.push_back(curNode);
//				if (route.size() != real_route.size())
//				{
//					can_go2 = false;
//				}
//			}
//
//			if (can_go1 || can_go2)
//			{
//				real_terminator.push_back(node);
//			}
//			else
//			{
//				continue;
//			}
//		}
//		sort(real_terminator.begin(), real_terminator.end());
//		for (int n : real_terminator)
//		{
//			printf("%d ", n);
//		}
//		printf("\n");
//	}
//}