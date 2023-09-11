from sys import stdin
MAX = float('inf')
def dp(s, e, memo, series, accsum):
    if s == e:
        return 0
    if e-s == 1:
        memo[s][e] = series[s]+series[e]
        return series[s]+series[e]
    if memo[s][e] != 0:
        return memo[s][e]
    r = MAX

    sum_ = accsum[e] if s-1 < 0 else accsum[e]-accsum[s-1]
    for i in range(s, e):
        
        r = min(r, dp(s, i, memo, series, accsum)+dp(i+1, e, memo, series, accsum) + sum_)
    memo[s][e] = r
    return r

def sol(n, series):
    memo = [[0 for j in range(n+1)] for i in range(n+1)]
    accsum = []
    sum_ = 0
    for e in series:
        sum_ += e
        accsum.append(sum_)
    return dp(0, n-1, memo, series, accsum)
    
t = int(stdin.readline().strip())
for i in range(t):
    n = int(stdin.readline().strip())
    series = list(map(int, stdin.readline().strip().split(" ")))
    print(sol(n, series))