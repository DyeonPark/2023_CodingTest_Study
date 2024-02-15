// 문제 풀이 링크: https://velog.io/@cuppizza/백준-13549-숨바꼭질-3-C-파이썬-BFS-최단거리
// C++ 두번째 풀이
// 실행시간: 0ms 메모리: 1620KB
#include <stdio.h>
#include <queue>
#include <stdlib.h>

using namespace std;

int N, K;s
int visited[100002];
queue<int> q;

void teleport(int cur, int sec)
{
    while (cur <= 100000 && visited[cur] == -1)
    {
        visited[cur] = sec;
        q.push(cur);
        if (cur == K)
        {
            printf("%d", visited[cur]);
            exit(0);
        }
        cur *= 2;
    }
}

int main(void)
{
    scanf("%d %d", &N, &K);
    fill(visited, visited + 100001, -1);
    int d[2] = { -1, 1 };

    teleport(N, 0);
    while (!q.empty())
    {
        int cur = q.front(); q.pop();
        for (int offset : d)
        {
            if (cur + offset < 0 || cur + offset >= 100002)
            {
                continue;
            }
            if (visited[cur + offset] != -1)
            {
                continue;
            }
            teleport(cur + offset, visited[cur] + 1);
        }
    }
    printf("%d", visited[K]);
}

// C++ 첫번째 풀이
// 실행시간: 0ms 메모리: 2548KB
#include<iostream>
#include<queue>

using namespace std;
int N, K;
int race[100002];
queue<int> q;
void teleport(int pos, int value)
{
	while (pos <= 100001 && race[pos] == -1)
	{
		race[pos] = value;
		q.push(pos);
		// arrive
		if (pos == K)
		{
			return;
		}
		pos *= 2;
	}
}
int main(void)
{
	cin >> N;
	cin >> K;
	fill(race, race + 100001, -1);
	int pos;
	q.push(N);
	race[N] = 0;
	teleport(N * 2, 0);
	while (!q.empty())
	{
		pos = q.front();
		q.pop();
		if (pos + 1 >= 0 && pos + 1 <= 100001 && race[pos + 1] == -1)
		{
			race[pos + 1] = race[pos] + 1;
			q.push(pos + 1);
			teleport((pos + 1) * 2, race[pos + 1]);
		}
		if (pos - 1 >= 0 && pos - 1 <= 100001 && race[pos - 1] == -1)
		{
			race[pos - 1] = race[pos] + 1;
			q.push(pos - 1);
			teleport((pos - 1) * 2, race[pos - 1]);
		}
	}
	cout << race[K];
}