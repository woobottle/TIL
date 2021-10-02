class Animal:
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    print(self.name + ' cannot speak.')

  def move(self):
    print(self.name + ' cannot move.')

class Dog(Animal):
  def move(self):
    print(self.name + ' moves like a jagger.')

class Retriever(Dog):
  def speak(self):
    print(self.name + ' is smart enough to speak.')

dog = Dog('Nancy')
dog.speak()
dog.move()

super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()