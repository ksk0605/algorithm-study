from sys import stdin as reader

n,m = map(int,reader.readline().split())
trees = list(map(int, reader.readline().split()))

start, end = 0, max(trees)
mid = (start + end) // 2

result = 0
while start <= end: 
    length = 0
    for tree in trees :
        if tree > mid: 
            length += tree - mid
    
    if length > m : 
        start = mid + 1
        mid = (start + end) // 2
    elif length < m : 
        end = mid - 1 
        mid = (start + end) // 2
    else : 
        result = mid
        break

    result = mid

print (result)