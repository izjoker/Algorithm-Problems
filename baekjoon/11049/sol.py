from sys import stdin
<<<<<<< HEAD
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
=======
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
>>>>>>> bb01eee589e11ce1c6b4e317837df0723c0a36f7

n = int(stdin.readline().strip())
matsizes = []
for i in range(n):
<<<<<<< HEAD
    matsizes.append(tuple(map(int, stdin.readline().strip().split(" "))))
print(sol(n, matsizes))
=======
    matsizes.append(list(map(int, stdin.readline().strip().split(" "))))
print(sol(matsizes))
>>>>>>> bb01eee589e11ce1c6b4e317837df0723c0a36f7
