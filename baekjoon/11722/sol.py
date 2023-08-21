
# 문제

# 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.
# 입력

# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
# 출력

# 첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

def sol(n, arg):
    dp = [0]*(n+1)
    series = [0] + arg
    for i in range(1, n+1):
        cands = []
        for j in range(1, i):
            if series[i] < series[j]:
                cands.append(dp[j])
        if cands:
            dp[i] = max(cands)+1
        else:
            dp[i] = 1

    return max(dp)



args = []
while True:
    try:
        args += [input()]
    except:
        break
n = int(args[0])
arg = [int(e) for e in args[1].split(" ")]
print(sol(n, arg))
