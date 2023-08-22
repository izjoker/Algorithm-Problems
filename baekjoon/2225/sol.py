# 문제
# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.

# 입력
# 첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

# 출력
# 첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.
def sol(n, k):
    dp = [[0 for i in range(k+1)] for i in range(n+1)]
    for i in range(len(dp)):
        dp[i][1] = 1
    for i in range(2, k+1):
        for j in range(n+1):
            for k_ in range(j+1):
                dp[j][i] += dp[j-k_][i-1]
    return dp[n][k]%1_000_000_000
n, k = map(int, input().split(" "))
print(sol(n, k))
