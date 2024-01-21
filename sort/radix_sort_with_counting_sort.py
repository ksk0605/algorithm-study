def radix_sort(arr):
    # 가장 큰 숫자의 자릿수를 찾는다.
    max_num = max(arr)
    max_digits = len(str(max_num))

    # 각 자릿수에 대해 counting sort 수행
    for digit in range(max_digits):
        counting_sort(arr, digit)

def counting_sort(arr, digit):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 0부터 9까지의 숫자를 세기 위한 배열

    # 현재 자릿수에 따라 각 숫자의 개수를 센다.
    for i in range(n):
        index = arr[i] // (10 ** digit)
        count[index % 10] += 1

    # 누적 합을 구한다.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # output 배열에 정렬된 순서대로 원소를 배치한다.
    i = n - 1
    while i >= 0:
        index = arr[i] // (10 ** digit)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # 원래 배열을 정렬된 결과로 업데이트한다.
    for i in range(n):
        arr[i] = output[i]

# 예시
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("기수 정렬 결과:", arr)
