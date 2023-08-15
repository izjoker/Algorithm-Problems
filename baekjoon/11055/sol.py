# 문제
# 수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가하는 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 합이 가장 큰 증가하는 부분 수열의 합을 출력한다.

def sol(n, series):
    dp = [0]*(n+1)
    series = [0]+series
    for i in range(1, n+1):
        cands = []
        for j in range(1, i):
            if series[j] < series[i]:
                cands.append(dp[j])
        if cands:
            dp[i] = max(cands)+series[i]
        else:
            dp[i] = series[i]
    return max(dp)
                
args = []
while True:
    try:
        args += [input()]
    except:
        break
n = int(args[0])
series = [int(e) for e in args[1].split(" ")]

print(sol(n, series))