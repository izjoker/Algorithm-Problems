# 문제
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 출력
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
from sys import stdin
class SegTree:
    def __init__(self, series):
        self.tree = [0]*len(series)*4
        self.source = [0] + series
        self.buildtree()

    def buildtree(self):
        def build(s, e, idx):
            if s == e:
                self.tree[idx] = self.source[s]
                return
            mid = (s+e)//2
            self.tree[idx] = sum(self.source[s:e+1])
            build(s, mid, idx*2)
            build(mid+1, e, idx*2+1)
        build(1, len(self.source)-1, 1)

    def searchRan(self, ran):
        def search(s, e, idx, ran):
            if e < ran[0] or s > ran[1]:
                return 0
            if ran[0] <= s and e <= ran[1]:
                return self.tree[idx]
            mid = (s+e)//2
            return search(s, mid, 2*idx, ran) + search(mid+1, e, 2*idx+1, ran)
        return search(1, len(self.source)-1, 1, ran)
            
def sol(n, m, series, rans):
    segtree = SegTree(series)
    r = []
    for ran in rans:
        r.append(segtree.searchRan(ran))
    return "\n".join(map(str, r))

n, m = map(int, stdin.readline().strip().split(" "))
series = list(map(int, stdin.readline().strip().split(" ")))
rans = []
for i in range(m):
    rans.append(list(map(int, stdin.readline().strip().split(" "))))
print(sol(n, m, series, rans))