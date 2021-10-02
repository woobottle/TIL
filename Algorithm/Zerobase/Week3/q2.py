class Stack:
    def __init__(self):
        self.list = list()

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

class Calculator:
    def __init__(self):
        self.stack = Stack()

    def calculate(self, string):
      for el in string.split(' ') :
        if(el in ['+', '-', '*', '/']) :
          first = self.stack.pop()
          second = self.stack.pop()
          value = 0
          if (el == '+') :
            value = first + second
          elif (el == '-') :
            value = second - first
          elif (el == '*') :
            value = first * second
          elif (el == '/') :
            value = second / first
          self.stack.push(value)
        else :
          self.stack.push(int(el))
      return self.stack.pop()

# Test code
calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +')) # 14
print(calc.calculate('2 5 + 3 * 6 - 5 *')) # 75