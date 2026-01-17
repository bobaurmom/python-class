#exercise 1


def arithmetic(a,b):
    print("sum=",a+b)
    print("difference=",a-b)
    print("product=",a*b)
    print("Quotion=",a/b)
    
num1 = int(input ("enter 1s number:"))
num2 = int(input ("enter 2ns number:"))

arithmetic(num1,num2)

#exercise 2


def compareNum (a,b,c):

    
    if (a>b and a>c):
        print(f"max value is ",a)
    elif (b>a and b>c):
        print(f"max value is",b)
    else:
        print(f"max value is ",c)

a =int(input("Enter 1st number:"))
b =int(input("Enter 2nd number:"))
c =int(input("Enter 3rd number:"))

compareNum(a,b,c)

#exercise 3

for i in range (1,101):
    if (i%3==0 and i%5==0):
        print("FizzBuzz")
    elif (i%3 == 0):
        print("fizz")
    elif (i%5 == 0):
        print("buzz")
    else:
        print(i)

#exercise 4
def facto (x):
    sum = 1
    while x > 1:
        sum = sum * x
        x = x - 1
    return sum

x = int(input("Enter a number for factorial:"))
print(facto(x))

#exercise 5

def palidrome (string):

    half = len(string)//2

    string1= string[:half] #i slice it from 0 -> half
    string2= string[:-half-1:-1] #i slice and reverse the 2nd half so from -1 (the end) and stop before half

    for i in range (half):
        if(string1[i]!=string2[i]):
            print("This is not a palidrome")
            return
        else:
            is_palidrome= True
    if (is_palidrome):
        print("It is a palidrome")

string = input("Enter a word:")

palidrome(string)


#exercise bonus



def validator (password):
    
    if (len(password)<8):
        print("Weak ahh password")
        return
    
    has_num = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if (has_num and has_lower and has_upper and has_special):
        print("This password is Strong")

    else:
        print("password moderate")



password = input ("Enter your password:")

validator(password)

