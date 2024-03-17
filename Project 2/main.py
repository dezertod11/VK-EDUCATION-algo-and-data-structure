class Node:
    def __init__(self, value = 0):
        self.value = value
        self.next = None

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


linked_list = LinkedList()
list = [i for i in range(1, 6)]
for i in list[::-1]:
    linked_list.append_front(i)
linked_list.print_list()
