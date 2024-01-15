import sys 

n,m = map(int, sys.stdin.readline().split())

numbers = []

for i in range(n): 
    numbers.append(list(map(int, sys.stdin.readline().split())))

sums = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1): 
    for j in range(1,n+1): 
        sums[i][j] = sums[i-1][j] + sums[i][j-1] + numbers[i-1][j-1] - sums[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())

    if(x1==x2 and y1 == y2): 
        print(numbers[x1-1][y1-1])
        continue
    
    # result = sums[y2][x2] - sums[y2][x1-1] - sums[y1-1][x2] + sums[y1-1][x1-1] // 순서 유의
    result = sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1]
    print(result)
