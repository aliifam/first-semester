item = int(input())

def simple_search(list, item):

    counter = 0
    
    while counter != len(list):
        if list[counter] == item:
            return counter
            
        counter += 1
        
        if item not in list:
            return None
            
my_list = [1, 3, 5, 7, 9]
print(simple_search(my_list, item), "It's index element location in the list")
   


