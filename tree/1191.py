import sys 

def preorder(lc, rc, cur):
    print(chr(cur+ TO_INT), end = '')
    if lc[cur] != 0: preorder(lc,rc,lc[cur])
    if rc[cur] != 0: preorder(lc,rc,rc[cur])

def inorder(lc, rc, cur):
    if lc[cur] != 0: inorder(lc,rc,lc[cur])
    print(chr(cur+ TO_INT), end = '')
    if rc[cur] != 0: inorder(lc,rc,rc[cur])
    
def postorder(lc, rc, cur):
    if lc[cur] != 0: postorder(lc,rc,lc[cur])
    if rc[cur] != 0: postorder(lc,rc,rc[cur])
    print(chr(cur+ TO_INT), end = '')

n = int(sys.stdin.readline())
TO_INT = 64
lc = [0] * (n+1)
rc = [0] * (n+1)
for _ in range(n): 
    parent, left, right = sys.stdin.readline().split()
    if left != '.':
        lc[ord(parent)-TO_INT] = ord(left)-TO_INT
    if right != '.':
        rc[ord(parent)-TO_INT] = ord(right) - TO_INT

preorder(lc,rc,1)
print()
inorder(lc,rc,1)
print()
postorder(lc,rc,1)
