input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        # 각 패스에서 인접한 원소들을 비교합니다
        # n-i-1인 이유는 매 반복마다 마지막 i개의 원소는 이미 정렬
        for j in range(n - i - 1):
            # 현재 원소가 다음 원소보다 크다면
            if array[j] > array[j + 1]:
                # 두 원소의 위치를 교환합니다
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))