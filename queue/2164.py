from collections import deque
import sys 

dq = deque([(i+1) for i in range(int(sys.stdin.readline()))])

trash = True
while True: 
    if len(dq) == 1: 
        break

    if trash: 
        dq.popleft()
    else: 
        trashed = dq.popleft()
        dq.append(trashed)
    
    trash = not trash

print(dq.pop())