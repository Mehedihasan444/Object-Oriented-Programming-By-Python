

user_name=["healthMin", "reliefMin", "FoodMin"]
user_password=['123health','456 relief','789food']
admin= {'imadmin':"123"}

user_info=dict(zip(user_name,user_password))
logged_in_user=None
def login(name,password):
    global logged_in_user
    if name in user_name:
        if password==user_info[name]:
            logged_in_user=name
            print("Login successful as ",name)
        else:
            print("Invalid password")
    elif name==list(admin.keys())[0] and password==admin[name]:
            logged_in_user=name
            print("Admin login successful")
    else:
        print("Invalid UserName")


def add_user(name,password):
     global logged_in_user
     if logged_in_user==list(admin.keys())[0]:
          if name not in user_name:
             user_name.append(name)
             user_info[name]=password
             print("New user", name, "added successfully")
          else:
            print("User already exists")
     else:
        print("Only admin can add new users")

login("healthMin", "123health")  # Should print "Login successful as healthMin"
login("reliefMin", "123")  # Should print "Incorrect password. Login denied."
login("imadmin", "123")  # Should print "Admin login successful"
login("FoodMin", "123")


login("imadmin", "123")  # Admin login
add_user("newUser", "newPassword")  # Should print "New user newUser added successfully"
add_user("newAdmin", "adminPass")  # Should print "New user newAdmin added successfully"


login("newUser", "newPassword")  # Should print "Login successful as newUser"
print(user_info)