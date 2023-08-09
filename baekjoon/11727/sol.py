
# 문제

# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.

# 입력

# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# 출력

# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.



def sol(n):
    dp = [0]*(n+1+2)
    dp[1] = 1
    dp[2] = 3
    
    for i in range(3, n+1):
        dp[i] = dp[i-1]+2*dp[i-2]
    return dp[n] % 10007

args = [] 
while True:
    try:
        args += [input()]
    except:
        break
n = int(args[0])

print(sol(n))