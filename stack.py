class stack:
    def __init__(self):
        self.stack=[]
    def add (self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False#add is not used here
    def peek():
        return self.stack[-1]
    def push(self,data):
        self.stack.append(data)
        return self.stack
    def remove(self):
        if len(self.stack)<=0:
            return 'no element'
        else:
            return self.stack.pop()
    def print(self):
        print( self.stack)
s=stack()
s.push(4)
s.push(5)
s.push(6)
s.print()

#another method
def push(elmnt):
    stack.append(elmnt)
    
def pop():
    if len(stack)!=0:
        x=stack.pop()
        print("Element poped was ",x)
    else:
        print("stack is empty")
    
def display():
    print("===========================================")
    print("Elements are ", stack, "Stack length",len(stack))
    print("===========================================")
    

print("Stack implementation in Python using List")
stack=[]
ch=0
while(ch!=3):
    print("1. Push 2. Pop 3. Exit\nEnter your choice")
    y=input()
    if y.isdigit():
        ch=int(y)
        
        if ch==1:
            elemnt=int(input("Enter a value to push into stack"))
            push(elemnt)
            display()
        elif ch==2:
            pop()
            display()
        elif ch==3:
            break
        else:
            print("Invalid choice")
    
    else:
        print("Invalid-Not a number")
