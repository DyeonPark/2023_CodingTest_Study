// 문제 풀이 링크: https://velog.io/@cuppizza/백준-1697-숨바꼭질-C-파이썬
// 실행 시간: 0ms 메모리: 2292KB
#include <iostream>
#include <queue>
using namespace std;


int main(void)
{
    int N, K;
    cin >> N >> K;
    int position[100001] = {};
    queue<int> next_pos;
    next_pos.push(N);
    position[N] = 1;
    while (!next_pos.empty())
    {
        int cur_pos = next_pos.front();
        next_pos.pop();
        if(cur_pos - 1 >= 0 && position[cur_pos - 1] == 0)
        {
            position[cur_pos - 1] = position[cur_pos] + 1;
            next_pos.push(cur_pos - 1);
        }
        if(cur_pos + 1 < 100001 && position[cur_pos + 1] == 0)
        {
            position[cur_pos + 1] = position[cur_pos] + 1;
            next_pos.push(cur_pos + 1);
        }
        if (cur_pos * 2 < 100001 && position[cur_pos * 2] == 0)
        {
            position[cur_pos * 2] = position[cur_pos] + 1;
            next_pos.push(cur_pos * 2);
        }
        if(cur_pos + 1 == K || cur_pos - 1 == K || cur_pos * 2 == K)
        {
            cout << position[K] - 1;
            return 0;
        }
    }
}
// 실행 시간: 0ms 메모리: 2292KB
#include<iostream>
#include<queue>

using namespace std;
int main(void)
{
	int N, K;
	cin >> N;
	cin >> K;

	int pos[100002];
	fill(pos, pos + 100001, -1);

	int cur;
	queue<int> q;
	pos[N] = 0;
	q.push(N);
	while (!q.empty())
	{
		cur = q.front();
		q.pop();

		if (cur - 1 >= 0 && cur - 1 < 100002 && pos[cur - 1] == -1)
		{
			pos[cur - 1] = pos[cur] + 1;
			q.push(cur - 1);
		}

		if (cur + 1 >= 0 && cur + 1 < 100002 && pos[cur + 1] == -1)
		{
			pos[cur + 1] = pos[cur] + 1;
			q.push(cur + 1);
		}

		if (cur * 2 >= 0 && cur * 2 < 100002 && pos[cur * 2] == -1)
		{
			pos[cur * 2] = pos[cur] + 1;
			q.push(cur * 2);
		}

		if (cur - 1 == K || cur + 1 == K || cur * 2 == K)
		{
			cout << pos[K];
			return 0;
		}
	}
}