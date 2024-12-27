def find_pair_sum(arr, target):
    """
    정렬된 배열에서 합이 target이 되는 두 수를 찾는 함수

    Args:
        arr (list): 오름차순으로 정렬된 정수 배열
        target (int): 찾고자 하는 합의 목표값

    Returns:
        tuple: 합이 target이 되는 두 수의 쌍 (없으면 None)

    Raises:
        ValueError: 배열이 정렬되어 있지 않은 경우
        ValueError: 배열의 길이가 2보다 작은 경우
    """
    # 입력값 검증
    if len(arr) < 2:
        raise ValueError("배열의 길이는 2 이상이어야 합니다.")

    # 정렬 여부 확인
    if not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        raise ValueError("배열이 정렬되어 있지 않습니다.")
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(find_pair_sum(sorted_array, 21))  # (6, 15) 출력

