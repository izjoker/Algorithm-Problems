from sys import stdin
def sol(signal):
    def signalCheck(state, value):
        if state == "S":
            return "A" if value == 0 else "B"
        elif state == "A":
            return False if value == 0 else "S"
        elif state == "B":
            return "C" if value == 0 else False
        elif state == "C":
            return "D" if value == 0 else False
        elif state == "D":
            return "D" if value == 0 else "E"
        elif state == "E":
            return "A" if value == 0 else "X"
        elif state == "X":
            return "Y" if value == 0 else "X"
        elif state == "Y":
            return "D" if value == 0 else "S"
        else:
            raise "Invalid State"
    state = "S"
    for ch in signal:
        nextState = signalCheck(state, int(ch))
        if not nextState:
            return "NO"
        state = nextState
    if state != "S" and state != "X" and state != "E":
        return "NO"
    return "YES"

t = int(stdin.readline().strip())

for i in range(t):
    signal = stdin.readline().strip()
    print(sol(signal))