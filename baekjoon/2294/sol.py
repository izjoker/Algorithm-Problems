# 문제
# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

# 입력
# 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

# 출력
# 첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.
# dp[7] dp[1]+dp[6]
# dp[6] dp[1]+dp[5]
def sol(n, k, values):
    dp = [float('inf')]*(k+1)
    values.sort(reverse=True)
    for v in values:
        for i in range(v, k+1):
            if i == v:
                dp[i] = 1
            else:
                dp[i] = min(dp[i], dp[v]+dp[i-v])
    return dp[k] if dp[k] != float('inf') else -1

n, k = map(int, input().split(" "))
coins = []
for i in range(n):
    coins.append(int(input()))
print(sol(n, k, coins))