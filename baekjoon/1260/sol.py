# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

    # 그래프 자료구조
        # 인접 행렬
        # 인접 리스트
import sys
sys.setrecursionlimit(10**6)
def dfslst(lst, v, visit):
    if visit[v]:
        return []
    r = [v]
    visit[v] = True
    for node in sorted(lst[v]):
        r += dfslst(lst, node, visit)
    return r

def bfslst(lst, v):
    r = []
    visitmap = {}
    q = [v]
    while q:
        v = q.pop(0)
        if v in visitmap:
            continue
        visitmap[v] = True
        for node in sorted(lst[v]):
            q.append(node)
        r += [v]
    return r

def sol(m, n, v, edges):
    lst = [[] for i in range(n+1)]
    for edge in edges:
        v1, v2 = edge
        lst[v1].append(v2)
        lst[v2].append(v1)
    
    visitdfs = [False]*(n+1)
    return " ".join(map(str, dfslst(lst, v, visitdfs))) + "\n" + " ".join(map(str, bfslst(lst, v)))
    
                
args = []
while True:
    try:
        args += [input()]
    except:
        break
m, n, v = [int(e) for e in args[0].split(" ")]
edges = [[int(e) for e in line.split(" ")] for line in args[1:]]

print(sol(m, n, v, edges))