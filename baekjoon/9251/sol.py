

# 문제

# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
# 입력

# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
# 출력

# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.



def sol(arg1, arg2):
    str1, str2 = [arg1, arg2]
    if len(arg1) > len(arg2):
        str1, str2 = [arg2, arg1] 
    str1, str2 = [" "+str1, " "+str2]
    dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1]+1 
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return max(dp[-1])



args = []
while True:
    try:
        args += [input()]
    except:
        break
arg1 = args[0]
arg2 = args[1]
print(sol(arg1, arg2))
