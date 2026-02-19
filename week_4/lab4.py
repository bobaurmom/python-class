
#ex1-2
#Create a class called Car with the attributes: make, model, and year.
class Car :
    make = "Toyota"
    model = "Corola"
    year = 2020
    #Modify the Car class to include a constructor
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    #Add a method is_vintage() that returns True if the car is older than 25 years and False otherwise.
    def is_vintage(self):
        vintage = lambda year : (2025 - year) > 25
        if vintage(self.year):
            print("it old")  
        else:
            print("not vintage")
    #Add a method display_info() that prints the car's details
    def display_info (self):
        print("make:",Car.make)
        print("model:",Car.model)
        print("year:",Car.year)
#- Create an object from the Car class and display its information.
car_detail = Car("toyota","corola",2020)
car_detail.display_info()

#Create two objects, one vintage and one non-vintage, and call the is_vintage() method on each.
car1 = Car("toyota","corola",1990)
car2 = Car("toyota","corola",2025)
car1.is_vintage()
car2.is_vintage()

#ex3
#- Create a class called Student with attributes: name, age, and grade.
class Student:
    name= "John"
    age=20
    grade="B"
#- Add a method update_grade(new_grade) that changes the student's grade.
    def update_grade(self,new_grade):
        self.grade = new_grade

#- Create an object, update its grade, and print the updated information.
student1 = Student()
student1.update_grade("A")
print(student1.grade)


#ex4
#- Create a class called BankAccount with attributes: owner and balance.
class BankAccount:
    owner = "John"
    balance = 0
    #- Add methods deposit(amount) and withdraw(amount), where the withdraw() method checks if there are sufficient funds before subtracting.
    def deposit(self,amount):
        self.balance += amount
        print("depositing:",amount)
        print("new balance:",self.balance)

        
    def withdraw(self,amount):
        enough = lambda amount , balance : balance - amount <=0
        if enough (self.balance,amount):
            self.balance -= amount
            print("withdrawing:",amount)
            print("new balance:",self.balance)
        else:
            print("not enough cash on acc")
            print(" balance is:",self.balance)
            print(" withdrawing amount is:",amount)



#Create an object, perform some deposits and withdrawals, and print the resulting balacne

h1 = BankAccount()
h1.deposit(100)
h1.withdraw(50)


#5
#Create two classes: Book with attributes title, author, and price, and Library with an
#attribute books (a list of Book objects).

class Book:
    def __init__(self,title,author,price):
        self.title =title
        self.author = author
        self.price = price
    
class Library:
    def __init__(self):
        self.books=[]
    #- Add a method add_book(book) in Library to add Book objects to the library.
    def add_book(self,book):
        self.books.append(book)
    #- Add another method show_books() that prints the details of each book in the library.
    def show_books(self):
        for book in self.books:
            print(f"Title:{book.title}Author:{book.author}Price:{book.price}")

#- Create a Library object, add several Book objects to it, and display the book list.
lib1 = Library()
book1 = Book("The Great Man", "F. Ane Fit", 10.99)
book2 = Book("The story about apt", "Fake man", 12.99)

lib1.add_book(book1)
lib1.add_book(book2)

lib1.show_books()

#ex6
#Create a class called Classroom with attributes: class_name and students (a list of
#student names).

class Classroom :

    class_name ="math 101"
    students =[]

    #Add methods add_student(name) to add a new student and list_students() to print all student name
    def add_student(self,name):
        self.students.append(name)
        print("added:",name)
    def list_students(self):
        for name in self.students :
            print(name)

#- Create an object, add some students, and list them.

c1 = Classroom()
c1.add_student("alice")
c1.add_student("bib")
c1.add_student("charlie")
c1.list_students()
        
#ex7
#Create a class called PhoneBook with an attribute contacts (a dictionary where keys are
#names and values are phone numbers).

class PhoneBook :
    contacts ={}
    #Add methods add_contact(name, number) to add a contact and find_contact(name) to
    #display a contact's number or a message if not found.
    def add_contact(self,name,number):
        self.contacts[name]=number

    def find_contact(self,name):
        for name  in self.contacts:
            print(name , self.contacts[name])
        else:
            print(f"{name} not found")
#- Create an object, add contacts, and look up a contact.
p1 = PhoneBook()
p1.add_contact("koka",123-456-789)
p1.find_contact("koka")
p1.find_contact("kok")


#ex8
#- Create a class called SportsLeague with the following attributes:
class SportLeague:
    #teams (a dictionary where keys are team names and values are lists of player
    #dictionaries; each player dictionary has keys 'id', 'name', and 'position')
    def __init__(self):
        self.team = {}

#- Implement the following methods:
    #o add_team(team_name) to add a new team.
    def add_team(self,team_name):
        self.team[team_name] = []
    #add_player(team_name, player_id, player_name, position) to add a player to a specific team
    def add_player(self,team_name,player_id,player_name,position):
        player ={"id":player_id,"name":player_name,"position":position}
        self.team[team_name].append(player)
    #view_team(team_name) to display all players on a team
    def view_team(self,team_name):
        if team_name in self.team:
            for player in self.team[team_name]:
                print(player)
    #update_player(team_name, player_id, new_name=None, new_position=None)
    #to update a player's information
    def update_player(self,team_name,player_id,new_name =None , new_position= None ):
        if team_name in self.team:
            for player in self.team[team_name]:
                if player["id"] == player_id:
                    if new_name: player['name'] = new_name
                    if new_position: player['position'] = new_position 
                return
        else:
            print("player not found")           
s1 = SportLeague()
s1.add_team("team1")
s1.add_player("team1","kiki","lola","haha")
s1.update_player("team1","kiki","lola","ha3a")
s1.view_team("team1")