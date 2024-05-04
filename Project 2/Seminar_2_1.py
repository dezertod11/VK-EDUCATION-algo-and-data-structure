class Node:
    def __init__(self, value = None):
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

    def make_cycle(self, value):
        if self.head == None:
            print("list is empty")
            return
        slow = self.head
        fast = self.head.next
        while (fast.next != None):
            if (slow.value != value):
                slow = slow.next
            fast = fast.next
        fast.next = slow

    def cycle_or_not(self):

        if self.head == None or self.head.next == None:
            return False

        slow = self.head
        fast = self.head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

# linked_list = LinkedList()
# list = [i for i in range(1, 6)]
# for i in list[::-1]:
#     linked_list.append_front(i)
#
# linked_list.print_list() # print initial list
# print(linked_list.cycle_or_not()) # check whether linked_list is cycle or not
# linked_list.make_cycle(3) # making linked_list cyclic
# print(linked_list.cycle_or_not()) # check whether linked_list is cycle or not
# #linked_list.print_list() # print cycle linked_list :)))))



