// 문제 풀이 링크: https://velog.io/@cuppizza/백준-14719-빗물-C-투-포인터
// 실행 시간: 0ms 메모리: 2020KB
#include <iostream>
#include <vector>

using namespace std;
int main(void)
{
    int h, w;
    cin >> h >> w;
    vector<int> block(w);
    for (int i=0; i<w; ++i)
    {
        cin >> block[i];
    }
    int result = 0;
    // left
    // find start
    int start = 0, end = 0;
    for (int i=0; i<w; ++i)
    {
        if (block[i] > 0)
        {
            start = i;
            break;
        }
    }
    // find end
    for (int i=start+1; i<w; ++i)
    {
        if (block[i] >= block[start])
        {
            end = i;
            // fill
            for(int j=start+1; j<end; ++j)
            {
                result += block[start] - block[j];
            }
            start = end;
        }
    }

    // right
    // find start
    for (int i=w-1; i>=0; --i)
    {
        if (block[i] > 0)
        {
            start = i;
            break;
        }
    }
    // find end
    for (int i=start-1; i>=0; --i)
    {
        if (block[i] > block[start])
        {
            end = i;
            // fill
            for(int j=start-1; j>end; --j)
            {
                result += block[start] - block[j];
            }
            start = end;
        }
    }

    cout << result;
}
// 2 3
// 2 0 2 중복 계산 방지 위해 왼쪽/오른쪽 중 한 곳은 더 큰 블록으로!