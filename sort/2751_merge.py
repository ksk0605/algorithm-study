import sys 

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 왼쪽과 오른쪽 부분 배열을 재귀적으로 정렬
        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        # 두 개의 부분 배열을 합병
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 남은 원소들을 복사
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


n = int(sys.stdin.readline())
l = []
for _ in range(n): 
    l.append(int(sys.stdin.readline()))
merge_sort(l)

for num in l:
    print(num)