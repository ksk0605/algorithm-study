from collections import deque
import heapq

def heappush(heap, data):
    heap.append(data)
    # 추가한 원소의 인덱스를 구한다.
    current = len(heap) - 1
    # 현재 원소가 루트(인덱스 0)에 도달하면 종료
    while current > 0:
        # 추가한 원소의 부모 인덱스를 구한다.
        parent = (current - 1) // 2
        if abs(heap[parent]) > abs(heap[current]):
            heap[parent], heap[current] = heap[current], heap[parent]
            # 추가한 원소의 인덱스를 갱신한다.
            current = parent
        elif abs(heap[parent]) == abs(heap[current]) and heap[parent] > heap[current]:
            heap[parent], heap[current] = heap[current], heap[parent]
            # 추가한 원소의 인덱스를 갱신한다.
            current = parent   
        else:
            break

# def heappop(heap):
#     if not heap:
#         return "Empty Heap!"
#     elif len(heap) == 1:
#         return heap.pop()

#     pop_data, heap[0] = heap[0], heap.pop()
#     current, child = 0, 1
#     while child < len(heap):
#         sibling = child + 1
#         if sibling < len(heap) and abs(heap[child]) > abs(heap[sibling]):
#             child = sibling

#         if abs(heap[current]) > abs(heap[child]):
#             heap[current], heap[child] = heap[child], heap[current]
#             current = child
#             child = current * 2 + 1
#         elif abs(heap[current]) == abs(heap[child]) and heap[current] == heap[child]:
#         else:
#             break
#     return pop_data

    

heap = []
result = []
import sys 
n = int(sys.stdin.readline())
for i in range(n): 
    print(heap)
    input = int(sys.stdin.readline())
    if input == 0: 
        if heap: 
            # print(heap.popleft())
            # result.append(heap.popleft())
            result.append(heapq.heappop(heap))
        else: 
            # print('0')
            result.append(0)
    else: 
        heappush(heap, input)
print()
for num in result: 
    print(num)