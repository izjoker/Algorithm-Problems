from sys import stdin
MAX = 2**31-1
def sol(matsizes):
    dp = [[0 for i in range(len(matsizes))] for j in range(len(matsizes))]
    for i in range(len(matsizes)):
        for j in range(len(matsizes)-i):
            a = j
            b = j+i
            for k in range(a, b):
                if dp[a][b] != 0:
                    dp[a][b] = min(dp[a][b], dp[a][k]+dp[k+1][b]+matsizes[a][0]*matsizes[k][1]*matsizes[b][1])
                else:
                    dp[a][b] = dp[a][k]+dp[k+1][b]+matsizes[a][0]*matsizes[k][1]*matsizes[b][1]
    return dp[0][-1]

n = int(stdin.readline().strip())
matsizes = []
for i in range(n):
    matsizes.append(list(map(int, stdin.readline().strip().split(" "))))
print(sol(matsizes))