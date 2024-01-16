from collections import deque 
import sys 

n = int(sys.stdin.readline())


numbers = deque([(i+1) for i in range(n)])

sequence = deque([])
dq = deque([0])

for i in range(n): 
    sequence.append(int(sys.stdin.readline()))

result = []
success = True
while sequence: 
    if sequence[0] > dq[-1]: 
        result.append('+')
        dq.append(numbers.popleft())
    elif sequence[0] < dq[-1]: 
        if not numbers:
            success = False
            break
        dq.append(numbers.popleft())
    else:
        result.append('-')
        dq.pop()
        sequence.popleft()

if success: 
    for i in range(len(result)):
        print(result[i])
else: 
    print('NO')