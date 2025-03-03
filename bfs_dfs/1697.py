""" 
5 7
5 10 9 18 17

1 3 
1 2 3

각 위치에서 선택할 수 있는 경우의 수 
-1 
+1 
* 2
"""

line = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]

import sys
from collections import deque 
n,k = map(int, sys.stdin.readline().split())

def bfs():
    visited[n] = True
    line[n] = 0 
    dq = deque([n])
    while dq: 
        curlo = dq.popleft()
        if curlo + 1 <= 100000 and not visited[curlo + 1]: 
            visited[curlo + 1] = True
            line[curlo + 1] = line[curlo] + 1
            dq.append(curlo + 1)
        if curlo - 1 >= 0 and not visited[curlo - 1]: 
            visited[curlo - 1] = True
            line[curlo - 1] = line[curlo] + 1
            dq.append(curlo - 1)
        if curlo * 2 <= 100000 and not visited[curlo * 2]: 
            visited[curlo * 2] = True
            line[curlo * 2] = line[curlo] + 1
            dq.append(curlo * 2)
        

bfs()

print(line[k])
print(line[:100])