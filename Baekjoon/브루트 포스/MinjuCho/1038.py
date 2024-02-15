# 문제 풀이 링크: https://velog.io/@cuppizza/백준-1038-감소하는-수-C-브루트-포스
# 실행 시간: 96ms 메모리: 37976KB
from queue import deque
n = int(input())
q = deque()
for i in range(10):
    q.append(i)
cnt = 0
while cnt <= n:
    cnt += 1
    if len(q) == 0:
        print(-1)
        exit(0)
    num = q.popleft()
    for i in range(0, num % 10):
        q.append(num * 10 + i)
print(num)
