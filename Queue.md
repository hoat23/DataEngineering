## Queue Data Structure in Python

Queue is a linear data structure, that follows the FIFO (First In First Out) principe. Therefore, the first element that will be inserted in que queue would be the first element that will be removed from it.

Operations
- Enqueue(element): Add a new element to the end of the queue.
- Dequeue: Remove the first element from the front of the queue.
- isEmpty: Check if the queue if empty (returns True) or not (returns False).
- Peek: Get the first element of the queue, without removing it.

### Simple Queue

#### Implementation of Queue Using Python List

see below:
```python
class Queue():
    def __init__(self):
        self.queue = []


    '''Returns False if the queue has at least one element (length of list > 0). 
    Otherwise returns True (length of list == 0) '''
    def is_empty(self):
        return not len(self.queue)

    
    '''Adds an element to the end of the list (queue)'''
    def enqueue(self, element):
        self.queue.append(element)
        return self.queue


    '''Firstly checks if the queue is empty. If the queue does not empty, removes 
    the first element of the list (queue). Otherwise, it returns a warning message'''
    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue.pop(0)

    
    '''Return the value of the front of the queue without removing it. 
    If queue is empty return a warning message'''
    def peek(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue[0]
```
Implementing a queue using Python List hampers the performance of the system since we use a lot of data. The deletion of an element at the beginning of the list requires all the other elements to shift left by one, which requires O(n) time. This is what adversely affects the performance.

Example:

```python
my_queue = Queue()

my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")
print(f"Queue first element: {my_queue.peek()}")
# Queue first element: a

print(f"The element '{my_queue.dequeue()}' removed from the Queue")
# The element 'a' removed from the Queue

print(f"Queue first element: {my_queue.peek()}")
# Queue first element: b
```

### Simple Linked List

Refer to the code given below:

```python
''' Node class represents a node of the list '''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

'''' LnkedList class represents the linked list '''
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    

    ''' Check if the list (queue) is empty so returns True (self.head is None) 
    or not so returns False (self.head is not None) '''
    def is_empty(self):
        return not self.head


    '''Add a new node to the end of the linked list (queue)'''
    def enqueue(self, new_node):
        if self.is_empty():
           self.head = new_node
           self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    
    ''' Remove the first node of the linked list (queue).
    If the linked list (queue) is empty returns a warning message '''
    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        deleted_element = self.head.value
        self.head = self.head.next
        return deleted_element

    
    ''' Return the first node of the linked list. 
    If the linked list (queue) is empty returns a warning message'''
    def peek(self):
        if self.is_empty():
            return  "Warning: The queue is empty"
        return self.head.value
```

Example:
```python
my_queue = LinkedList()

my_queue.enqueue(Node("a"))
my_queue.enqueue(Node("b"))
my_queue.enqueue(Node("c"))

print(f"Queue first element: {my_queue.peek()}")
# Queue first element: a

print(f"The element '{my_queue.dequeue()}' removed from the Queue")
# The element 'a' removed from the Queue

print(f"Queue first element: {my_queue.peek()}")
# Queue first element: b
```

## Queue using the Deque Module

Deque (double-ended-queue) is a specific object in the collections module that you can use for linked lists. In the following example, we will enqueue new elements using the ```append(element)``` method and we will dequeue elements using the ```popleft()``` method

```python
from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()


    ''' Return False if the queue has at list one element (len of queue > 0), 
    otherwise returns True (len of queue = 0) '''
    def is_empty(self):
        return not len(self.queue)


    ''' Add element to the end of the queue '''
    def enqueue(self, element):
        self.queue.append(element)
        return self.queue


    ''' Remove the element from the end of the queue.
    If the queue is empty returns a warning message'''
    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue.popleft()
        

    ''' Return the value of the element on the front of the queue without removing it.
    If the queue is empty returns a warning message '''
    def peek(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue[0]
```

Example:
```python
my_queue = Queue()

my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")

print(f"Queue first element: {my_queue.peek()}")
# Queue first element: a

print(f"The element '{my_queue.dequeue()}' removed from the Queue")
# The element 'a' removed from the Queue

print(f"Queue first element: {my_queue.peek()}")
# Queue first element: b
```

Reference:
- https://python.plainenglish.io/queue-data-strucure-theory-and-python-implementation-e58f3582c390
