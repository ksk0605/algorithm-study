"""
현재 칸의 최소 수 = 1~6칸 전(뱀의 머리가 아닌) + 1 중 가장 작은 것  + 만약 사다리의 도착점이라면 사다리 출발점 포함해서. 

현재 칸이 만약 뱀 머리? 그럼 걍 넘기고 

"""
import sys

n, m = map(int, sys.stdin.readline().split())
board = [1 for _ in range(101)]

sadaris = {}
bems = {} 

for _ in range(n): 
    start, end = map(int, sys.stdin.readline().split())
    sadaris[end] = start

for _ in range(m): 
    start, end = map(int, sys.stdin.readline().split())
    bems[end] = start

for i in range(7, 101): 
    loads = []
    for j in range(1,7): 
        target = i-j 
        loads.append(board[target] + 1)

    if i in sadaris.keys(): 
        loads.append(board[sadaris[i]])
    board[i] = min(loads)

print(board[-1])

# for i in range(10): 
#     for j in range(1,11): 
#         print(board[i*10 + j], ' ', end='')
#     print()