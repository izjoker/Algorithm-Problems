# 문제
# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

# 출력
# 첫째 줄에 경우의 수를 출력한다.

def sol(n):
    dp = [0]*(n+1)
    for i in range(2, n+1):
        for j in range(1, i+1):
            if j == 2:
                dp[i] += 3*dp[i-j]
            elif j%2 == 0:
                dp[i] += 2*dp[i-j]
        
        if i == 2:
            dp[i] += 3
        elif i % 2 == 0:
            dp[i] += 2
    return dp[n]

args = []
while True:
    try:
        args += [input()]
    except:
        break
n = int(args[0])
print(sol(n))
