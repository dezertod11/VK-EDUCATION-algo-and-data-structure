class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def set(self, value):
        self.value = value

    def get(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None

    def append_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def append_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while (cur_node != None):
            print(cur_node.value, '->', sep = '', end = '')
            cur_node = cur_node.next
        print("None")

    def reverse_linked_list(self):
        prev = None
        cur = self.head

        while (cur != None):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev


# linked_list = LinkedList()
# list = [i for i in range(1, 11)]
# for i in list[::-1]:
#     linked_list.append_front(i)
#
#
# linked_list.print_list()
# print(linked_list.reverse_linked_list())
# linked_list.print_list()