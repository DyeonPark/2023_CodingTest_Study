"""
중복 원소가 있는 permutation 생성하는 문제 해결하는 방법 녹이면 될 듯
36236KB	128ms
"""
def get_all_possible_compute(op: list):
    result = []
    dp = set()

    if len(op) == 1: return [op[:]]
    for _ in range(len(op)):
        n = op.pop(0)
        if (n, len(op)) not in dp:
            perm = get_all_possible_compute(op)
            for p in perm: p.append(n)
            dp.add((n, len(op)))
            result.extend(perm)
        op.append(n)
    return result

def compute_by_permutation(op: list):
    res = nums[0]
    for x, operator in zip(nums[1:], op):
        if operator == 0: res +=x
        elif operator == 1: res -=x
        elif operator == 2: res *=x
        else: 
            if res < 0: res = abs(res)//x*(-1)
            else: res //= x
    return res


n = int(input())
nums = list(map(int, input().split()))
numof_ops = list(map(int, input().split()))
ops = []
for i, o in zip([0, 1, 2, 3], numof_ops):
    for _ in range(o):
        ops.append(i)

perm = get_all_possible_compute(ops)

max_val, min_val = -1e10, 1e10
for p in perm:
    val = compute_by_permutation(p)
    if val > max_val: 
        max_val = val
    if val < min_val:
        min_val = val

print(max_val)
print(min_val)
