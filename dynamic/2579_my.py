n = int(input()) 

stairs = [0] * 300
for i in range(n): 
    stairs[i] = int(input())
    
scores = [0] * 300
scores[0] = stairs[0]
scores[1] = stairs[0] + stairs[1]
scores[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
scores[3] = max(stairs[0]+stairs[1]+stairs[3], stairs[0]+ stairs[2]+ stairs[3])

for i in range(4, 300):
    a = scores[i-4] + stairs[i-2] + stairs[i]
    b = scores[i-4] + stairs[i-3] + stairs[i-1] + stairs[i]
    scores[i] = max(a,b)

print(scores[n-1])