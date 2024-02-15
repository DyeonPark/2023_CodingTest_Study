// 문제 풀이 링크: https://velog.io/@cuppizza/백준-2178-미로-탐색-C-파이썬-BFS-최단거리
// 실행 시간: 0ms 메모리: 2028KB
#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int main(void)
{
	int N, M;
	cin >> N;
	cin >> M;

	vector<vector<int>> maze;
	vector<int> temp;
	string element;
	for (int i = 0; i < N; ++i)
	{
		cin >> element;
		for (int j = 0; j < M; ++j)
		{
			temp.push_back((int)element[j] - '0');
		}
		maze.push_back(temp);
		temp.clear();
	}

	int dx[] = { -1, 0, 0, 1 };
	int dy[] = { 0, -1, 1, 0 };
	int nx = 0, ny = 0;
	pair<int, int> coord = { 0, 0 };
	queue<pair<int, int>> q;
	int distance = 1;
	q.push(coord);
	while (!q.empty())
	{
		coord = q.front();
		q.pop();
		distance = maze[coord.first][coord.second];
		for (int i = 0; i < 4; ++i)
		{
			nx = coord.first + dx[i];
			ny = coord.second + dy[i];
			if (nx < 0 || nx >= N || ny < 0 || ny >= M)
			{
				continue;
			}
			if (maze[nx][ny] != 1 || (nx==0 && ny==0))
			{
				continue;
			}
			maze[nx][ny] += distance;
			q.push({ nx, ny });
		}
	}
	cout << maze[N - 1][M - 1];
}