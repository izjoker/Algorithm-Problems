# 문제
# N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수, 또는 제일 큰 정수를 찾는 것은 어려운 일이 아니다. 하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다. 이 문제를 해결해 보자.

# 여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최소, 최댓값을 찾아야 한다. 각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.

# 입력
# 첫째 줄에 N, M이 주어진다. 다음 N개의 줄에는 N개의 정수가 주어진다. 다음 M개의 줄에는 a, b의 쌍이 주어진다.

# 출력
# M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 최솟값, 최댓값 순서로 출력한다.
import sys
sys.setrecursionlimit(10**6)
class SegTree(list):
    def __init__(self, series):
        self.source = [-1] + series
        self.tree = [[float('inf'), -float('inf')] for i in range(4*len(series))]   
        self.buildtree()

    def buildtree(self):
        def build(s, e, idx):
            if s == e:
                self.tree[idx] = [self.source[s], self.source[s]]
                return
            mid = (s+e)//2
            for i in range(s, e+1):
                self.tree[idx][0] = min(self.tree[idx][0], self.source[i])
                self.tree[idx][1] = max(self.tree[idx][1], self.source[i])
            build(s, mid, 2*idx)
            build(mid+1, e, 2*idx+1)
        build(1, len(self.source)-1, 1)

    def searchRange(self, ran):
        def search(s, e, idx, ran):
            if e < ran[0] or s > ran[1]:
                return [float('inf'), -float('inf')]
            if ran[0] <= s and e <= ran[1]:
                return self.tree[idx]
            mid = (s+e)//2
            left = search(s, mid, idx*2, ran)
            right = search(mid+1, e, idx*2+1, ran)
            return [min(left[0], right[0]), max(left[1], right[1])]
        return search(1, len(self.source)-1, 1, ran)

    def changeValue(self, v_i, v):
        self.source[v_i] = v
        def change(s, e, idx, v_i, v):
            if e < v_i or s > v_i or s == e:
                return
            if s <= v_i <= e:
                self.tree[idx] = [min(self.tree[idx][0], v), max(self.tree[idx][1], v)]
            mid = (s+e)//2
            left = change(s, mid, idx*2, v_i, v)
            right = change(mid+1, e, idx*2+1, v_i, v)
        change(1, len(self.source)-1, 1, v_i, v)
        

from sys import stdin
def sol(n, m, series, rans):
    r = []
    tree = SegTree(series)
    tree.changeValue(1, 999)
    for ran in rans:
        r.append(tree.searchRange(ran))

    
    return r

n, m = map(int, stdin.readline().strip().split(" "))
series = []
for i in range(n):
    series.append(int(stdin.readline().strip()))
rans = []
for i in range(m):
    rans.append(tuple(map(int, stdin.readline().strip().split(" "))))
v = sol(n, m, series, rans)
for row in v:
    print(" ".join(map(str, row)))
