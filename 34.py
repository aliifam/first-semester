days = int(input())

if days >= 365:
    years = days // 365
    months = (days - years*365) // 30
    weeks = (days - years*365 - months*30) // 7
    day = (days - years*365 - months*30 - weeks*7)
else:
    years = 0
    months = days // 30
    weeks = (days - months*30) // 7
    day = (days - months*30 - weeks*7)

print( days, "days equals", years, "year", months, "month", weeks, "week", day, "day")
    
    
    
    
