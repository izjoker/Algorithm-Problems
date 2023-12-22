
# 문제

# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.
# 입력

# 첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.
# 출력

# 첫째 줄에 정답 정사각형의 크기를 출력한다.

from sys import stdin
def search(square_size, numbers):
    base_idxs = [0, 0]
    offset = square_size - 1
    while True:
        if base_idxs[0]+offset >= len(numbers):
            return False
        elif base_idxs[1]+offset < len(numbers[0]): 
            left_top = numbers[base_idxs[0]][base_idxs[1]]
            right_top = numbers[base_idxs[0]][base_idxs[1]+offset]
            left_btm = numbers[base_idxs[0]+offset][base_idxs[1]]
            right_btm = numbers[base_idxs[0]+offset][base_idxs[1]+offset]
            if left_top == right_top == left_btm == right_btm:
                return True
            base_idxs[1] += 1
        else:
            base_idxs[0] += 1
            base_idxs[1] = 0
            

def sol(n, m, numbers):
    square_size = min(n, m)
    while square_size > 0:
        if search(square_size, numbers):
            return square_size**2
        square_size -= 1
    return False

n, m = map(int, stdin.readline().split(" "))
numbers = []
for i in range(n):
    numbers.append(stdin.readline().strip())

print(sol(n, m, numbers))