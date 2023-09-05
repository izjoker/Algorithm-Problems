# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

from sys import stdin
def sol(n, series):
    dp = [[0, []] for i in range(len(series))] 
    for i in range(len(series)):
        cands = []
        for j in range(i):
            if series[j] < series[i]:
                cands.append(dp[j])
        if cands:
            v, lst = max(cands)
            dp[i] = [v+1, lst+[series[i]]]
        else:
            dp[i] = [1, [series[i]]]
    r = max(dp)
    r[0] = str(r[0])
    r[1] = " ".join(map(str, r[1]))
    return "\n".join(r)
    
n = int(stdin.readline().strip())
series = list(map(int, stdin.readline().strip().split(" ")))

print(sol(n, series))