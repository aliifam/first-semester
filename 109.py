#palindrome in python

def is_palindrome(words):
    palindrome = False
    words = words.lower()
    reverse_list = []
    akhir = len(words)-1
    
    for i in range(akhir, -1, -1):
        reverse_list.append(words[i])
        
    terbalik = "".join(reverse_list)
    
    if terbalik == words:
        palindrome = True
    
    return palindrome

print(is_palindrome("aba"))
