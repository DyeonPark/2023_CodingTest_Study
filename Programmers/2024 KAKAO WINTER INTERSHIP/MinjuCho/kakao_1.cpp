#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

int solution(vector<string> friends, vector<string> gifts) {
    map<string, map<string, int>> info;
    map<string, int> points;
    for (auto elem : gifts)
    {
        stringstream ss(elem);
        ss.str(elem);
        string give, receive;
        ss >> give;
        ss >> receive;
        ++points[give];
        --points[receive];
        ++info[give][receive];
    }
    map<string, int> result;
    for (int i = 0; i < friends.size(); ++i)
    {
        string frnd = friends[i];
        for (int j = i + 1; j < friends.size(); ++j)
        {
            string with = friends[j];
            if (frnd == with)
            {
                continue;
            }
            if (info[frnd][with] > info[with][frnd])
            {
                ++result[frnd];
            }
            else if (info[frnd][with] < info[with][frnd])
            {
                ++result[with];
            }
            else
            {
                if (points[frnd] > points[with])
                {
                    ++result[frnd];
                }
                else if (points[frnd] < points[with])
                {
                    ++result[with];
                }
            }
        }
    }
    int answer = 0;
    for (auto elem : result)
    {
        if (elem.second > answer)
        {
            answer = elem.second;
        }
    }
    return answer;
}

int main(void)
{
    vector<string> friends = { "muzi", "ryan", "frodo", "neo" },
                    gifts = { "muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi",
                                "frodo muzi", "frodo ryan", "neo muzi" };
    printf("%d", solution(friends, gifts));
}