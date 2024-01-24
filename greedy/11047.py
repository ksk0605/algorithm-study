from sys import stdin 

n,k = map(int,stdin.readline().split())

coins = [] 
for i in range(n): 
    coins.append(int(stdin.readline()))

cnt = 0
for coin in reversed(coins):
    if k>=coin: 
        cnt += k//coin
        k -= (k // coin) * coin
    if k == 0: 
        break

print(cnt)