from sys import stdin as std

def binary_search(target, l): 
    start, end = 0, (len(l)-1)
    mid = end // 2

    while start <= end: 
        if l[mid] < target: 
            start = mid + 1
            mid = (start + end) // 2
        elif l[mid] > target: 
            end = mid - 1
            mid = (start + end) // 2
        else: 
            return True
    
    return False

n = std.readline()
nums = list(map(int, std.readline().split()))
nums.sort()
m = std.readline() 
targets = list(map(int, std.readline().split()))

for target in targets: 
    if binary_search(target, nums): 
        print(1)
    else: 
        print(0)