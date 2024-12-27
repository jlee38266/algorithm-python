import time
import random
import string
from typing import List, Set


def generate_random_menu(length=8):
    """랜덤한 메뉴 이름 생성"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# 테스트용 데이터
SMALL_MENU_COUNT = 5
SMALL_ORDER_COUNT = 3
LARGE_MENU_COUNT = 10000
LARGE_ORDER_COUNT = 100

# 작은 데이터셋
small_menus = [generate_random_menu() for _ in range(SMALL_MENU_COUNT)]
small_orders = random.sample(small_menus, SMALL_ORDER_COUNT)
small_orders_with_invalid = small_orders + [generate_random_menu()]


def search_list(menus: List[str], orders: List[str]) -> bool:
    """리스트 순차 검색을 사용한 주문 가능 여부 확인

    시간복잡도: O(n*m), 여기서 n은 orders의 길이, m은 menus의 길이
    공간복잡도: O(1), 추가 공간 필요 없음
    """
    for order in orders:
        if order not in menus:
            return False
    return True


def search_binary(menus: List[str], orders: List[str]) -> bool:
    """이진 검색을 사용한 주문 가능 여부 확인

    시간복잡도: O(m*log(m) + n*log(m)), 여기서 n은 orders의 길이, m은 menus의 길이
    공간복잡도: O(1), 정렬이 in-place로 수행된다고 가정
    """
    menus.sort()  # 이진 검색을 위한 정렬

    def binary_search(target: str, array: List[str]) -> bool:
        start = 0
        end = len(array) - 1

        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    for order in orders:
        if not binary_search(order, menus):
            return False
    return True


def search_hash(menus: List[str], orders: List[str]) -> bool:
    """해시 테이블(Set)을 사용한 주문 가능 여부 확인

    시간복잡도: O(m + n), 여기서 n은 orders의 길이, m은 menus의 길이
    공간복잡도: O(m), 메뉴 리스트를 저장할 추가 공간 필요
    """
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


def measure_time(func, menus, orders, iterations=1000):
    """함수의 실행 시간을 측정"""
    total_time = 0
    for _ in range(iterations):
        # 매 반복마다 새로운 메뉴 리스트 복사 (원본 보존)
        menus_copy = menus.copy()
        start_time = time.time()
        func(menus_copy, orders)
        end_time = time.time()
        total_time += (end_time - start_time)
    return (total_time / iterations) * 1000  # 밀리초 단위 변환


def run_performance_test(menus: List[str], orders: List[str], dataset_name: str):
    """성능 테스트 실행 및 결과 출력"""
    print(f"\n=== {dataset_name} ===")
    print(f"메뉴 개수: {len(menus)}, 주문 개수: {len(orders)}")

    # 정확성 테스트
    print("\n정확성 테스트 (유효한 주문):")
    print(f"List Search:   {search_list(menus.copy(), orders)}")
    print(f"Binary Search: {search_binary(menus.copy(), orders)}")
    print(f"Hash Search:   {search_hash(menus.copy(), orders)}")

    # 잘못된 주문 테스트
    invalid_orders = orders + [generate_random_menu()]
    print("\n정확성 테스트 (잘못된 주문):")
    print(f"List Search:   {search_list(menus.copy(), invalid_orders)}")
    print(f"Binary Search: {search_binary(menus.copy(), invalid_orders)}")
    print(f"Hash Search:   {search_hash(menus.copy(), invalid_orders)}")

    # 성능 테스트
    print("\n성능 테스트 (평균 실행 시간):")
    list_time = measure_time(search_list, menus, orders)
    binary_time = measure_time(search_binary, menus, orders)
    hash_time = measure_time(search_hash, menus, orders)

    print(f"List Search:   {list_time:.6f}ms")
    print(f"Binary Search: {binary_time:.6f}ms")
    print(f"Hash Search:   {hash_time:.6f}ms")


if __name__ == "__main__":
    # 작은 데이터셋 테스트
    run_performance_test(small_menus, small_orders, "작은 데이터셋 테스트")

    # 큰 데이터셋 테스트
    large_menus = [generate_random_menu() for _ in range(LARGE_MENU_COUNT)]
    large_orders = random.sample(large_menus, LARGE_ORDER_COUNT)
    run_performance_test(large_menus, large_orders, "큰 데이터셋 테스트")




