n = int(input())
A = input().split()

A  = list(set(A))

convert = [int(x) for x in A]
convert.sort(reverse=True)

print(convert[1])

