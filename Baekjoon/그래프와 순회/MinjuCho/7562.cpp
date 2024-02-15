// 문제 풀이 링크: https://velog.io/@cuppizza/백준-7562-나이트의-이동-파이썬-C
// 실행 시간: 24ms 메모리: 1496KB
#include <vector>
#include <queue>
#include <stdio.h>

int dx[] = { -1, -2, -2, -1, 1, 2, 1, 2 };
int dy[] = { -2, -1, 1, 2, -2, -1, 2, 1 };
void bfs();
using namespace std;
int main(void)
{
	int testCase;
	scanf_s("%d", &testCase);
	while (testCase--)
	{
		bfs();
	}
}

void bfs()
{
	int n;
	scanf_s("%d", &n);
	int sx, sy, tx, ty;
	scanf_s("%d %d", &sx, &sy);
	scanf_s("%d %d", &tx, &ty);

	if (sx == tx && sx == ty)
	{
		printf("0\n");
		return;
	}

	vector<vector<int>> graph(n, vector<int>(n, 0));
	queue<pair<int, int>> q;
	graph[sx][sy] = 1;
	q.push({ sx, sy });
	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();

		for (int d = 0; d < 8; ++d)
		{
			int nx = cur.first + dx[d];
			int ny = cur.second + dy[d];
			if (nx < 0 || nx >= n || ny < 0 || ny >= n)
			{
				continue;
			}
			if (nx == tx && ny == ty)
			{
				printf("%d\n", graph[cur.first][cur.second]);
				return;
			}
			if (graph[nx][ny] != 0)
			{
				continue;
			}
			graph[nx][ny] = graph[cur.first][cur.second] + 1;
			q.push({ nx, ny });
		}
	}
}