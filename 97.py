#simple sorting algorithm python

def buble_sort(the_list):
    for i in range(len(the_list)):
        for j in range (len(the_list) - 1):
            if the_list[j] >= the_list[j+1]:
                the_list[j], the_list[j+1] = the_list[j+1], the_list[j]
    return the_list

the_list = [2,3,1,6,8,7]
print(buble_sort(the_list))

def sel_sort(the_list_2):
    pass

print(len(the_list))


