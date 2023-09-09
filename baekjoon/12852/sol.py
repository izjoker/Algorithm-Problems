from sys import stdin
def sol(n):
    dp = [[0, []] for i in range(n+1+1)]
    dp[1] = [0, [1]]
    for i in range(2, n+1):
        dp[i] = [dp[i-1][0]+1, [i]+dp[i-1][1]]
        if i%3 == 0:
            dp[i] = min(dp[i], [dp[i//3][0]+1, [i]+dp[i//3][1]])
        if i%2 == 0:
            dp[i] = min(dp[i], [dp[i//2][0]+1, [i]+dp[i//2][1]])
    
    return str(dp[n][0])+"\n"+" ".join(map(str, dp[n][1]))
n = int(stdin.readline().strip())
print(sol(n))
