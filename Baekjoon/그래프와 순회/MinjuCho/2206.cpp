// 문제 풀이 링크: https://velog.io/@cuppizza/백준-2206-벽-부수고-이동하기-파이썬-C-BFS-최단거리
// 실행 시간: 180ms 메모리: 21624KB
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
int main(void)
{
	int n, m;
	cin >> n >> m;
	
	vector<vector<int>> graph(n);
	for (int i = 0; i < n; ++i)
	{
		string row_str;
		cin >> row_str;
		vector<int> row(m);
		for (int j = 0; j < m; ++j)
		{
			row[j] = row_str[j] - '0';
		}
		graph[i] = row;
	}
	vector<vector<vector<int>>> visited(2);
	visited[0] = graph;
	visited[1] = graph;

	int dx[4] = { 0, 0, -1, 1 };
	int dy[4] = { -1, 1, 0, 0 };
	queue<vector<int>> q;
	q.push({ 0, 0, 0 });
	visited[0][0][0] = 1;
	while (!q.empty())
	{
		int z = q.front()[0];
		int curX = q.front()[1];
		int curY = q.front()[2];
		q.pop();
		if (curX == n - 1 && curY == m - 1)
		{
			cout << visited[z][curX][curY];
			return 0;
		}
		for (int d = 0; d < 4; ++d)
		{
			int nx = curX + dx[d];
			int ny = curY + dy[d];
			if (nx < 0 || nx >= n || ny < 0 || ny >= m)
			{
				continue;
			}
			if (visited[z][nx][ny] == 0 && visited[z][nx][ny] == 0)
			{
				visited[z][nx][ny] = visited[z][curX][curY] + 1;
				q.push({ z, nx, ny });
			}
			else if (!z && visited[0][nx][ny] == 1)
			{
				visited[1][nx][ny] = visited[0][curX][curY] + 1;
				q.push({ 1, nx, ny });
			} 
		}
	}
	cout << -1;
}