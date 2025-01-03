class ArrayStack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        return None

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

def test_array_stack():
   stack = ArrayStack()
   print("Initial stack:", stack._items)  # []

   # Test push
   for i in range(5):
       stack.push(i)
       print(f"After push({i}):", stack._items)  # [0], [0,1], [0,1,2]...

   # Test peek/pop
   print(f"\nSize: {stack.size()}")  # 5
   print(f"Peek: {stack.peek()}")    # 4
   print(f"Pop: {stack.pop()}")      # 4
   print(f"After pop: {stack._items}")  # [0,1,2,3]

   # Test empty
   while not stack.is_empty():
       print(f"Pop: {stack.pop()}, Remaining: {stack._items}")

   # Test empty stack behavior
   print(f"\nEmpty stack pop: {stack.pop()}")     # None
   print(f"Empty stack peek: {stack.peek()}")    # None

if __name__ == "__main__":
    test_array_stack()