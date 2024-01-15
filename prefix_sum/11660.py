import sys 

n,m = map(int, sys.stdin.readline().split())

numbers = []

for i in range(n): 
    numbers.append(list(map(int, sys.stdin.readline().split())))

sums = [[0]*(n+1) for _ in range(n+1)]
print(sums)
for i in range(1, n+1): 
    for j in range(1,n+1): 
        sums[i][j] = sums[i-1][j] + sums[i][j-1] + numbers[i-1][j-1]

for i in range(n+1): 
    print(sums[i])