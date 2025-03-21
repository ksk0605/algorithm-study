""" 
주사위 번호로 combination(n, n//2)
a 주사위 합 목록 구하기 
b 주사위 합 목록 구하기 

주어진 주사위 목록에서 nCn//2 의 조합으로 모든 주사위 선택 경우의 수를 구한다. 
0,1 -> [합,합,합,합,합...] 
0,2
0,3
1,2
1,3
2,3

각 조합 마다 주사위를 굴려서, 
나올 수 있는 모든 합을 더한다

0,1 -> [합,합,합,합,합...] 
0,2
0,3
1,2
1,3
2,3

주사위 조합별로 이기는 숫자를 구한다.

{ 
    (주사위 조합) : 이기는 수 
    ...
}

최고 많은 조합 반환
"""
from itertools import combinations, product
from bisect import bisect_left

# a의 원소보다 최초로 같거나 커지는 숫자
def bi(item: int, b: list) -> None: 
    start, end = 0, len(b)-1

    while start<= end: 
        mid = (start + end) // 2
        if item > b[mid]: 
            start = mid+1
        else : 
            end = mid-1
    return end+1


def solution(dice): 
    # 주어진 주사위 목록에서 nCn//2 의 조합으로 모든 주사위 선택 경우의 수를 구한다.  10C5 2C1 4C2 
    results = {}
    N = len(dice)
    for a_comb in combinations(range(N), N//2): 
        b_comb = [i for i in range(N) if i not in a_comb]

        # 각 조합 마다 주사위를 굴려서, 나올 수 있는 모든 합을 더한다 1 / 0,1 / 0,1,2
        A = []
        B = []
        for p in product(range(6), repeat=len(a_comb)):
            a = 0
            b = 0
            for z in zip(a_comb, p):
                a += dice[z[0]][z[1]]
            for z in zip(b_comb, p): 
                b += dice[z[0]][z[1]]
            A.append(a)
            B.append(b)
        B.sort()

        # 주사위 조합별로 이기는 숫자를 구한다.
        win = 0
        for a in A: 
            # win += bi(a, B)
            win += bisect_left(B, a)

        results[win] = a_comb
    print(results)
    key = max(results.keys())
    return list(map(lambda x:x+1, results[key]))

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]	
# dice = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
# dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]	
# dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5],[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
result = solution(dice)
print(result)