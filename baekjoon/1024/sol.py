# 문제
# N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 L이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이고, L은 2보다 크거나 같고, 100보다 작거나 같은 자연수이다.

# 출력
# 만약 리스트의 길이가 100보다 작거나 같으면, 연속된 수를 첫째 줄에 공백으로 구분하여 출력한다. 만약 길이가 100보다 크거나 그러한 수열이 없을 때는 -1을 출력한다.

# k k+1 k+2..
# i(k + k+i-1)/2
# = i(2k+i-1)/2 = n
# (2*n/i +1 -i)/2 = k 

from sys import stdin
def sol(n, l):
    for i in range(l, 101):
        k = ((2*n/i+1-i)/2)
        if k.is_integer() and k >= 0:
            return " ".join([str(int(e+k)) for e in range(i)])    
    return -1
n, l = map(int, stdin.readline().strip().split(" "))

print(sol(n, l))