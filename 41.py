#instance varible vs class variable

class User:
    
    totalUser = 0 #class Variable
    
    def __init__(self, x, y, z):
        self.name = x #instance Variable
        self.email = y 
        self.role = z 
        User.totalUser += 1

zelda = User("Zelda", "zelda@mail.com", "admin")
Aliif = User("Aliif", "Aliif@mail.com", "admin")
Rayhan = User("Rayhan", "Rayhan@mail.com", "user")

print(Aliif.name)
print(User.totalUser)
