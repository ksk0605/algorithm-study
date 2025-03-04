from collections import deque 
import sys 

n,m = map(int, sys.stdin.readline().split()) 

maps = [[0 for _ in range(m+2)] for _ in range(n+2)]
visited = [[False for _ in range(m+2)] for _ in range(n+2)]
dists = [[0 for _ in range(m+2)] for _ in range(n+2)]

for i in range(1, n+1): 
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(1, m+1): 
        maps[i][j] = line[j-1]

start = (0,0) 
for i in range(n): 
    for j in range(m): 
        if maps[i][j] == 2: 
            start = (i,j)

# print(start)
visited[start[0]][start[1]] = True
    
def bfs(): 
    news = [(-1,0), (1,0), (0,-1), (0,1)]
    dq = deque([start])
    while(dq): 
        cnt = dq.popleft()
        cx = cnt[0]
        cy = cnt[1]
        for v in news: 
            x = v[0] + cx 
            y = v[1] + cy
            # print(x,y)
            if not visited[x][y] and maps[x][y] != 0: 
                visited[x][y] = True
                dq.append((x,y))
                dists[x][y] = dists[cx][cy] + 1
bfs()

for i in range(1,n+1):
    for j in range(1,m+1): 
        if dists[i][j] == 0 and maps[i][j] != 0: 
            dists[i][j] = -1
dists[start[0]][start[1]] = 0

for i in range(1,n+1): 
    this = dists[i]
    print(' '.join(map(str, this[1:m+1])))