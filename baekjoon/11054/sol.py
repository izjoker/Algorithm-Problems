
# 문제

# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

# 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.
# 입력

# 첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)
# 출력

# 첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.


def sol(n, series):
    dp0 = [0]*(n+1)
    dp1 = [0]*(n+1)
    series = [0] + series
    print(series)
    for i in range(1, n+1):
        cands = []
        for j in range(1, i):
            if series[j] < series[i]:
                cands.append(dp0[j]+1)
        if cands:
            dp0[i] = max(cands)
        else:
            dp0[i] = 1
    
    series = [0]+list(reversed(series))
    for i in range(1, n+1):
        cands = []
        for j in range(1, i):
            if series[j] < series[i]:
                cands.append(dp1[j]+1)
        if cands:
            dp1[i] = max(cands)
        else:
            dp1[i] = 1
    dp1 = [0]+list(reversed(dp1[1:]))
    
    print(dp0)
    print(dp1)

    return max([e1+e2 for e1, e2 in zip(dp0, dp1)])

args = []
while True:
    try:
        args += [input()]
    except:
        break
n = int(args[0])
series = [int(e) for e in args[1].split(" ")]
print(sol(n, series))
