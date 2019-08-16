class Node:
    def __init__(self, data):
                 self.data = data  
                 self.next = None   
class LinkedList: 
    def __init__(self):  
        self.head = Non
    def ins_beg(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data) 
        new_node.next = prev_node.next
        prev_node.next = new_node
    def ins_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head 
        while (last.next): 
            last = last.next 
            last.next =new_node
            
