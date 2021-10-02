class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedQueue:
    def __init__(self):
      self.front = None
      self.rear = None

    def is_empty(self):
      return ((self.front == None) & (self.rear == None))

    def put(self, data):
      if self.front == None :
        self.front = Node(data)
      else :
        prevNode = self.front if self.rear == None else self.rear
        newRearNode = Node(data, prevNode)
        prevNode.next = newRearNode
        self.rear = newRearNode

    def get(self):
      if self.front == None :
        self.rear = None
        return None
      else :
        prevNode = self.front
        self.front = prevNode.next
        if self.front != None :
          self.front.prev = None 
        return prevNode.data

    def peek(self):
      if self.front == None :
        return None
      else : 
        return self.front.data

# Test code
queue = LinkedQueue()

print(queue.is_empty()) # true
for i in range(10):
  queue.put(i)
print(queue.is_empty()) # false

for _ in range(11):
  print(queue.get(), end=' ') # 값 출력
print()

for i in range(20):
  queue.put(i)
print(queue.is_empty()) # false

for _ in range(5):
  print(queue.peek(), end=' ') # 값 출력
print()

for _ in range(21):
  print(queue.get(), end=' ')
print()
print(queue.is_empty()) # true
