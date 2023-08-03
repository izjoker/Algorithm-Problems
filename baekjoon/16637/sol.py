# 문제
# 길이가 N인 수식이 있다. 수식은 0보다 크거나 같고, 9보다 작거나 같은 정수와 연산자(+, -, ×)로 이루어져 있다. 연산자 우선순위는 모두 동일하기 때문에, 수식을 계산할 때는 왼쪽에서부터 순서대로 계산해야 한다. 예를 들어, 3+8×7-9×2의 결과는 136이다.

# 수식에 괄호를 추가하면, 괄호 안에 들어있는 식은 먼저 계산해야 한다. 단, 괄호 안에는 연산자가 하나만 들어 있어야 한다. 예를 들어, 3+8×7-9×2에 괄호를 3+(8×7)-(9×2)와 같이 추가했으면, 식의 결과는 41이 된다. 하지만, 중첩된 괄호는 사용할 수 없다. 즉, 3+((8×7)-9)×2, 3+((8×7)-(9×2))은 모두 괄호 안에 괄호가 있기 때문에, 올바른 식이 아니다.

# 수식이 주어졌을 때, 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값을 구하는 프로그램을 작성하시오. 추가하는 괄호 개수의 제한은 없으며, 추가하지 않아도 된다.

# 입력
# 첫째 줄에 수식의 길이 N(1 ≤ N ≤ 19)가 주어진다. 둘째 줄에는 수식이 주어진다. 수식에 포함된 정수는 모두 0보다 크거나 같고, 9보다 작거나 같다. 문자열은 정수로 시작하고, 연산자와 정수가 번갈아가면서 나온다. 연산자는 +, -, * 중 하나이다. 여기서 *는 곱하기 연산을 나타내는 × 연산이다. 항상 올바른 수식만 주어지기 때문에, N은 홀수이다.

# 출력
# 첫째 줄에 괄호를 적절히 추가해서 얻을 수 있는 결과의 최댓값을 출력한다. 정답은 231보다 작고, -231보다 크다.
import random
import re
from copy import deepcopy as dc
class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

def pickOps(opsidxs, n):
    r = []
    if n == 0:
        return []
    if n == 1:
        for idx in opsidxs:
            r += [[idx]]
        return r
    for i, idx in enumerate(opsidxs):
        idxs = opsidxs[i+2:]
        r += [[idx] + e for e in pickOps(idxs, n-1)]
    return r


def eval_(formula, idxs):
    postfix = getpostfix(formula, idxs)
    treeroot = createTree(postfix)
    return evaltree(treeroot)

def evaltree(node):
    def cal(a, b, op):
        if op == "+":
            return a+b
        elif op == "-":
            return a-b
        elif op == "*":
            return a*b
    if not node.left:
        return node.v
    
    return cal(evaltree(node.left), evaltree(node.right), node.v)

def createTree(postfix):
    s = []
    for ch in postfix:
        if ch in ["**", "++", "--", "*", "+", "-"]:
            r, l = [s.pop(-1), s.pop(-1)]
            opnode = Node(ch[0])
            opnode.left = l
            opnode.right = r
            s.append(opnode)
        else:
            s.append(Node(ch))
    return s[-1]

def getpostfix(formula, idxs):
    priority = {
        "**":5,
        "++":5,
        "--":5,
        "*":3,
        "+":3,
        "-":3
    }
    parenthesisOpMap = {
        "*":"**",
        "+":"++",
        "-":"--",
    }
    s = []
    postfix = []
    for i, ch in enumerate(formula):
        if i in idxs:
            ch = parenthesisOpMap[ch]
        if ch in priority:
            while s and priority[s[-1]] >= priority[ch]:
                postfix.append(s.pop(-1))
            s.append(ch)
        else:
            postfix.append(ch)
    while s:
        postfix.append(s.pop(-1))
    return postfix

def sol(n, formula):
    formula = re.split(r"(\W)", formula)
    numbers = []
    ops = []
    cands = []
    opidxs = []
    for i, ch in enumerate(formula): 
        if ch in ["*", "+", "-"]:
            opidxs.append(i)
        if ch.isnumeric():
            formula[i] = int(ch)
    print(formula, opidxs)
    for i in range(len(formula)//4+2):
        idxs = pickOps(opidxs, i)
        for idxset in idxs:
            cands.append(eval_(formula, idxset))
    return max(cands)
args = [] 
while True:
    try:
        args += [input()]
    except:
        break
n = int(args[0])
formula = args[1:][0]
print(sol(n, formula))