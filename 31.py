numbers = [0, 3, 4, -1, 2]

lucky_number = []

#with for loop
for number in numbers:
    if number % 2 == 0:
        lucky_number.append(number)
        
print(lucky_number)

#with list comprehension
lucky_numbers = [x for x in numbers if x % 2 == 0]

print(lucky_numbers)
