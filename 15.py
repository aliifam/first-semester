#binanry searching algorithm 
item = int(input())

def binary_search(list, item): #parameter is a item want we search and list where the item located
    low = 0                    #index of first element in list
    high = len(list) - 1       #index of last element in list
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1 
        else:
            low = mid + 1 
    return None
    

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, item), "its index element location in list")


