import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = [];

    def is_empty(self):
        return len(self.queue) == 0

    def put(self, data):
        heapq.heappush(self.queue, data)

    def get(self):
        if len(self.queue) != 0 :
          return heapq.heappop(self.queue)
        return None        

    def peek(self):
        if self.queue[0] : 
          return self.queue[0]
        return None

pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
