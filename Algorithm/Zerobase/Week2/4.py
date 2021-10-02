class Foo:
  bar = 'A'

  def __init__(self):
    self.bar = 'B'

  class Bar:
    bar = 'C'

    def __init__(self):
      self.bar = 'D'
  

print(Foo.bar)
print(Foo().bar)
print(Foo.Bar.bar)
print(Foo.Bar().bar)