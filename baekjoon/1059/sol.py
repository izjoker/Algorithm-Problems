from sys import stdin
def sol(s, n):
    s.sort()
    prev_e = 0
    for e in s:
        if e == n:
            return 0
        min_, max_ = [prev_e+1, e-1]
        if min_ <= n and n <= max_:
            return (n-min_+1) * (max_-n+1) - 1
        prev_e = e
    return 0

_ = int(stdin.readline().strip())
s = list(map(int, stdin.readline().split(" ")))
n = int(stdin.readline().strip())
print(sol(s, n))
