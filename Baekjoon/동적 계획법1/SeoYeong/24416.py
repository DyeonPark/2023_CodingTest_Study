
def fibo_recursive(n):
    global recursive_n
    print(f"fibo_recursive({n})")
    if n == 0 or n == 1:
        recursive_n += 1; print(f'recursive_n={recursive_n}')
        return 1
    return fibo_recursive(n-1) + fibo_recursive(n-2)

def recursive_calc(n):
    # 재귀 호출 - 2^n
    return 

def fibo_dp(n):
    global dp_n
    f = [0 for _ in range(n+1)]
    f[0], f[1] = 1, 1
    for i in range(2, n+1):
        dp_n+=1
        f[i] = f[i-1] + f[i-2]
    return f[n]

n = int(input())
recursive_n, dp_n = 0, 0
fibo_recursive(n-1)
fibo_dp(n-1)
print(recursive_n, dp_n)
