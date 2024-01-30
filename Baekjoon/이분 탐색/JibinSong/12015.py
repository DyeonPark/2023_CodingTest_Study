def get_idx(arr, key):  # key보다 크지만 가장 작은 값의 위치
  min_v = 0
  max_v = len(arr) - 1
  while True:
    if min_v > max_v:
      return min_v
    mid = (min_v + max_v) // 2
    if arr[mid] < key:
      min_v = mid + 1
    else:
      max_v = mid - 1


n = int(input())  # 10 20 30 15 20 25 50 45 55 60
array = list(map(int, input().split()))
result = [array[0]]

for i in array:
  if i > result[-1]:
    result.append(i)
  else:
    idx = get_idx(result, i)
    result[idx] = i

print(len(result))