# 단순 연결 리스트
class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        temp = self.head
        if not self.head:
            self.head = new_node
            return 
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
    def appendleft(self, value):
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
    def popleft(self):
        val = self.head.val
        self.head = self.head.next
        return val
    def pop(self):
        if not self.head:
            return None
        temp = self.head
        if temp.next == None:
            val = self.head.val
            self.head = None
            return val 

        while temp.next.next:
            temp = temp.next
        val = temp.next.val
        temp.next = None
        return val
    
    def is_empty(self):
        if self.head == None:
            return True
    
    def print_list(self):
        node = self.head
        while node:
            print(node.val, end='->')
            node = node.next
        print("None")


linked_list = LinkedList()
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.appendleft(2)
linked_list.appendleft(1)
linked_list.print_list()



linked_list.popleft() # 1 제거
linked_list.popleft() # 2 제거
linked_list.popleft() # 3 제거
linked_list.print_list() # 4 -> 5 -> 6
linked_list.popleft() # 4 제거
linked_list.popleft() # 5 제거
linked_list.popleft() # 6 제거

linked_list.print_list()