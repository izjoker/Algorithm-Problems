from sys import stdin
def dfs(s, e, dp, matsizes):
    print(dp, s, e)
    if s == e:
        return 0
    if s+1 == e:
        return matsizes[s][0]*matsizes[s][1]*matsizes[e][1]
    if dp[s][e] != -1:
        return dp[s][e]
    r = float('inf')
    
    for i in range(s+1, e-1):
        r = min(r, dfs(s, i-1, dp, matsizes)+matsizes[s][0]*matsizes[i][0]*matsizes[e][1]+ dfs(i+2, e, dp, matsizes))
        print(r)
    dp[s][e] = r
    return r

def sol(n, matsizes):  
    dp = [[-1 for i in range(len(matsizes))] for i in range(len(matsizes))]

    return dfs(0, len(matsizes)-1, dp, matsizes)
def matmul(matsize1, matsize2):
    a, b = matsize1
    b, c = matsize2
    return [(a, c), a*b*c]

n = int(stdin.readline().strip())
matsizes = []
for i in range(n):
    matsizes.append(tuple(map(int, stdin.readline().strip().split(" "))))
print(sol(n, matsizes))