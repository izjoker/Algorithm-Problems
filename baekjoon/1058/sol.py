from sys import stdin
def sol(f_flags):
    ans = 0
    for row, line in enumerate(f_flags):
        friends = {}
        for col, ch in enumerate(line):
            if ch == "Y":
                friends[col] = True
                for idx, ch_ in enumerate(f_flags[col]):
                    if ch_ == "Y" and idx != row:
                        friends[idx] = True
        ans = max(ans, len(list(friends)))
    return ans

n = int(stdin.readline().strip())
f_flags = []
for i in range(n):
    line = stdin.readline().strip()
    f_flags.append(line)

print(sol(f_flags))

