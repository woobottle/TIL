def hash_func(key):
    return ord(key[0]) % 10

class HashTable:
    def __init__(self):
        self.table = [None]*10

    def set(self, key, value):
        self.table[hash_func(key)] = value

    def get(self, key):
        return self.table[hash_func(key)]

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

class ChainedHashTable(HashTable):
    def set(self, key, value) :
      row = super().get(key)
      node = Node(key, value)
      if row != None :
        isNewKey = True
        
        for prev in row :
          if prev.key == node.key :
            prev.data = node.data
            isNewKey = False
            
        if isNewKey:
          row[-1].next = node
          row.append(node)
          super().set(key, row)
      else :
        super().set(key, [node])

    def get(self, key) :
      row = super().get(key)
      for node in row :
        if node.key == key :
          return node.data
        else :
          next


# Test code

ht = ChainedHashTable()
ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)

print(ht.get('hello'), end=' ') 
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
print()

ht.set('hello2', 5)

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
