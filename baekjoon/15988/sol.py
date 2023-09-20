from sys import stdin
DIV = 1_000_000_009
def sol(n):
    dp1 = 1
    dp2 = 2
    dp3 = 4
    if n == 1:
        return dp1
    if n == 2:
        return dp2
    if n == 3:
        return dp3
    for i in range(4, n+1):
        dp4 = (dp1+dp2+dp3) % DIV
        dp1=dp2 
        dp2=dp3
        dp3=dp4
    return dp4
t = int(stdin.readline().strip())
for i in range(t):
    n = int(stdin.readline().strip())
    print(sol(n))