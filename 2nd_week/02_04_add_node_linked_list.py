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

    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.get_node(index-1)

        next_node = prev_node.next

        prev_node.next = new_node
        new_node.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

# print(linked_list.get_node(0).data)
# print(linked_list.get_node(1).data)
# print(linked_list.get_node(2).data)

linked_list.add_node(1, 6)
linked_list.add_node(0, 90)
linked_list.print_all()
