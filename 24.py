#list4jam
"""
names = ["agung", "hendarto", "maulana", "malik", "ibrahim"]

for name in names:
    print("nama :", name)

numbers = [5,6,7,8,1]
print(numbers)

numbers.append(99)
print(numbers)

numbers.insert(2, 100)  #(index parameter, value plus)
print(numbers)

numbers.pop(2) #delete by index
print(numbers)

numbers.remove(8) #delete by value
print(numbers)

numbers.sort()
print(numbers)

numbers = [5,6,7,8,1]

init_number = 0 

for number in numbers:
    init_number = init_number + number
    
print(init_number)
print(sum(numbers))

numbers = [5,6,7,8,1]

numbers.sort()

print(numbers[-1])"""

numbers = [5,6,7,8,1]

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)




