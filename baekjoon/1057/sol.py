from sys import stdin
import sys
sys.setrecursionlimit(10**6)
def sol(n, num1, num2):
    def playround(round_, players):
        end = False
        next_players = [0]*(len(players)//2) if len(players) % 2 == 0 else [0]*((len(players)//2) + 1) 
        for i in range(0, len(players), 2):
            if len(players) <= i+1:
                next_players[i//2] = players[i] 
            elif players[i] == 1 and players[i+1] == 1:
                end = True
            elif players[i] == 1 or players[i+1] == 1:
                next_players[i//2] = 1
            else:
                next_players[i//2] = 0
               
        round_ += 1
        return [round_, next_players, end]
    players = [0]*(n)
    players[num1-1] = 1
    players[num2-1] = 1
    round_ = 1
    while len(players) > 1:
        nextround, players, end = playround(round_, players)
        if end:
            return round_
        round_ = nextround
    return -1

n, num1, num2 = map(int, stdin.readline().split(" "))
print(sol(n, num1, num2))