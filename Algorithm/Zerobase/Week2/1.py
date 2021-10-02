import csv

f = open('a.csv', 'r', encoding="utf-8-sig")
reader = csv.reader(f)
listOfReader = list(reader)
answer = sum(list(map(lambda x: int(x), listOfReader[0])))
print(answer)