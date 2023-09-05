# 문제
# N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

# 먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.



# 별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

# 출력
# 첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

from sys import stdin
from copy import deepcopy as dc
            
n = int(stdin.readline().strip())
table = []
prevrows = []
for i in range(n):
    row = list(map(int, stdin.readline().strip().split(" ")))
    rows = [dc(row), dc(row)]
    if prevrows:
        for i in range(len(prevrows[0])):
            if i == 0:
                rows[0][i] += max(prevrows[0][i], prevrows[0][i+1])
                rows[1][i] += min(prevrows[1][i], prevrows[1][i+1])
            elif i == len(prevrows[0])-1:
                rows[0][i] += max(prevrows[0][i-1], prevrows[0][i])
                rows[1][i] += min(prevrows[1][i-1], prevrows[1][i])
            else:
                rows[0][i] += max(prevrows[0][i-1], prevrows[0][i], prevrows[0][i+1])
                rows[1][i] += min(prevrows[1][i-1], prevrows[1][i], prevrows[1][i+1])
    prevrows = dc(rows)
r = [max(prevrows[0]), min(prevrows[1])]
print(" ".join(map(str, r)))