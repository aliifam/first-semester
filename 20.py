def is_leap(year):
    leap = False
    habis_dibagi_400 = year % 400 == 0 
    habis_dibagi_100 = year % 100 == 0 
    habis_dibagi_4 = year % 4 == 0
    
    if habis_dibagi_400 or (habis_dibagi_4 and not habis_dibagi_100):
        leap = True
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))
