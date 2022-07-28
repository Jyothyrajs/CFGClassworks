# STACK


class StackList:
    """
    Stack Implementation using a List
    """

    def __init__(self,size):
        self.capacity = size
        self.container = [None] * size
        self.top = -1
        
    def push(self,element):
        if self.is_full():
            print("Stack is full.. exiting")
            exit(1)
        else:
            print("Inserting ..",element)
            self.top += 1
            self.container[self.top] = element

    def pop(self):
        """
            Remove element
            return : None

        """
        if self.is_empty():
            print("Stack empty..exiting")
            exit(1)

        print("removing ..", self.peek())

        top = self.container[self.top]
        self.top = self.top -1
        return top


    def size(self):
        return self.top + 1

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size == self.capacity

    def peek(self):
        if self.is_empty():
            print("Stack empty..exiting")
            exit(1)
        return self.container[self.top]




# Example run, but I encourage to try more examples to understand this

stack = StackList(3)

stack.push(1)
stack.push(2)

stack.pop()
stack.pop()

stack.push(3)

print("Top element is", stack.peek())
print("The stack size is", stack.size())

stack.pop()

# if stack.is_empty():
#     print("The stack is empty")
# else:
#     print("The stack is not empty")


#####################################################

"""
Stack implementation using deque class in Python
"""
from collections import deque

stack = deque()
# Run
stack.append(1)
stack.append(2)
stack.append(3)

print("top element : ",stack[-1])
stack.pop()
stack.pop()

print("Size : ",len(stack))
stack.pop()
stack.pop()

###############################################

# QUEUE


class MyQueue:
    """
    Queue Implementation using a List
    """
    def __init__(self,size):
        self.capacity = size
        self.q = [None] * size #cannot do [None,None,None,..]
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self,element):
        if self.is_full():
            print("Overflow:Queue full")
            exit(1)
        else:
            print("Inserting ", element,self.front,self.rear)
            self.rear = (self.rear + 1) % self.capacity
            self.q[self.rear] = element
            self.count += 1


    def dequeue(self):
        if(self.is_empty()):
            print("Underflow ...Queue empty")
            exit(1)
        else:
            print("Removing ..",self.q[self.front])
            ele = self.q.remove(self.q[self.front])
            print(self.front)
            self.front = (self.front + 1) % self.capacity
            self.count -= 1

    def peek(self):
        if self.is_empty():
            print("Empty.. terminating")
            exit(1)
        return self.q[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity


# Run
q = MyQueue(3)
q.enqueue(10)
q.enqueue(50)
q.enqueue(30)
# q.enqueue(40)
q.dequeue()
q.dequeue()


#####################################################


"""
Queue implementation using deque class in Python
"""
from collections import deque

q2 = deque([], maxlen = 5)

q2.append(1)
q2.append(2)
q2.append(3)

print("Front element is :",q2[0])

q2.popleft()
print("Front element is :",q2[0])

q2.popleft()
q2.popleft()
# print("Front element is :",q2[0])
# Run