# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

from sys import stdin

def sol(n, m, a, b):
    identified = {}
    for person in a:
        identified[person] = True
    cnt = 0    
    r = []
    for person in b:
        if person in identified:
            cnt += 1
            r.append(person)
    r.sort()
    return "\n".join([str(cnt)] + r)

n, m = map(int, stdin.readline().strip().split(" "))
a = []
for i in range(n):
    a.append(stdin.readline().strip())
b = []
for i in range(n):
    b.append(stdin.readline().strip())
print(sol(n, m, a, b))