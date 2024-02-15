// 문제 풀이 링크: https://velog.io/@cuppizza/백준-7576-토마토-C-파이썬
// 실행 시간: 120ms 메모리: 9700KB
#include <queue>
#include <vector>
#include <stdio.h>

using namespace std;
int main(void)
{
	int M, N;
	scanf("%d", &M);
	scanf("%d", &N);

	vector<vector<int>> tomato(N);
	vector<int> temp;
	int element;
	queue<pair<int, int>> q, tempQ;
	for (int x = 0; x < N; ++x)
	{
		for (int y = 0; y < M; ++y)
		{
			scanf("%d", &element);
			temp.push_back(element);
			if (element == 1)
			{
				tempQ.push({ x, y });
			}
		}
		tomato[x] = temp;
		temp.clear();
	}

	int dx[] = { -1, 0, 0, 1 };
	int dy[] = { 0, -1, 1, 0 };
	pair<int, int> coord;
	int count = -1;
	while (!tempQ.empty())
	{
		while (!tempQ.empty())
		{
			q.push(tempQ.front());
			tempQ.pop();
		}
		if (q.size() > 0)
		{
			++count;
		}
		while (!q.empty())
		{
			coord = q.front();
			q.pop();
			for (int i = 0; i < 4; ++i)
			{
				if (coord.first + dx[i] < 0 || coord.first + dx[i] >= N
					|| coord.second + dy[i] < 0 || coord.second + dy[i] >= M)
				{
					continue;
				}
				if (tomato[coord.first + dx[i]][coord.second + dy[i]] != 0)
				{
					continue;
				}
				tempQ.push({ coord.first + dx[i] , coord.second + dy[i] });
				tomato[coord.first + dx[i]][coord.second + dy[i]] = 1;
			}
		}
	}
	for (int x = 0; x < N; ++x)
	{
		for (int y = 0; y < M; ++y)
		{
			if (tomato[x][y] == 0)
			{
				count = -1;
				break;
			}
		}
		if (count == -1)
		{
			break;
		}
	}
	printf("%d", count);
}


// 실행 시간: 124ms 메모리: 13192KB

#include <vector>
#include <stdio.h>

using namespace std;
int main(void)
{
    int m, n, temp;
    scanf("%d %d", &m, &n);
    vector<vector<int>> graph(n, vector<int>(m, 0));
    vector<pair<int, int>> next_pos;
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            scanf("%d", &temp);
            if (temp == -1)
            {
                graph[i][j] = -1;
            }
            else if (temp == 1)
            {
                graph[i][j] = 1;
                next_pos.push_back({i, j});
            }
        }
    }

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};
    int result = -1;

    while(next_pos.size() != 0)
    {
        vector<pair<int, int>> cur_pos = next_pos;
        next_pos.clear();
        while(cur_pos.size() != 0)
        {
            int x, y;
            x = cur_pos.back().first;
            y = cur_pos.back().second;
            cur_pos.pop_back();
            for (int d=0; d<4; ++d)
            {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if(nx < 0 || nx >= n || ny < 0 || ny >=m)
                {
                    continue;
                }
                if(graph[nx][ny] != 0)
                {
                    continue;
                }
                graph[nx][ny] = 1;
                next_pos.push_back({nx, ny});
            }
        }
        ++result;
    }
    for(int i = 0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            if(graph[i][j] == 0)
            {
                printf("-1");
                return 0;
            }
        }
    }
    printf("%d", result);
}