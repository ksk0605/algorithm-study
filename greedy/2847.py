from sys import stdin as s

def solution(l: list) -> int : 
    cnt = 0
    for i in reversed(range(len(l) - 1)): 
        while l[i] >= l[i+1]: 
            l[i] -= 1
            cnt += 1
    return cnt


# 입력 
n = int(s.readline())
N = [int(s.readline()) for _ in range(n)]

print(solution(N))