// 문제 풀이 링크: https://velog.io/@cuppizza/백준-1012-유기농-배추-C-파이썬
// 실행 시간: 4ms 메모리: 2024KB
#include<iostream>
#include<vector>
#include<queue>
#define X first
#define Y second

using namespace std;
int main(void)
{
	int T;
	cin >> T;
	while (T--)
	{
		int M, N, K, x, y;
		cin >> M; cin >> N; cin >> K;
		vector<vector<int>> farm(N, vector<int>(M, 0));
		while (K--)
		{
			cin >> y; cin >> x;
			farm[x][y] = 1;
		}
		int count = 0;
		queue<pair<int, int>> q;
		pair<int, int> cur;
		pair<int, int> offset[] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < M; ++j)
			{
				if (farm[i][j] == 1)
				{
					farm[i][j] = 2;
					q.push({ i, j });
					while (!q.empty())
					{
						cur = q.front();
						q.pop();
						for (int of = 0; of < 4; ++of)
						{
							// out of range
							if (cur.X + offset[of].X < 0 || cur.X + offset[of].X >= N
								|| cur.Y + offset[of].Y < 0 || cur.Y + offset[of].Y >= M)
							{
								continue;
							}
							if (farm[cur.X + offset[of].X][cur.Y + offset[of].Y] == 1)
							{
								farm[cur.X + offset[of].X][cur.Y + offset[of].Y] = 2;
								q.push({ cur.X + offset[of].X, cur.Y + offset[of].Y });
							}
						}
					}
					++count;
				}
			}
		}
		cout << count << endl;
	}
}