def is_sosu(n): 
    for i in range(2, int(n**0.5)+1): 
        if n % i == 0: 
            return False
    return True

import sys 

n = int(sys.stdin.readline()) 
print(str(n)[::-1])
while True: 
    if n == 1: # 1 고려하자
        n+=1
        continue
    if str(n) == str(n)[::-1]:
        if is_sosu(n): 
            print(n)
            break
    n+=1