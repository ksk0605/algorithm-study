def radix_sort(arr):
    # 가장 큰 숫자의 자릿수를 찾는다.
    max_num = max(arr)
    max_digits = len(str(max_num))

    # 각 자릿수에 대해 radix sort 수행
    for digit in range(max_digits):
        arr = sort(arr, digit)
    
    return arr

def sort(arr, digit):
    n = len(arr)
    output = [0] * n

    # 현재 자릿수에 따라 버킷 생성
    buckets = [[] for _ in range(10)]

    # 현재 자릿수에 따라 각 숫자를 버킷에 할당
    for i in range(n):
        index = arr[i] // (10 ** digit)
        buckets[index % 10].append(arr[i])

    # 버킷에 있는 숫자를 순서대로 output 배열에 병합
    output_index = 0
    for bucket in buckets:
        for num in bucket:
            output[output_index] = num
            output_index += 1

    return output

# 예시
arr = [170, 45, 75, 90, 802, 24, 2, 66]
arr = radix_sort(arr)
print("기수 정렬 결과:", arr)
