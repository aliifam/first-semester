array = [1,2,3,4,5,6,7,8,9]



#without temporary variable
right = 0

left = len(array) - 1

while right < left:
    array[left], array[right] = array[right], array[left]
    right+=1
    left-=1

print(array)
