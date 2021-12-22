#contructoroop

class User:
    def __init__(self, x, y, z):
        self.name = x
        self.email = y
        self.role = z

zelda = User("zelda", "zelda@mial.com", "Admin")
link = User("link", "link@mail.com", "user")

print(zelda.name)
print(zelda.email)
print(zelda.role)

print(link.name)
