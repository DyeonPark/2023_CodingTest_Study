// 문제 풀이 링크: https://velog.io/@cuppizza/백준-2606-바이러스-파이썬-C
// 실행 시간: 0ms 메모리: 2024KB
#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int main(void)
{
	int n, edge;
	cin >> n;
	cin >> edge;
	
	vector<vector<int>> graph(n+1);
	while(edge--)
	{
		int v1, v2;
		cin >> v1 >> v2;
		graph[v1].push_back(v2);
		graph[v2].push_back(v1);
	}

	int result = 0;
	vector<int> contaminated(n + 1, 0);
	queue<int> q;
	contaminated[1] = 1;
	q.push(1);
	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		for (int v : graph[cur])
		{
			if (contaminated[v] == 1)
			{
				continue;
			}
			contaminated[v] = 1;
			++result;
			q.push(v);
		}
	}
	cout << result;
}