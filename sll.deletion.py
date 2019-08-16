class Node:
    def __init__(self, data):
                 self.data = data  
                 self.next = None   
class LinkedList: 
    def __init__(self):  
        self.head = Non
     def deleteNode(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break 
            if temp is None: 
                return 
            if temp.next is None: 
                return 
        next = temp.next.next
        temp.next = None
        temp.next = next
    def removeLastNode(head):
        if head == None:
            return None
        if head.next == None: 
            head = None
            return None
        second_last = head 
        while(second_last.next.next): 
            second_last = second_last.next
            second_last.next = None
            return head 
  
  
   
            
