class Queue:
  def __init__(self) :
    self.main = []
    self.temp = []

  def isEmpty(self, array):
    return len(array) == 0

  def enqueue(self, value) :
    self.main.append(value)
  
  def dequeue(self) :
    if self.isEmpty(self.temp) :
      while self.main :
        self.temp.append(self.main.pop())
    return self.temp.pop()

    # while self.main :
    #   self.temp.append(self.main.pop())

    # value = self.temp.pop()

    # while self.temp :
    #   self.main.append(self.temp.pop())

    # return value

a = Queue()
a.enqueue(3)
print(a.dequeue()) # 3
a.enqueue(5)
print(a.dequeue()) # 5
a.enqueue(4)
a.enqueue(5)
print(a.dequeue()) # 4
a.enqueue(6)
print(a.dequeue()) # 5
print(a.dequeue()) # 6
print(a.main)

