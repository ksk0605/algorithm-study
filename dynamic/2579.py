# 한번에 1,2 계단만 오를 수 있음
# 연속 3개 단 밟을 수 없음 1,2 
# 두칸연속 한칸이 더 큰지 한 띄고 두간 연속이

n = int(input()) 

stairs = [0] * 302
for i in range(1,n+1): 
    stairs[i] = int(input())
    
scores = [0] * 302
scores[1] = stairs[1]
scores[2] = scores[1] + stairs[2]
scores[3] = max(scores[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, 302):
    scores[i] = max(scores[i-2] + stairs[i] ,scores[i-3] + stairs[i-1] + stairs[i])

print(scores[n])