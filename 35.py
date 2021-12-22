#program tugas pertama alpro

nilai = input().split()

nilai1 = float(nilai[0])
nilai2 = float(nilai[1])
nilai3 = float(nilai[2])
nilai4 = float(nilai[3])
nilai5 = float(nilai[4])

#1
if nilai1 >= 80:
    grade1 = 4
elif nilai1 >= 70:
    grade1 = 3
elif nilai1 >= 60:
    grade1 = 2
elif nilai1 >= 50:
    grade1 = 1
elif nilai1 < 50:
    grade1 = 0

#2
if nilai2 >= 80:
    grade2 = 4
elif nilai2 >= 70:
    grade2 = 3
elif nilai2 >= 60:
    grade2 = 2
elif nilai2 >= 50:
    grade2 = 1
elif nilai2 < 50:
    grade2 = 0

#3
if nilai3 >= 80:
    grade3 = 4
elif nilai3 >= 70:
    grade3 = 3
elif nilai3 >= 60:
    grade3 = 2
elif nilai3 >= 50:
    grade3 = 1
elif nilai3 < 50:
    grade3 = 0
    
#4
if nilai4 >= 80:
    grade4 = 4
elif nilai4 >= 70:
    grade4 = 3
elif nilai4 >= 60:
    grade4 = 2
elif nilai4 >= 50:
    grade4 = 1
elif nilai4 < 50:
    grade4 = 0

#5
if nilai5 >= 80:
    grade5 = 4
elif nilai5 >= 70:
    grade5 = 3
elif nilai5 >= 60:
    grade5 = 2
elif nilai5 >= 50:
    grade5 = 1
elif nilai5 < 50:
    grade5 = 0
    
totalgpa = grade1 + grade2 + grade3 + grade4 + grade5
gpa = totalgpa / 5 

if gpa >= 2.75:
    print(format(gpa, '.2f'))
    print("PASSED")
else:
    print(format(gpa, '.2f'))
    print("FAILED")
