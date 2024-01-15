import sys

n,m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
sums = [0] * (n+1)
sums[1] = numbers[0]
for i in range(2,n+1): 
    sums[i] = numbers[i-1] + sums[i-1]

for i in range(m):
    to, end = map(int, sys.stdin.readline().split())
    print(sums[end] - sums[to-1])