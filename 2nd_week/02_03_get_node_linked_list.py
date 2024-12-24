class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# node = Node(3)
# print(node.data, node.next)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

#  Linkedlist의 가장 끝에 있는 노드에 새로운 노드를 연결시킨다.
    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.append(35)
# linked_list.print_all()

print(linked_list.get_node(0).data)
print(linked_list.get_node(1).data)
print(linked_list.get_node(2).data)
print(linked_list.get_node(3).data)