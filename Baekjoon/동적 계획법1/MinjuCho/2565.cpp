#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
	int N;
	cin >> N;

	// B �迭 0 ~ 500 ���� 501�� �ʱ�ȭ
	int a, b, B[501];
	fill_n(B, 501, 501);
	for (int i = 0; i < N; ++i)
	{
		cin >> a >> b;
		B[a] = b;
	}

	// dp �迭 0 ~ 500 ���� 1�� �ʱ�ȭ
	int dp[501];
	fill_n(dp, 501, 1);
	for (int a = 1; a < 501; ++a)
	{
		for (int j = 1; j < a; ++j)
		{
			if (B[j] < B[a] && B[a] != 501)
			{
				// �Ȱ�ġ�� ��� ã��
				dp[a] = max(dp[j] + 1, dp[a]);
			}
		}
	}
	cout << N - *max_element(dp, dp + 501);
}