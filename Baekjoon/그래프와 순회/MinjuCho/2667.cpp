// 문제 풀이 링크: https://velog.io/@cuppizza/백준-2667-단지번호붙이기-파이썬-C
// 실행 시간: 12ms 메모리: 2028KB
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
int main(void)
{
	int N;
	cin >> N;

	vector<vector<int>> graph(N, vector<int>(N, 0));
	vector<pair<int, int>> record;
	for (int i = 0; i < N; ++i)
	{
		string row;
		cin >> row;
		for (int j = 0; j < N; ++j)
		{
			if (row[j] == '1')
			{
				graph[i][j] = 1;
				record.push_back({ i, j });
			}
		}
	}

	int dx[] = { -1, 1, 0, 0 };
	int dy[] = { 0, 0, -1, 1 };
	vector<int> result;
	for (pair<int, int> coord : record)
	{
		// if visited, skip
		int cx = coord.first;
		int cy = coord.second;
		if (graph[cx][cy] == 0)
		{
			continue;
		}
		// BFS
		int cnt = 1;
		queue<pair<int, int>> q;
		q.push({ cx, cy });
		graph[cx][cy] = 0;
		while (!q.empty())
		{
			int x = q.front().first;
			int y = q.front().second;
			q.pop();
			for (int i = 0; i < 4; ++i)
			{
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || nx >= N || ny < 0 || ny >= N)
				{
					continue;
				}
				if (graph[nx][ny] == 0)
				{
					continue;
				}
				q.push({ nx, ny });
				graph[nx][ny] = 0;
				++cnt;
			}
		}
		result.push_back(cnt);
	}

	sort(result.begin(), result.end());
	cout << result.size() << endl;
	for (int num : result)
	{
		cout << num << endl;
	}
}