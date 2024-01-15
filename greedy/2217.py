# 1 <= n <= 100000 -> n^2 x 
# w 중량
# k 개의 로프
# 임의로 몇 개의 로프를 골라서 사용해도 된다.

# 최대 중량?
# 10 15
# 1개 15 
# 2개 10 

# 3 8 17 
# 1개 17 
# 2개 16
# 3개 9

# 20 50 66 74
# 1개 74 
# 2개 66 * 2
# 3개 50 * 3
# 4개 20 * 4

# 주어진 로프의 개수만큼 반복하면서 
# 가장 높은 무게를 버틸 수 있는 로프 부터 * 반복 횟수 
# 무게를 저장 후에 가장 큰 것 반환

# nlogN 까지만

n = int(input()) 

ropes = []
weights = []
for i in range(n): 
    ropes.append(int(input()))

ropes.sort(reverse=True) 

for i in range(n): 
    weights.append(ropes[i] * (i+1))

print(max(weights))