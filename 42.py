#method oop 2 jam

class User:
    
    totalUser = 0
    
    def __init__(self, x, y, z):
        self.name = x 
        self.email = y 
        self.role = z
        
        User.totalUser +=1
    
    def infoUser(self):
        return f"{self.name} - {self.email} - {self.role}"

aliif = User("aliif", "aliif@mail.com", "admin")
zelda = User("zelda", "zelda@mail.com", "user")

print(User.totalUser)
print(aliif.infoUser())
