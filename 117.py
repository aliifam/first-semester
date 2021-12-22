#uas ppk no. 1

temp = int(input())

n = list(map(int, input().split(" ")))

def buble_sort(the_list):
    for i in range(len(the_list)):
        for j in range (len(the_list) - 1):
            if the_list[j] >= the_list[j+1]:
                the_list[j], the_list[j+1] = the_list[j+1], the_list[j]
    return the_list

n = buble_sort(n)

n = " ".join(map(str, n))

print(n)
