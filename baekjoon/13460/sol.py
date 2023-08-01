from copy import deepcopy as dc 
n, m = [int(e) for e in input().split(" ")]
map_ = []
while True:
    try:
        row = input()
        map_ += [row]
    except:
        break

def sol(n, m, map_):
    ans = 0
    map_ = [list(row) for row in map_]
    infos = getInfos(map_)    
    q = [[map_, infos, "continue", 0]]
    visitmap = {}
    
    while q:
        map_, infos, flag, cnt = q.pop(0)
        if flag == 'win':
            return cnt
        if cnt > 10:
            break
        if flag == 'lose':
            continue
        if (tuple(infos['R']), tuple(infos['B'])) in visitmap:
            continue
        for d in range(4):
            newmap = dc(map_)
            newinfos = dc(infos)
            newinfos, flag = slide(d, newmap, newinfos)
            q.append([newmap, newinfos, flag, cnt+1])
        visitmap[(tuple(infos['R']), tuple(infos['B']))] = True
    return -1

def getInfos(map_):
    r = {'O':None, 'R':None, 'B':None}
    for i, row in enumerate(map_):
        for j, ch in enumerate(row):
            if ch == "O":
                r['O'] = [i, j]
            if ch == "R":
                r['R'] = [i, j]
            if ch == "B":
                r['B'] = [i, j]
    return r

def move(d, map_, start):
    r, c = start
    ball = map_[r][c]
    nextr, nextc = [r, c]
    dic = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while True:
        if map_[nextr+dic[d][0]][nextc+dic[d][1]] == "O":
            map_[r][c] = '.'
            return [[nextr+dic[d][0], nextc+dic[d][1]], "goal"]
        if map_[nextr+dic[d][0]][nextc+dic[d][1]] in ['#', "R", "B"]:
            map_[r][c] = "."
            map_[nextr][nextc] = ball
            return [[nextr, nextc], "done"]
        nextr += dic[d][0]
        nextc += dic[d][1]

def priority(infos, d):
    dic = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    if dic[d][0] != 0:
        idx = 0
        direction = dic[d][0]
    else:
        idx = 1
        direction = dic[d][1]
    if direction*infos['R'][idx] < direction*infos['B'][idx]:
        return [infos['B'], infos['R']]
    else:
        return [infos['R'], infos['B']]

def slide(d, map_, infos):
    flags = {}
    for loc in priority(infos, d):
        ball = map_[loc[0]][loc[1]]
        nextloc, flag = move(d, map_, loc)
        r, c = nextloc
        
        infos[ball] = nextloc
        flags[ball] = flag
    if flags['B'] == 'goal':
        return [infos, 'lose']
    if flags['R'] == 'goal':
        return [infos, 'win']
    return [infos, 'continue']

print(sol(n, m, map_))
