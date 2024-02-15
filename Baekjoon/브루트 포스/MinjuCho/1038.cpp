// 문제 풀이 링크: https://velog.io/@cuppizza/백준-1038-감소하는-수-C-브루트-포스
// 실행 시간: 0ms 메모리: 2020KB
#include<iostream>
#include<queue>

using namespace std;
int main(void)
{
	long long n;
	cin >> n;
	queue<long long> q;
	for (int i = 0; i < 10; ++i)
	{
		q.push(i);
	}
	long long cnt = 0, num = -1;
	while (cnt <= n)
	{
		if (q.empty())
		{
			cout << "-1";
			return 0;
		}
		num = q.front();
		q.pop();
		++cnt;
		long long x = num % 10;
		for (long long i = 0; i < x; ++i)
		{
			q.push(num * 10 + i);
		}
	}
	cout << num;
}