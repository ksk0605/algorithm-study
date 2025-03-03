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

line = [0 for _ in range(100002)]
visited = [False for _ in range(100002)]

import sys
from collections import deque 
n,k = map(int, sys.stdin.readline().split())

def bfs():
    visited[n] = True
    line[n] = 0 
    dq = deque([n])
    while dq: 
        curlo = dq.popleft()
        if curlo * 2 <= 100001 and not visited[curlo * 2]: 
            visited[curlo * 2] = True
            line[curlo * 2] = line[curlo]
            dq.appendleft(curlo * 2) # 0-1 bfs
        
        if curlo - 1 >= 0 and not visited[curlo - 1]: 
            visited[curlo - 1] = True
            line[curlo - 1] = line[curlo] + 1
            dq.append(curlo - 1)
        if curlo + 1 <= 100001 and not visited[curlo + 1]: 
            visited[curlo + 1] = True
            line[curlo + 1] = line[curlo] + 1
            dq.append(curlo + 1)

bfs()

print(line[k])