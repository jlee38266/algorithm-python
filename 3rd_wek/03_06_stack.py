class Node:
    """연결 리스트의 노드를 표현하는 클래스입니다.

    각 노드는 데이터와 다음 노드를 가리키는 포인터를 가집니다.
    """

    def __init__(self, data):
        self.data = data  # 노드가 저장하는 실제 값
        self.next = None  # 다음 노드를 가리키는 포인터


class Stack:
    """연결 리스트를 사용하여 구현한 스택 클래스입니다.

    LIFO(Last In First Out) 원칙에 따라 동작하며,
    push, pop, peek 등의 기본적인 스택 연산을 제공합니다.
    """

    def __init__(self):
        """스택을 초기화합니다."""
        self.head = None  # 스택의 맨 위를 가리키는 포인터
        self._size = 0  # 스택의 현재 크기를 저장 (내부 변수로 표시)

    def push(self, value):
        """스택의 맨 위에 새로운 값을 추가합니다.

        Args:
            value: 스택에 추가할 값
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        """스택의 맨 위 요소를 제거하고 반환합니다.

        Returns:
            스택이 비어있지 않은 경우 맨 위 요소의 값,
            비어있는 경우 None
        """
        if self.is_empty():
            return None

        pop_value = self.head.data
        self.head = self.head.next
        self._size -= 1
        return pop_value

    def peek(self):
        """스택의 맨 위 요소를 제거하지 않고 반환합니다.

        Returns:
            스택이 비어있지 않은 경우 맨 위 요소의 값,
            비어있는 경우 None
        """
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        """스택이 비어있는지 확인합니다.

        Returns:
            스택이 비어있으면 True, 그렇지 않으면 False
        """
        return self.head is None

    def get_size(self):
        """스택의 현재 크기를 반환합니다.

        Returns:
            스택에 들어있는 요소의 개수
        """
        return self._size

    def __str__(self):
        """스택의 내용을 문자열로 표현합니다.

        Returns:
            스택의 요소들을 화살표로 연결한 문자열 표현
        """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return '[' + ' -> '.join(elements) + ']'

    def clear(self):
        """스택의 모든 요소를 제거합니다."""
        self.head = None
        self._size = 0


def test_stack():
    """스택의 기능을 테스트하는 함수입니다."""
    # 스택 생성 및 요소 추가 테스트
    stack = Stack()
    print("스택 초기 상태:", stack)

    # push 테스트
    for i in range(5):
        stack.push(i)
        print(f"push({i}) 후 스택:", stack)

    # pop 및 peek 테스트
    print("\n현재 스택 크기:", stack.get_size())
    print("peek 결과:", stack.peek())
    print("pop 결과:", stack.pop())
    print("pop 후 스택:", stack)

    # 스택이 빌 때까지 pop
    print("\n스택이 빌 때까지 pop:")
    while not stack.is_empty():
        print(f"pop: {stack.pop()}, 남은 스택: {stack}")


if __name__ == "__main__":
    test_stack()