#include <vector>
#include <queue>
#include <stdio.h>

#define weight first
#define vertex second
using namespace std;

const int INF = 0x3f3f3f3f;
int n, m, st, en;
vector<pair<int, int>> adj[1001];
int pre[1001], d[1001];
int main(void)
{
    scanf("%d %d", &n, &m);
    while (m--)
    {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        adj[u].push_back({ w, v });
    }
    scanf("%d %d", &st, &en);

    fill(d, d + n + 1, INF);
    d[st] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({ 0, st });
    while (!pq.empty())
    {
        pair<int, int> cur = pq.top(); pq.pop();
        if (d[cur.vertex] != cur.weight)
        {
            continue;
        }
        for (pair<int, int> next : adj[cur.vertex])
        {
            if (d[next.vertex] <= d[cur.vertex] + next.weight)
            {
                continue;
            }
            d[next.vertex] = d[cur.vertex] + next.weight;
            pq.push({ d[next.vertex], next.vertex });
            pre[next.vertex] = cur.vertex;
        }
    }
    // 경로 복원
    vector<int> path;
    int curPath = en;
    while (curPath != st)
    {
        path.push_back(curPath);
        curPath = pre[curPath];
    }
    path.push_back(curPath);

    printf("%d\n", d[en]);
    printf("%d\n", (int)path.size());
    for (int i = path.size() - 1; i >= 0; --i)
    {
        printf("%d ", path[i]);
    }
}