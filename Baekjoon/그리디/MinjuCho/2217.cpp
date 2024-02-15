// 문제 풀이 링크: https://velog.io/@cuppizza/백준-2217-로프-C-파이썬-그리디-정렬
// 실행 시간: 36ms 메모리: 2412KB
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(void)
{
    int n;
    cin >> n;
    vector<int> ropes(n);
    for (int i=0; i<n; ++i)
    {
        cin >> ropes[i];
    }
    sort(ropes.begin(), ropes.end());

    int result = 0;
    for (int i=n; i>=0; --i)
    {
        result = max(result, (n - i) * ropes[i]);
    }
    cout << result;
}