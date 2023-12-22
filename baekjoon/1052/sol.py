
# 문제

# 지민이는 N개의 물병을 가지고 있다. 각 물병에는 물을 무한대로 부을 수 있다. 처음에 모든 물병에는 물이 1리터씩 들어있다. 지민이는 이 물병을 또 다른 장소로 옮기려고 한다. 지민이는 한 번에 K개의 물병을 옮길 수 있다. 하지만, 지민이는 물을 낭비하기는 싫고, 이동을 한 번보다 많이 하기는 싫다. 따라서, 지민이는 물병의 물을 적절히 재분배해서, K개를 넘지 않는 비어있지 않은 물병을 만들려고 한다.

# 물은 다음과 같이 재분배 한다.

#     먼저 같은 양의 물이 들어있는 물병 두 개를 고른다. 그 다음에 한 개의 물병에 다른 한 쪽에 있는 물을 모두 붓는다. 이 방법을 필요한 만큼 계속 한다.

# 이런 제약 때문에, N개로 K개를 넘지않는 비어있지 않은 물병을 만드는 것이 불가능할 수도 있다. 다행히도, 새로운 물병을 살 수 있다. 상점에서 사는 물병은 물이 1리터 들어있다.

# 예를 들어, N=3이고, K=1일 때를 보면, 물병 3개로 1개를 만드는 것이 불가능하다. 한 병을 또다른 병에 부으면, 2리터가 들어있는 물병 하나와, 1리터가 들어있는 물병 하나가 남는다. 만약 상점에서 한 개의 물병을 산다면, 2리터가 들어있는 물병 두 개를 만들 수 있고, 마지막으로 4리터가 들어있는 물병 한 개를 만들 수 있다.
# 입력

# 첫째 줄에 N과 K가 주어진다. N은 107보다 작거나 같은 자연수이고, K는 1,000보다 작거나 같은 자연수이다.
# 출력

# 첫째 줄에 상점에서 사야하는 물병의 최솟값을 출력한다. 만약 정답이 없을 경우에는 -1을 출력한다.

# 요구되는 조건
# n의 2진수표현 보다 크거나 같은 값 가운데 각 자릿수의 1의 갯수의 합이 k개 이하인 최소의 수 구함
# n과 위 수의 차분을 출력

# 인풋: 3 1
# bin: 11
# target: 100
# diff = 4-3 = 1

# 인풋: 13 2
# bin: 1101
# target: 10000
# diff = 16-13 = 3

# 인풋: 1 1
# bin: 1
# target: 1
# diff = 1-1 = 0

# 10111
# 11000
# ans = 1

# 1갯수가 k보다 작거나 같음
# 0 통과
# 1 갯수가 k 보다 많음
# 

# 버그: 2진수표현이 k개의 1만으로 표현된경우 0 출력해야함
# 여기에 덧셈해서 버그발생
from sys import stdin
def dec2bin(num):
    r = ""
    while num > 0:
        digit = num % 2
        num = num // 2
        r = str(digit) + r
    return r

def bin2dec(bin_):
    r = 0
    for i, ch in enumerate(reversed(bin_)):
        r += 2**i * int(ch)
    return r

def sol(n, k):
    bin_ = dec2bin(n)
    if bin_.count("1") <= k:
        return 0
    base = ""
    add = ""
    for ch in bin_:
        if ch == "1" and k > 0:    
            k -= 1
            base += ch    
            if k == 0:
                add += "1"
        else:
            base += "0"
            add += "0"
    target = bin2dec(base) + bin2dec(add)
    ans = target-n
    return ans

n, k = map(int, stdin.readline().split(" "))

print(sol(n, k))