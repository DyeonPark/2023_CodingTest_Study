# 문제 풀이 링크: https://velog.io/@cuppizza/백준-14719-빗물-C-투-포인터
# 실행 시간: 44ms 메모리: 31120KB
import sys
input = sys.stdin.readline
h, w = map(int, input().strip().split())
blocks = list(map(int, input().strip().split()))
result = 0
# left
# find start
start = 0
end = 0
for i in range(w):
    if blocks[i] > 0:
        start = i
        break
# find end
for i in range(start+1, w):
    if blocks[i] >= blocks[start]:
        end = i
        # fill
        for j in range(start+1, end):
            result += blocks[start] - blocks[j]
        start = end
# right
# find start
start = w-1
end = w-1
for i in range(w-1, -1, -1):
    if blocks[i] > 0:
        start = i
        break
# find end
for i in range(start-1, -1, -1):
    if blocks[i] > blocks[start]:
        end = i
        # fill
        for j in range(start-1, end, -1):
            result += blocks[start] - blocks[j]
        start = end
print(result)
