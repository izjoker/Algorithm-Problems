# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

def sol(n, m, arr1, arr2):
    arr1.sort()
    arr2_ = [(e, i) for i, e in enumerate(arr2)]
    arr2_.sort()
    j = 0
    ans = [0]*(len(arr2))
    for i in range(len(arr2_)):
        while True:
            if j >= len(arr1) or arr2_[i][0] < arr1[j]:
                ans[arr2_[i][1]] = 0
                break
            if arr2_[i][0] > arr1[j]:
                j+=1
            elif arr2_[i][0] == arr1[j]:
                ans[arr2_[i][1]] = 1
                break
            
    return "\n".join(map(str, ans))
        

args = []
while True:
    try:
        args.append(input())
    except:
        break
n = int(args[0])
arr1 = args[1].split(" ")
m = int(args[2])
arr2 = args[3].split(" ")

print(sol(n, m, arr1, arr2))
