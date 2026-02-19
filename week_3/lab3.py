"""
G1 team4 Lab 3
-Se Nita
-Hong Limhak
-Van Sovannvireak
"""
#Interation
#Write a for loop that prints each element in the list numbers = [1, 2, 3, 4, 5].


list1 = [1,2,3,4,5]

for item in list1:
    print(item,end=" ")

#Create a while loop that counts from 1 to 10 and prints the numbers. Use break to exit the loop when the count reaches 6.

i = 0
while i < 10:
    if i == 6:
        break
    print(i,end=" ")
    i += 1
#Modify the previous while loop to use continue to skip printing the number 4
i = 0
while i < 10:
    if i == 4:
        i += 1
        continue
    print(i,end=" ")
    i += 1

#list
#Create a list of your favorite fruits and print it.
list_of_fruits = ["apple","banana","mango","guava"]
print(list_of_fruits)
#Add a new fruit to the list using the append method and print the updated list.
list_of_fruits.append("orange")
print(list_of_fruits)
#Remove a fruit from the list using the remove method and print the updated list.
list_of_fruits.remove("apple")
print(list_of_fruits)
#Sort the list in alphabetical order and print it. (we using bubble sort)
for i in range(len(list_of_fruits)):
    for j in range (0 , len(list_of_fruits)-i-1):
        if list_of_fruits[j]> list_of_fruits[j+1]:
            temp = list_of_fruits[j]             
            list_of_fruits[j] = list_of_fruits[j+1] 
            list_of_fruits[j+1] = temp         
print(list_of_fruits)




#tuple
#Create a tuple containing five integers and print it.
tupless = (1,2,3,4,5)
print(tupless)

#Attempt to change one of the integers in the tuple and check your result in the terminal
#tupless[0] = 10  (this should raise an error).

#Convert the tuple into a list and print the list
listess = list(tupless)
print(listess)

#dictionary

# Create a dictionary to store the ages of three people (e.g., {"Alice": 30, "Bob": 25,"Charlie": 35}) and print it.
dictionary = {"alice":30,"bob":25,"charlie":35}
print(dictionary)
#Add a new person to the dictionary and print the updated dictionary.
dictionary["david"] = 28
print(dictionary)
# Remove one person from the dictionary using the pop method and print the updated dictionary.
dictionary.pop("alice")
print(dictionary)
#Print all keys and values in the dictionary using a loop.
for key, value in dictionary.items():
    print(f"{key}: {value}")

#function 

#Write a function named add that takes two numbers as arguments and returns their sum.
#Call the function and print the result.
def add (a,b):
    return a + b
print(add(3,5))


# Create a function named greet that prints "Hello, World!" without returning a value. Call the function.
def greet():
    print("hello world")

#Write a lambda function that takes one argument and returns the square of the number.
#Use this lambda function to print the square of 5.
result = lambda n : n**2
print(result(5))

#bonus

username =[]
users = {}
"""
1. Register:
a. Create a function that registers a user.
b. Ensure the username doesn’t already exist by checking the list of usernames.
c. Validate the password for strength based on the criteria above.
d. Store the username in a list and the username-password pair in a dictionary.
"""
def register ():
    name = input("enter username to register: ")
    if name in username:
        print("Username already exist")
        return
    while True:
        password = input("enter password: ")
        if pass_validate(password):
            users[name] = password
            username.append(name)
            print("registration successful")
            break
        else:
            print("password is weak try again ")
            continue


"""
2. Login:
a. Create a function to allow users to log in with their username and password.
b. Validate the credentials against the stored username-password pairs.
c. Allow users up to three login attempts before blocking further attempts.
"""
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


"""
3. Forgot Password:
a. Create a function to retrieve a password when the user provides a valid username.
b. If the username doesn’t exist, notify the user.
"""
def forgot_password():
    forgot_username = input("Enter your username to retrieve your password: ")
    if forgot_username not in username:
        print ("username not found")
        return
    print (f"Your password is:{users[forgot_username]}") #we can directly access the password using the username as key

"""
4. Menu:
a. Implement a menu that allows users to choose between registering, logging in, or
recovering their password.
b. Ensure users can exit the program.
"""
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
"""
5. Password Strength Validation:
a. Use a function to validate if the password meets the specified strength requirements.
b. Provide feedback to users on why a password is considered weak and how to
improve it.
"""              
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