#dictionary 

user = {
    "name" : "Aliif Arief Maulana",
    "Age" : 17,
    "location" : "bekasi",
    "is_admin" : True
}

user["username"] = "Baqeer"
user["name"] = "aliif tampan"

temp = user.get("username")


print(temp)
