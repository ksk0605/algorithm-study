from sys import stdin
from collections import deque as dq

# 입력 
m, n ,h = map(int, stdin.readline().split())
box = []
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
zero_count = 0
q = dq([])
for i in range(h): 
    plate = []
    for j in range(n): 
        line = list(map(int, stdin.readline().split()))
        zero_count += line.count(0)
        for k in range(m): 
            if line[k] == 1: 
                q.append((k, j, i))
                # visited[i][j][k] = True
        plate.append(line)
    box.append(plate)

# print(visited)
# 처음부터 다 익으면?  (0 개수가 0이면) 0

# 익어있는 토마토 좌표를 모두 큐에 넣기
def bfs(): 
    dir = [(1,0,0), (-1, 0 ,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    while(q):         
        cur = q.popleft()
        cx = cur[0]
        cy = cur[1] 
        cz = cur[2]
        visited[cz][cy][cx] = True
        for d in dir: 
            nx = cx + d[0]
            ny = cy + d[1]
            nz = cz + d[2]
            if nx < 0 or ny < 0 or nx == m or ny == n or nz < 0 or nz == h: 
                continue
            if not visited[nz][ny][nx] and box[nz][ny][nx] == 0: 
                box[nz][ny][nx] = box[cz][cy][cx] + 1
                q.append((nx, ny, nz))

if zero_count == 0: 
    print(0)
    exit
else: 
    bfs()

    # 다 익었는지? (0개수가 1개라도 남아있으면) -1
    for plate in box: 
        for line in plate: 
            if line.count(0) > 0: 
                print(-1)
                exit(0)
    min = 0
    for plate in box: 
        for line in plate: 
            for item in line: 
                if item > min: 
                    min = item
    print(min -1 )