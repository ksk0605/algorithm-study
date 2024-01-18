import sys 
s = sys.stdin.readline()
l = []
for i in range(len(s)-1):
    l.append(int(s[i]))
l.sort(reverse=True)
print(''.join(map(str, l)))