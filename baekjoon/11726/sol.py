
# 문제

# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

# 입력

# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# 출력

# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.



args = []
while True:
    try:
        args += [input()]
    except:
        break

def sol(n):
    dp = [0]*(n+1+2)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 10_007
    

for n in args:
    print(sol(int(n)))