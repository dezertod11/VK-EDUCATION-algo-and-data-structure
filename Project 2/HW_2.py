class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def setvalue(self, value):
        self.value = value

    def getvalue(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None

    def sethead(self, new_head):
        self.head = new_head

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

    def append_back(self, new_node):
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

def merge_sorted_linked_list(list1, list2):
    cur1 = list1.head
    cur2 = list2.head
    merge_list = LinkedList()

    if cur1.value <= cur2.value:
        merge_list.sethead(cur1)
        last = cur1
        cur1 = cur1.next
    else:
        merge_list.sethead(cur2)
        last = cur2
        cur2 = cur2.next

    while (cur1 != None) and (cur2 != None):
        if cur1.value <= cur2.value:
            last.next = cur1
            last = cur1
            cur1 = cur1.next
        else:
            last.next = cur2
            last = cur2
            cur2 = cur2.next

    if (cur1 != None):
        last.next = cur1

    if (cur2 != None):
        last.next = cur2

    return merge_list

# linked_list1 = LinkedList()
# list1 = [i for i in range(1, 11, 2)]
# for i in list1[::-1]:
#     linked_list1.append_front(i)
# print("linked_list1:")
# linked_list1.print_list()
#
# linked_list2 = LinkedList()
# list2 = [i for i in range(6, 16, 2)]
# for i in list2[::-1]:
#     linked_list2.append_front(i)
# print("\nlinked_list2:")
# linked_list2.print_list()
#
# merge_linked_list = merge_sorted_linked_list(linked_list1, linked_list2)
# print("\nmerged_linked_list:")
# merge_linked_list.print_list()



