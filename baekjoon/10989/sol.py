
# 문제

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 입력

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
# 출력

# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

def countsort(lst, range_):
    counter = [0]*(range_+1)
    for e in lst:
        counter[e] += 1
    idx = 0
    for v in range(len(counter)):
        for j in range(counter[v]):
            lst[idx] = v
            idx += 1

def sol():
    counter = [0]*(10000+1)
    n = int(input())
        
    while True:
        try:
            v = int(input())
            counter[v] += 1
        except:
            break
    for v in range(len(counter)):
        for j in range(counter[v]):
            print(v)
    
sol()

 
