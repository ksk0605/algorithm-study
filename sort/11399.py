import sys
n = int(sys.stdin.readline())
l = list(map(int , sys.stdin.readline().split()))
l.sort(reverse=True)
result = 0
for i,num in enumerate(l,1): 
    result += i*num
print(result)