def merge(left, right):
    """두 개의 정렬된 배열을 하나의 정렬된 배열로 병합합니다.

    이 함수는 merge sort의 가장 기본이 되는 연산을 수행합니다.
    두 정렬된 배열을 받아서 이들을 정렬된 상태로 병합합니다.

    Args:
        left: 정렬된 첫 번째 배열
        right: 정렬된 두 번째 배열

    Returns:
        두 배열의 모든 원소가 정렬된 상태로 병합된 새로운 배열
    """
    merged = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged


def merge_sort(array):
    """하나의 배열을 정렬하는 기본적인 merge sort를 수행합니다.

    배열을 재귀적으로 분할하고 병합하면서 정렬을 수행합니다.
    이는 merge sort의 가장 기본적인 형태입니다.

    Args:
        array: 정렬할 배열

    Returns:
        정렬된 새로운 배열
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge_sort_two_arrays(array1, array2):
    """두 개의 정렬되지 않은 배열을 받아서 하나의 정렬된 배열로 만듭니다.

    이는 merge sort의 첫 번째 확장으로, 두 개의 독립된 배열을 처리합니다.
    각 배열을 개별적으로 정렬한 후 병합합니다.

    Args:
        array1: 첫 번째 정렬되지 않은 배열
        array2: 두 번째 정렬되지 않은 배열

    Returns:
        두 배열의 모든 원소가 정렬된 상태로 병합된 새로운 배열
    """
    sorted_array1 = merge_sort(array1)
    sorted_array2 = merge_sort(array2)
    return merge(sorted_array1, sorted_array2)


def merge_sort_multiple_arrays(*arrays):
    """임의의 개수의 정렬되지 않은 배열들을 하나의 정렬된 배열로 만듭니다.

    이는 merge sort의 가장 일반화된 형태로, 임의의 개수의 배열을 처리할 수 있습니다.
    각 배열을 개별적으로 정렬한 후, 순차적으로 병합해 나갑니다.

    Args:
        *arrays: 정렬할 배열들 (가변 인자)

    Returns:
        모든 배열의 원소가 정렬된 상태로 병합된 새로운 배열
    """
    if not arrays:
        return []

    sorted_arrays = [merge_sort(array) for array in arrays]
    result = sorted_arrays[0]

    for i in range(1, len(sorted_arrays)):
        result = merge(result, sorted_arrays[i])

    return result


def main():
    """함수들의 사용 예시를 보여주는 메인 함수입니다."""
    # 기본 merge sort 테스트
    single_array = [5, 2, 8, 1, 9, 3]
    print(f"단일 배열 정렬 테스트:")
    print(f"입력: {single_array}")
    print(f"출력: {merge_sort(single_array)}\n")

    # 두 배열 정렬 테스트
    array1 = [5, 2, 8]
    array2 = [1, 6, 3]
    print(f"두 배열 정렬 테스트:")
    print(f"입력: {array1}, {array2}")
    print(f"출력: {merge_sort_two_arrays(array1, array2)}\n")

    # 여러 배열 정렬 테스트
    array3 = [7, 4, 9, 30, 15, -1]
    print(f"세 배열 정렬 테스트:")
    print(f"입력: {array1}, {array2}, {array3}")
    print(f"출력: {merge_sort_multiple_arrays(array1, array2, array3)}")


if __name__ == "__main__":
    main()