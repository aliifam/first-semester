'''
#binary search biasa pake while loop
def binary_search(list_n, n):
    lower = 0
    higher = len(list_n) - 1
    
    while lower <= higher:
        middle = (lower + higher) // 2
        guess_n = list_n[middle]
        if guess_n == n:
            return middle
        if guess_n > n:
            higher = middle - 1
        else:
            lower = middle + 1
    return None
    

list_n = list(map(int, input().split()))
list_n.sort()
n = int(input())
print(binary_search(list_n, n))'''



#binary search dengan recursive
def bs_recursive(list_n, lower, higher, n):
    while lower <= higher:
        middle = (lower+higher)//2
        guess_n = list_n[middle]
        if guess_n == n:
            return middle
        if guess_n > n:
            return bs_recursive(list_n, lower, middle - 1, n)
        else:
            return bs_recursive(list_n, middle + 1, higher, n)

print(bs_recursive([1,3,5,7,9], 0, len([1,3,5,7,9])-1, 7))


