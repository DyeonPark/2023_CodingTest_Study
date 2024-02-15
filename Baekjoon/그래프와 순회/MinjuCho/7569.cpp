// 문제 풀이 링크: https://velog.io/@cuppizza/백준-7569-토마토-C-파이썬
// 실행 시간: 176ms 메모리: 12140KB
#include <vector>
#include <stdio.h>
#include <queue>
#include <algorithm>

using namespace std;
int main(void)
{
    int m, n, h;
    scanf("%d %d %d", &m, &n, &h);
    vector<vector<vector<int>>> tomato(h);
    queue<vector<int>> q;
    for (int i=0; i<h; ++i)
    {
        vector<vector<int>> plane(n);
        for (int j=0; j<n; ++j)
        {
            vector<int> row(m);
            for (int k=0; k<m; ++k)
            {
                int temp;
                scanf("%d", &temp);
                row[k] = temp;
                if (temp == 1)
                {
                    q.push({i, j, k});
                }
            }
            plane[j] = row;
        }
        tomato[i] = plane;
    }

    int dx[6] = {-1, 1, 0, 0, 0, 0};
    int dy[6] = {0, 0, -1, 1, 0, 0};
    int dz[6] = {0, 0, 0, 0, -1, 1};
    int x, y, z, nx, ny, nz;
    vector<int> cur;
    while (!q.empty())
    {
        cur = q.front();
        q.pop();
        x = cur[1];
        y = cur[2];
        z = cur[0];
        for (int d=0; d<6; ++d)
        {
            nx = x+dx[d];
            ny = y+dy[d];
            nz = z+dz[d];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || nz < 0 || nz>= h)
            {
                continue;
            }
            if (tomato[nz][nx][ny] != 0)
            {
                continue;
            }
            tomato[nz][nx][ny] = tomato[z][x][y] + 1;
            q.push({nz, nx, ny});
        }
    }
    int result = -1;
    for (int i = 0; i < h; ++i)
    {
        for (int j=0; j<n; ++j)
        {
            for (int k=0; k<m; ++k)
            {
                if (tomato[i][j][k] == 0)
                {
                    printf("-1");
                    return 0;
                }
            }
            result = max(result, *max_element(tomato[i][j].begin(), tomato[i][j].end()));
        }
    }
    printf("%d", result-1);
}

// 실행 시간: 384ms, 메모리: 13096KB
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
int main(void)
{
	int M, N, H;
	cin >> M;
	cin >> N;
	cin >> H;
	queue<vector<int>> nextQ;
	vector<vector<vector<int>>> boxes;
	for (int h = 0; h < H; ++h)
	{
		vector<vector<int>> plane;
		for (int i = 0; i < N; ++i)
		{
			vector<int> row(M);
			for (int j = 0; j < M; ++j)
			{
				cin >> row[j];
				if (row[j] == 1)
				{
					nextQ.push({ h, i, j });
				}
			}
			plane.push_back(row);
		}
		boxes.push_back(plane);
	}

	int result = 0;
	if (nextQ.size() == M * N * H)
	{
		cout << 0;
		return 0;
	}

	int dh[6] = { 0, 0, 0, 0, -1, 1 };
	int dx[6] = { -1, 1, 0, 0, 0, 0 };
	int dy[6] = { 0, 0, -1, 1, 0, 0 };

	while (!nextQ.empty())
	{
		queue<vector<int>> tempQ;
		while (!nextQ.empty())
		{
			auto elem = nextQ.front();
			nextQ.pop();
			tempQ.push(elem);
		}
		while(!tempQ.empty())
		{
			int h, x, y;
			h = tempQ.front()[0];
			x = tempQ.front()[1];
			y = tempQ.front()[2];
			tempQ.pop();
			for (int k = 0; k < 6; ++k)
			{
				int nh = h + dh[k];
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nh < 0 || nh >= H || nx < 0 || nx >= N || ny < 0 || ny >= M)
				{
					continue;
				}
				if (boxes[nh][nx][ny] == -1 || boxes[nh][nx][ny] == 1)
				{
					continue;
				}
				boxes[nh][nx][ny] = 1;
				nextQ.push({ nh, nx, ny });
			}
		}
		if (!nextQ.empty())
		{
			++result;
		}
	}

	for (int h = 0; h < H; ++h)
	{
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < M; ++j)
			{
				if (boxes[h][i][j] == 0)
				{
					cout << -1;
					return 0;
				}
			}
		}
	}
	cout << result;
}