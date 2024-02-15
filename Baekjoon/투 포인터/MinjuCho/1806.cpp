// 문제 풀이 링크: https://velog.io/@cuppizza/백준-1806-부분합-C-투-포인터
// 실행 시간: 32ms 메모리: 2412KB
#include<vector>
#include<iostream>
#include<algorithm>
#include<climits>

using namespace std;

int main(void)
{
	int n, s;
	cin >> n >> s;
	vector<int> arr(n);
	for (int i = 0; i < n; ++i)
	{
		cin >> arr[i];
	}

	int start = 0, end = 0;
	int sum = arr[0];
	int result = INT_MAX;
	while (end < n && start <= end)
	{
		if (sum >= s)
		{
			result = min(end - start + 1, result);
			sum -= arr[start];
			++start;
		}
		else
		{
			++end;
			sum += arr[end];
		}
	}
	if (result == INT_MAX)
	{
		cout << "0";
		return 0;
	}
	cout << result;
}

/* 이분탐색 풀이, 실패
int main(void)
{
	int n, s;
	cin >> n >> s;
	vector<int> arr(n);
	for (int i = 0; i < n; ++i)
	{
		cin >> arr[i];
	}

	int max_elem, min_elem;
	max_elem = *max_element(arr.begin(), arr.end());
	min_elem = *min_element(arr.begin(), arr.end());

	int start, end;
	start = 1;
	if (max_elem == s)
	{
		cout << "1";
		return 0;
	}
	else if (max_elem < s)
	{
		end = s - max_elem;
	}
	else
	{
		if (min_elem > s)
		{
			cout << "0";
			return 0;
		}
		if (min_elem == s)
		{
			cout << "1";
			return 0;
		}
		else
		{
			end = arr.size();
		}
	}
	int result = 0;
	while (start <= end)
	{
		int mid = (start + end) / 2;
		bool canSum = false;
		for (int i = 0; i < n - mid + 1; ++i)
		{
			int part_sum = 0;
			for (int j = i; j < i + mid; ++j)
			{
				part_sum += arr[j];
			}
			if (part_sum >= s)
			{
				canSum = true;
				break;
			}
		}
		if (canSum)
		{
			result = mid;
			end = mid - 1;
		}
		else
		{
			start = mid + 1;
		}
	}
	cout << result;
}
*/