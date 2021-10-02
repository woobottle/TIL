class Median:
  def __init__(self):
    self.items = []

  def get_item(self, item):
    self.items.append(item)

  def clear(self):
    self.items = []

  def show_result(self):
    self.items = sorted(self.items)
    itemsLength = len(self.items)
    midIndex = int(itemsLength/2)
    isItemsLengthEven = itemsLength % 2 == 0
    if (isItemsLengthEven) :
      print((self.items[midIndex] + self.items[midIndex-1])/2)
    else :
      print(self.items[midIndex])

median = Median()
for x in range(10):
  median.get_item(x)
median.show_result()

median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4] :
  median.get_item(x)
median.show_result()
