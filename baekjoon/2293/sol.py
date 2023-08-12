# 문제
# n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

# 입력
# 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 경우의 수를 출력한다. 경우의 수는 231보다 작다.

def sol(n, k, values):
    dp = [0]*(k+1)
    values.sort(reverse=True)
    for v in values:
        for i in range(v, k+1):
            if i == v:
                dp[i] += 1
            elif i > v:
                dp[i] += dp[i-v]
    
    return dp[k]

args = []
while True:
    try:
        args += [input()]
    except:
        break
n, k = [int(e) for e in args[0].split(" ")]
values = []
for line in args[1:]:
    values.append(int(line))
print(sol(n, k, values))