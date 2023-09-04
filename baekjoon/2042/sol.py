# 문제
# 어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b(1 ≤ b ≤ N)번째 수를 c로 바꾸고 a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력하면 된다.

# 입력으로 주어지는 모든 수는 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.
import sys
sys.setrecursionlimit(10**6)
from sys import stdin
def createSegtree(series, segtree):
    def build(s, e, idx):
        if s == e:
            segtree[idx] = series[s]
            return  
        for i in range(s, e+1):
            segtree[idx] += series[i]
        mid = (e+s)//2
        build(s, mid, idx*2)
        build(mid+1, e, idx*2+1)
    build(0, len(series)-1, 1)

def rangeSum(segtree, ran, size):
    def search(s, e, idx, ran):
        if e < ran[0] or s > ran[1]:
            return 0
        if ran[0] <= s and e <= ran[1]:
            return segtree[idx]
        mid = (e+s)//2
        return search(s, mid, idx*2, ran) + search(mid+1, e, idx*2+1, ran) 
    return search(1, size, 1, ran)

def treeReplaceElem(segtree, replace, size):
    def search(s, e, idx, replace):
        if s <= replace[0] <= e:    
            segtree[idx] += replace[2]
            segtree[idx] -= replace[1]
        else:
            return
        if s == e:
            return
        mid = (e+s)//2
        search(s, mid, idx*2, replace)
        search(mid+1, e, idx*2+1, replace) 
    search(1, size, 1, replace)


n, m, k = map(int, stdin.readline().split(" "))
series = []
for i in range(n):
    series.append(int(stdin.readline()))
segtree = [0] * len(series)*4
createSegtree(series, segtree)
for i in range(m+k):
    a, b, c = map(int, stdin.readline().split(" "))
    if a == 1:
        treeReplaceElem(segtree, [b, series[b-1], c], len(series))
        series[b-1] = c
    else:
        print(rangeSum(segtree, [b, c], len(series)))
