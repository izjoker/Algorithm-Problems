# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

import sys
sys.setrecursionlimit(10**6)
def dfs(table, loc, visit):
    x, y = loc
    if not 0 <= x < len(table) or not 0 <= y < len(table[0]) or table[x][y] == 0:
        return 0
    if visit[x][y]:
        return 0
    r = 0
    r += 1
    visit[x][y] = True
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
        nextloc = (x+d[0], y+d[1])
        r += dfs(table, nextloc, visit)
    return r

def sol(n, table):
    ans_lst = []
    
    visit = [[False]*(n) for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                localans = dfs(table, (i, j), visit)
                if localans != 0:
                    ans_lst.append(localans)
    return str(len(ans_lst)) + "\n" + "\n".join(map(str, sorted(ans_lst)))
                
args = []
while True:
    try:
        args += [input()]
    except:
        break
n = int(args[0])

table = [[int(e) for e in list(line)] for line in args[1:]]

print(sol(n, table))