# 문제 풀이 링크: https://velog.io/@cuppizza/백준-1806-부분합-C-투-포인터
# 실행 시간: 144ms 메모리: 42204KB
import sys
input = sys.stdin.readline
n, s = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
start = 0
end = 0
sum_arr = arr[0]
result = int(1e9)
while end<n and start<=end:
    if sum_arr < s:
        end += 1
        if end >= n:
            break
        sum_arr += arr[end]
    else:
        result = min(result, end - start + 1)
        sum_arr -= arr[start]
        start += 1
if result == int(1e9):
    print(0)
else:
    print(result)
