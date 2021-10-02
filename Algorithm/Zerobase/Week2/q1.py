class Foo:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print('I am ' + self.name)

class Bar(Foo):
  def __init__(self, name):
    super().__init__(name)
  
  def speak(self):
    print('Yout are ' + self.name)

bar = Bar('John')
bar.speak()