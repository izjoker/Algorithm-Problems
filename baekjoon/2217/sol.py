from sys import stdin
def sol(n, caps):
    caps.sort(reverse=True)
    cands = []
    for i in range(len(caps)):
        maxWeight = caps[i] * (i+1)
        cands.append(maxWeight)

    return max(cands)
n = int(stdin.readline().strip())
caps = []
for i in range(n):
    caps.append(int(stdin.readline().strip()))
    
print(sol(n, caps))