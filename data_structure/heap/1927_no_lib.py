class Heap: 
    def __init__(self):
        self.hq = []

    def add(self, num): 
        self.hq.append(num)
        self.__up()

    def pop(self): 
        if len(self.hq) == 0: 
            return 0
        
        num = self.hq[0]
        self.hq[0] = self.hq[-1]
        self.hq.pop()
        self.__down()
        return num

    def __up(self) -> None:
        curr = len(self.hq) - 1

        while self.__parent(curr) >= 0 and self.hq[self.__parent(curr)] > self.hq[curr]: 
            self.hq[self.__parent(curr)], self.hq[curr] = self.hq[curr], self.hq[self.__parent(curr)]
            curr = self.__parent(curr)

    def __down(self) -> None: 
        curr = 0 

        last = len(self.hq) - 1

        leftchild = self.__left_child(curr)
        rightchild = self.__right_child(curr)
        
        while leftchild <= last: 
            if rightchild <= last: 
                if self.hq[leftchild] >= self.hq[curr] and self.hq[rightchild] >= self.hq[curr]: 
                    break

                if self.hq[leftchild] < self.hq[rightchild]: 
                    self.hq[leftchild], self.hq[curr] = self.hq[curr], self.hq[leftchild]
                    curr = leftchild
                    leftchild = self.__left_child(curr)
                    rightchild = self.__right_child(curr)
                else: 
                    self.hq[rightchild], self.hq[curr] = self.hq[curr], self.hq[rightchild]
                    curr = rightchild
                    leftchild = self.__left_child(curr)
                    rightchild = self.__right_child(curr)
                continue
            else: 
                if self.hq[leftchild] >= self.hq[curr]: 
                    break
                else:
                    self.hq[leftchild], self.hq[curr] = self.hq[curr], self.hq[leftchild]
                    curr = leftchild
                    leftchild = self.__left_child(curr)
                    rightchild = self.__right_child(curr)


        
    def __parent(self, child) -> int: 
        return (child - 1) // 2
    
    def __left_child(self, parent) -> int: 
        return parent * 2 + 1
    
    def __right_child(self, parent) -> int: 
        return parent * 2 + 2

"""
        0
   1          2
 3   4     5     6 
7 8 9 10 11 12 13 14

확인할 수 있는 자식이 있을때 
왼쪽 오른쪽 자식이 둘다 있으면 
하나씩 확인하고 더 작은 쪽이랑 바꿈 

왼쪽 자식만 있으면 
더 작으면 바꿈 

자식 없으면 그만두고 
둘다 자기보다 크면 그만 두고
"""


import sys 

n = int(sys.stdin.readline())
h = Heap()

for _ in range(n): 
    num = int(sys.stdin.readline())

    if num == 0: 
        print(h.pop())
    else: 
        h.add(num)