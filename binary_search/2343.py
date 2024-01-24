from sys import stdin as reader

def binary_search(files, target):



n,m = map(int,reader.readline().split())
files = list(map(int, reader.readline().split()))

start, end = min(files), max(files)
mid = (start + end) // 2

while start<=end: 
    

print (result)