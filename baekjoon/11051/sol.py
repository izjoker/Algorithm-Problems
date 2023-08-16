#  문제

# 자연수
# \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수

# \(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
# 입력

# 첫째 줄에
# \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 1,000, 0 ≤ \(K\) ≤

# \(N\))
# 출력

 
# \(\binom{N}{K}\)를 10,007로 나눈 나머지를 출력한다.
DIV = 10_007
def sol(n, k):
    dp = [[0]*(n+1) for i in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
    return dp[n][k] % DIV
    
args = []
while True:
    try:
        args += [input()]
    except:
        break
n, k = [int(e) for e in args[0].split(" ")]
print(sol(n, k))
