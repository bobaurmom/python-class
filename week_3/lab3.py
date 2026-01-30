
#Interation
#exercise 1.1

list1 = [1,2,3,4,5]

for item in list1:
    print(item,end=" ")

#exercise 1.2
i = 0
while i < 10:
    if i == 6:
        break
    print(i,end=" ")
    i += 1
#exercise 1.3
i = 0
while i < 10:
    if i == 4:
        i += 1
        continue
    print(i,end=" ")
    i += 1

#list
list_of_fruits = ["apple","banana","mango","guava"]
list_of_fruits.append("orange")
print(list_of_fruits)
list_of_fruits.remove("apple")
print(list_of_fruits)
for i in range(len(list_of_fruits)):
    for j in range (0 , len(list_of_fruits)-i-1):
        if list_of_fruits[j]> list_of_fruits[j+1]:
            temp = list_of_fruits[j]             
            list_of_fruits[j] = list_of_fruits[j+1] 
            list_of_fruits[j+1] = temp         
print(list_of_fruits)




#tuple

tupless = (1,2,3,4,5)
print(tupless)
listess = list(tupless)
print(listess)

#dictionary
dictionary = {"alice":30,"bob":25,"charlie":35}
print(dictionary)
dictionary["david"] = 28
print(dictionary)
dictionary.pop("alice")
print(dictionary)
for key, value in dictionary.items():
    print(f"{key}: {value}")

#function 

def add (a,b):
    return a + b
print(add(3,5))

def greet():
    print("hello world")

result = lambda n : n**2
print(result(5))

#bonus

username =[]
users = {}

def register ():
    name = input("enter username to register: ")
    password = input("enter password: ") 
    if name in username:
        print("Username already exist")
        return
    if pass_validate(password):
        users[name] = password
        print("registration successful")
        username.append(name)
    else:
        print("password is weak try again ")
        return

def pass_validate( password):
    weak = lambda password: len(password) < 8
        
    
    has_num = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if weak(password):
        print("password too short")
        return False
    if (not has_num):
        print("password at least 1 digit")
        return False
    elif (not has_upper):
        print("password at least 1 uppercase")
        return False
    elif (not has_lower):
        print("password at least 1 lower")
        return False
    elif (not has_special):
        print ("password at least 1 special")
        return False
    else:
        return True
def login ():
    for i in range (1,4):
        name = input("enter username: ")
        password = input("enter password:")
        if name in users and users[name] == password:
            print("Login successful")
            return
        else:
            print(f"Invalid username or password you have {3-i} attempt left")
    print("timeout u imposter")
    exit()

def forgot_password():
    forgot_username = input("Enter your username to retrieve your password: ")
    if forgot_username not in username:
        print ("username not found")
        return
    for forgot_username ,password in users.items():
        
        print (f"Your password is:{password}") 

ok = True
while ok == True:
    print("Menu: 1. Register 2. Login 3. Forgot Password 4. Exit")
    option = int(input("enter an option 1-4: "))
    match option:
        case 1:
            register()   
        case 2:
            login()
             
        case 3:
            forgot_password()
                 
        case 4:
            print("exiting")
            ok= False
                 
        case _:
            print("enter a valid one ")
                 
