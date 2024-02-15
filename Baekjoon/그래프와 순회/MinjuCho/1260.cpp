// 문제 풀이 링크 : https://velog.io/@cuppizza/백준-1260-DFS와-BFS-파이썬-C
// 실행 시간: 8ms 메모리: 2288KB
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;
int main(void)
{
	int n, m, v;
	cin >> n >> m >> v;

	vector<vector<int>> graph(n + 1);
	while (m--)
	{
		int v1, v2;
		cin >> v1 >> v2;

		graph[v1].push_back(v2);
		graph[v2].push_back(v1);
	}
	// sort
	for (int i = 0; i < graph.size(); ++i)
	{
		sort(graph[i].begin(), graph[i].end());
	}
	vector<int> visited(n + 1, 0);
	stack<int> stk;
	// DFS
	stk.push(v);
	while (!stk.empty())
	{
		int cur = stk.top();
		stk.pop();
		if (visited[cur] == 0)
		{
			cout << cur << " ";
			visited[cur] = 1;
		}
		for (int i= graph[cur].size() - 1; i>=0; --i)
		{
			if (visited[graph[cur][i]] == 1)
			{
				continue;
			}
			stk.push(graph[cur][i]);
		}
	}
	cout << endl;
	fill(visited.begin(), visited.end(), 0);
	queue<int> q;
	// BFS
	q.push(v);
	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		if (visited[cur] == 0)
		{
			cout << cur << " ";
			visited[cur] = 1;
		}
		for (int vertex:graph[cur])
		{
			if (visited[vertex] == 1)
			{
				continue;
			}
			q.push(vertex);
		}
	}
}