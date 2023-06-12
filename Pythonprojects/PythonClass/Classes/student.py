# cration of a class
class Studentss:
    name="Rachel"
    age="21"
    school:"AkiraChix"
    nationality:"Kenyan"


# methods and attributes
class Student:
    school:"AkiraChix"
    def __init__(self,name,age,nationality):#used to initialize the attributes of an object 
        self.name=name
        self.age=age
        self.nationality=nationality
    def greet_student(self):
        return f"Hello{self.name}, welcome to {self.school}"#f-strings are those containing expressions that will be replaced with their values.
    def year_of_birth(self):
        year=2023-self.age
        return f"Hello {self.name}, you were born in {year}"
    
# Define a class Rectangle with attributes width and height, and methods area() and perimeter().
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        add=self.width+self.height
        return add*2

# Define a subclass Square that inherits from the Rectangle class and has an additional size attribute.
#  Override the area() and perimeter() methods to work with the size attribute instead of width and height.

class Square(Rectangle):
    def __init__(self,size):#the __init__ is being overidden
        self.size= size
        super().__init__(size,size)#used to call a method from a parent class by temporarily returning object of the
        # superclass, which allows you to call its methods
    def area(self):
        return self.size**2
    def perimeter(self):
        return 4*self.size

# Define a class Person with attributes name and age, and a method greet()
#  that prints "Hello, my name is [name] and I am [age] years old.".

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old.'

        
# Define a subclass Student that inherits from the Person class and has an additional 
# attribute student_id. Override the greet() method to print "Hello, my name is [name],
#  I am [age] years old, and my student ID is [student_id]." instead.

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        return f'Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}.'


student1 = Student('Mia', 20, '19989')  
print(student1.greet())  
# Define a class BankAccount with attributes balance and owner_name, 
# and methods deposit() and withdraw() that modify the balance attribute.
class BankAccount():
    def __init__(self,balance,owner_name):
        self.balance=balance
        self.owner_name=owner_name
    def deposit(self):
        new_balance=2000
        return new_balance-self.balance
    def withdraw(self):
        new_balance=2000
        return self.balance-new_balance

  

# Define a class Bank that has a dictionary attribute accounts that maps account IDs (integers) to BankAccount objects.
#  Implement methods create_account() that creates a new BankAccount object with a unique account ID and adds it to the accounts dictionary,
#  and get_account() that retrieves a BankAccount object from the accounts dictionary by ID.

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        # Assume BankAccount class has been defined elsewhere
        new_account = BankAccount()
        while new_account.id in self.accounts:
            new_account = BankAccount()
        self.accounts[new_account.id] = new_account

    def get_account(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id]


# Define a class Employee with attributes name, department, and salary, and a method get_raise() 
# that takes a percentage increase in salary as a float and updates the salary attribute accordingly.
class Employer:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary
    def get_raise(self, raise_percentage):
        self.salary += self.salary * raise_percentage / 100
        return self.salary

emp1 = Employer("John", "Marketing", 50000)

# Call the get_raise() method on emp1
new_salary = emp1.get_raise(15)

# The new_salary variable will now hold the updated salary of emp1
print(new_salary) 
        




# Define a subclass Manager that inherits from the Employee class and has an additional attribute employees
#  that is a list of Employee objects that the manager is responsible for. 
# Implement a method get_bonus() that calculates a bonus as 5% of the sum of the salaries of all employees under the manager's supervision.


# Define a class Polygon with attribute sides that is an integer indicating the number of sides, and a method area() that raises a NotImplementedError. Define a subclass Triangle that inherits from Polygon and implements the area() method properly for a triangle with given side lengths. Define a subclass Rectangle that inherits from Polygon and implements the area() method properly for a rectangle with given length and width.
# Define a class Graph that has a dictionary attribute nodes that maps node IDs (integers) to lists of adjacent nodes (also integers). Implement a method add_node() that adds a new node to the graph with unique ID, and a method add_edge() that adds an undirected edge between two nodes identified by ID.
# Define a class EmailClient that has attributes inbox, sent, and drafts, which are lists of emails class objects. Implement methods send_email(), receive_email(), and save_draft().
