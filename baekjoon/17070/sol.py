# 문제
# 유현이가 새 집으로 이사했다. 새 집의 크기는 N×N의 격자판으로 나타낼 수 있고, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽이다.

# 오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 파이프는 아래와 같은 형태이고, 2개의 연속된 칸을 차지하는 크기이다.



# 파이프는 회전시킬 수 있으며, 아래와 같이 3가지 방향이 가능하다.



# 파이프는 매우 무겁기 때문에, 유현이는 파이프를 밀어서 이동시키려고 한다. 벽에는 새로운 벽지를 발랐기 때문에, 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.

# 파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 파이프는 밀면서 회전시킬 수 있다. 회전은 45도만 회전시킬 수 있으며, 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.

# 파이프가 가로로 놓여진 경우에 가능한 이동 방법은 총 2가지, 세로로 놓여진 경우에는 2가지, 대각선 방향으로 놓여진 경우에는 3가지가 있다.

# 아래 그림은 파이프가 놓여진 방향에 따라서 이동할 수 있는 방법을 모두 나타낸 것이고, 꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.



# 가로



# 세로



# 대각선

# 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.

# 입력
# 첫째 줄에 집의 크기 N(3 ≤ N ≤ 16)이 주어진다. 둘째 줄부터 N개의 줄에는 집의 상태가 주어진다. 빈 칸은 0, 벽은 1로 주어진다. (1, 1)과 (1, 2)는 항상 빈 칸이다.

# 출력
# 첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수를 출력한다. 이동시킬 수 없는 경우에는 0을 출력한다. 방법의 수는 항상 1,000,000보다 작거나 같다.

from sys import stdin
import sys
sys.setrecursionlimit(10**6)
def dfs(state, table, goal, dp):
    loc1, loc2, pose = state
    if not (0 <= loc1[0] < len(table) and \
        0 <= loc2[0] < len(table) and \
        0 <= loc1[1] < len(table[0]) and \
        0 <= loc2[1] < len(table[0])):
        return 0

    if pose != 2 and not table[loc2[0]][loc2[1]] == 0:
        return 0
    elif pose == 2 and \
        not (table[loc2[0]][loc2[1]] == 0 and \
             table[loc2[0]-1][loc2[1]] == 0 and \
             table[loc2[0]][loc2[1]-1] == 0):
        return 0

    if [loc2[0], loc2[1]] == goal:
        dp[state] = 1
        return 1
    if state in dp:
        return dp[state]
    r = 0
    if pose == 0:
        for d in [((0, 1), (0, 1), 0), ((0, 1), (1, 1), 2)]:
            dloc1, dloc2, nextpose = d
            nextloc1 = (loc1[0]+dloc1[0], loc1[1]+dloc1[1])
            nextloc2 = (loc2[0]+dloc2[0], loc2[1]+dloc2[1])
            r += dfs((nextloc1, nextloc2, nextpose), table, goal, dp)    
    elif pose == 1:
        for d in [((1, 0), (1, 0), 1), ((1, 0), (1, 1), 2)]:
            dloc1, dloc2, nextpose = d
            nextloc1 = (loc1[0]+dloc1[0], loc1[1]+dloc1[1])
            nextloc2 = (loc2[0]+dloc2[0], loc2[1]+dloc2[1])
            r += dfs((nextloc1, nextloc2, nextpose), table, goal, dp)    
    else:
        for d in [((1, 1), (0, 1), 0), ((1, 1), (1, 0), 1), ((1, 1), (1, 1), 2)]:
            dloc1, dloc2, nextpose = d
            nextloc1 = (loc1[0]+dloc1[0], loc1[1]+dloc1[1])
            nextloc2 = (loc2[0]+dloc2[0], loc2[1]+dloc2[1])
            r += dfs((nextloc1, nextloc2, nextpose), table, goal, dp)    
    dp[state] = r
    return r

def sol(n, table):
    dp = {}
    goal = [n-1, n-1]
    return dfs(((0, 0), (0, 1), 0), table, goal, dp)
    
n = int(stdin.readline().strip())
table = []
for i in range(n):
    table.append(list(map(int, stdin.readline().strip().split(" "))))

print(sol(n, table))