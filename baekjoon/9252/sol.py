
from sys import stdin
def sol(arg1, arg2):
    str1, str2 = [arg1, arg2]
    if len(arg1) > len(arg2):
        str1, str2 = [arg2, arg1] 
    str1, str2 = [" "+str1, " "+str2]
    dp = [["" for _ in range(len(str2))] for _ in range(len(str1))]

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1]+str2[j] 
            else:
                dp[i][j] = max([dp[i-1][j], dp[i][j-1]], key=lambda x: len(x))
    r_str = max(dp[-1], key=lambda x: len(x))
    r_len = str(len(r_str))

    return r_len+"\n"+r_str

arg1 = str(stdin.readline().strip())
arg2 = str(stdin.readline().strip())
print(sol(arg1, arg2))
