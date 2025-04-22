"""
3 1 
3 2 6 
5 5 6 
16

2 1  

4 3 3 3 
4 6 6 3

19

주어진 반복수만큼 
지금 리스트에서 가장 작은 숫자 두개 찾아서 
합친걸로 그 두개 업데이트

횟수는 m은 최대 15000
n은 최대 1000
m번 반복 
가장 작은 숫자 두개 찾는거 n번
"""
from sys import stdin as s 
import heapq

n,m = map(int, s.readline().split())
N = list(map(int, s.readline().split()))

def solution(l: list, n: int)-> int : 
    for _ in range(n): 
        curlist = [i for i in l]
        heapq.heapify(curlist)
        first = heapq.heappop(curlist)
        least = heapq.heappop(curlist)
        s = first + least
        l[l.index(first)] = s
        l[l.index(least)] = s

    return sum(l)

print(solution(N, m))