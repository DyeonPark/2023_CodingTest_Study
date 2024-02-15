// 문제 풀이 링크: https://velog.io/@cuppizza/백준-16928-뱀과-사다리-게임-C-파이썬-BFS-최단거리
// 실행 시간: 0ms 메모리: 2028KB
#include <map>
#include <queue>
#include <vector>
#include <iostream>

using namespace std;
int main(void)
{
    int n, m;
    cin >> n >> m;
    map<int, int> ladders, snakes;
    int x, y;
    for (int i=0; i<n; ++i)
    {
        cin >> x >> y;
        ladders[x] = y;
    }
    for (int i=0; i<m; ++i)
    {
        cin >> x >> y;
        snakes[x] = y;
    }
    queue<int> q;
    q.push(1);
    vector<int> board(101, 0);
    board[1] = 1;
    int cur;
    while(!q.empty())
    {
        cur = q.front();
        q.pop();
        for(int i=1; i<=6; ++i)
        {
            if (cur+i <= 100 && board[cur+i] == 0)
            {
                board[cur+i] = board[cur] + 1;
                if(ladders[cur+i] != 0 && board[ladders[cur+i]] == 0)
                {
                    board[ladders[cur+i]] = board[cur+i];
                    q.push(ladders[cur+i]);
                    continue;
                }
                else if(snakes[cur+i] != 0 && board[snakes[cur+i]] == 0)
                {
                    board[snakes[cur+i]] = board[cur+i];
                    q.push(snakes[cur+i]);
                    continue;
                }
                else if ((snakes[cur+i] != 0 && board[snakes[cur+i]] != 0)||(ladders[cur+i] != 0 && board[ladders[cur+i]] != 0))
                {
                    continue;
                }
                q.push(cur+i);
            }
        }
    }
    cout << board[100]-1;
}