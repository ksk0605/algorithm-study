# 비용을 계산하는 방법? 
# 그리디... 안되지 
# 매 줄마다 해당 줄의 최소 값을 구한다면 
# 이중 포문 
# 0 1,2 
# 1 0,2 
# 2 0,1

n = int(input()) 

rgbs = []
for i in range(n): 
    rgbs.append(list(map(int, input().split())))

costs = [[0]*3 for _ in range(n)]
costs[0] = rgbs[0]

for i in range(1, n):     
    for j in range(3): 
        if j == 0:
            a, b = 1, 2
        elif j == 1:
            a, b = 0, 2
        elif j == 2:
            a, b = 0, 1
        costs[i][j] = min(costs[i-1][a], costs[i-1][b]) + rgbs[i][j]

print(min(costs[-1]))