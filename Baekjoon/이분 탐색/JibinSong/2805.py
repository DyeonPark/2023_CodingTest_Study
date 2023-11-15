n, m = map(int, input().split())

arr = list(map(int, input().split()))

min_h = max(arr) - m  # 절단기 높이의 최솟값
max_h = max(arr)  # 절단기 높이의 최댓값

def count_length(mid):
  cnt = 0
  for i in arr:
    if i > mid:
      cnt += i - mid
  return cnt

while True:
  print(f"min: {min_h}, max: {max_h}, mid: {(min_h + max_h) // 2}")
  if min_h > max_h:
    print(max_h)
    break
  mid = (min_h + max_h) // 2
  cnt = count_length(mid)
  print(f"cnt: {cnt}")
  if cnt >= m:
    min_h = mid + 1
  else:
    max_h = mid - 1