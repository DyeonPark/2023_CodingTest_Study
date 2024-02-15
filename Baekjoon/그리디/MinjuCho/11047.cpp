// 문제 풀이 링크: https://velog.io/@cuppizza/백준-11047-동전-0-C-파이썬-그리디
// 실행 시간: 0ms 메모리: 2020KB
#include <iostream>
#include <vector>

using namespace std;
int main(void)
{
    int N, K;
    cin >> N >> K;
    vector<int> coins(N);
    for (int i=0; i<N; ++i)
    {
        int val;
        cin >> val;
        coins[i] = val;
    }
    int result = 0;
    for (int i = N-1; i >= 0 && K != 0; --i)
    {
        if (K / coins[i] == 0)
        {
            continue;
        }
        result += K / coins[i];
        K = K % coins[i];
    }
    cout << result;
}