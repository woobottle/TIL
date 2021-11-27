def fifo(records) :
    queue = []
    total = 0
    for record in records :
        type, price, number = record.split()
        number = int(number)
        price = int(price)
        if type == 'P' :
            while number != 0 :
                queue.append(price)
                number -= 1
        else :
            while number != 0 :
                temp = queue.pop(0)
                total += temp
                number -= 1
    return total

def lifo(records) :
    stack = []
    total = 0
    for record in records:
        type, price, number = record.split()
        number = int(number)
        price = int(price)
        if type == 'P':
            while number != 0:
                stack.append(price)
                number -= 1
        else:
            while number != 0:
                temp = stack.pop()
                total += temp
                number -= 1
    return total

def solution(records):
    answer = []
    answer.append(fifo(records))
    answer.append(lifo(records))
    return answer


print(solution(["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"])) # [1500, 2400]
print(solution(["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"])) # [1800, 2700]
print(solution(["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"])) #[7100, 10700]
