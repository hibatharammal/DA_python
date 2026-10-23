# class Student:
#     def __init__(self,name,age,mark):
#         self.name=name
#         self.age=age
#         self.mark=mark
#     def update_mark(self,new_mark):
#         self.mark=new_mark
#     def display_details(self):
#         print(self.name)
#         print(self.age)
#         print(self.mark)
# obj=Student("hiba",25,90)
# obj.update_mark(94)
# obj.display_details()

# class BankAccount:
#     def __init__(self,amount):
#         self.amount= amount
#     def deposit(self,deposit_amount):
#         if deposit_amount>0:
#             self.amount = self.amount+ deposit_amount
#             print("Deposit successful")
#         else:
#             print("Invalid deposit amount")
            
#     def withdraw(self,withdraw_amount):
#         if withdraw_amount <= 0:
#             print("Invalid withdraw amount")
#         elif withdraw_amount> self.amount:
#             print("insufficient balance")
#         else:
#             self.amount =self.amount - withdraw_amount
#             print("withdrawal successful")
#     def check_balance(self):
#         return self.amount
        
# obj=BankAccount(10000)
# obj.deposit(5000)
# print("Balance: ",obj.check_balance())
# obj.withdraw(2000)
# print("Balance: ",obj.check_balance())

# class Car: 
#     def __init__ (self,brand,model,mileage):
#         self.brand= brand
#         self.model= model
#         self.mileage= mileage
#     def update_mileage(self,new_mileage):
#         self.mileage = new_mileage
#         return new_mileage
#     def display_details(self):
#         print("Brand: ",self.brand)
#         print("Model: ",self.model)
#         print("Mileage: ",self.mileage)
# obj=Car("Toyota","corolla",15000)
# obj.display_details()
# obj.update_mileage(20000)
# obj.display_details()

# class Animal:
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("boww")
# obj=Dog()
# obj.sound()

# class Rectangle:
#     def __init__ (self,length,width):
#         self.length= length
#         self.width= width
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2*(self.length + self.width)
# obj=Rectangle(5,4)
# print("Area: ",obj.area())
# print("Perimeter: ",obj.perimeter())

# class Print:
#     def print_document(self):
#         print("Printing Document")
# class Scanner:
#     def scan_document(self):
#         print("Scanning Document")
# class Machine(Print,Scanner):
#     pass
# obj=Machine()
# obj.scan_document()
# obj.print_document()

# class Employee:
#     def __init__(self,basic,bonus,deduction):
#         self.basic=basic
#         self.bouns=bonus
#         self.deduction= deduction
#     def salary(self):
#         return self.basic+self.bouns-self.deduction
# obj=Employee(5000,500,200)
# print("salary: ",obj.salary())

# class Book:
#     def __init__ (self,name):
#         self.name= name
#         self.borrowed = False
# class Library():
#     def __init__(self):
#         self.books=[]
#     def add_book(self,book):
#         self.books.append(book)
#     def borrow_book(self,name):
#         for book in self.books:
#             if book.name==name and not book.borrowed:
#                 book.borrowed = True
#                 print("Book borrowed")
#                 return
#         print("Book Not Available")
#     def return_book(self,name):
#         for book in self.books:
#             if book.name== name and book.borrowed:
#                 book.borrowed = False
#                 print("Book returned")
#                 return
#         print("Cannot return book")
# lib= Library()
# b1 = Book("Python")
# b2 = Book("SQL")
# lib.add_book(b1)
# lib.add_book(b2)
# lib.borrow_book("Python")
# lib.return_book("Python")

# class Temperature:
#     def __init__ (self,n):
#         self.n=n
#     def cels_to_fara(self):
#         return (self.n*9/5)+ 32
#     def fera_to_cels(self):
#         return (self.n-32)*5/9
# c=Temperature(25)
# print("Fahrenheit: ",c.cels_to_fara())
# f=Temperature(77)
# print("Celsius: ",f.fera_to_cels())

# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius= radius
#     def area(self):
#         return 3.14*self.radius**2
# class Square(Shape):
#     def __init__(self,side):
#         self.side= side 
#     def area(self):
#         return self.side**2
# c=Circle(5)
# print("Area of Circle= ",c.area())
# s=Square(4)
# print("Area of Square= ",s.area())

# class Queue:
#     def __init__(self):
#         self.item =[]
#     def enqueue(self,item):
#         self.item.append(item)
#         return
#     def dequeue(self):
#         if self.item:
#             return self.item.pop(0)
#         else:
#             return "Queue is Empty"
# obj=Queue()
# obj.enqueue(10)
# obj.enqueue(20)
# obj.enqueue(30)
# obj.enqueue(50)
# print(obj.item)
# obj.dequeue()
# obj.enqueue(40)
# print(obj.item)

# class Product:
#     def __init__(self,name,price,discount):
#         self.name=name
#         self.price=price
#         self.discount=discount 
#     def calculate_discount(self):
#         discount_amount= self.price*self.discount/100
#         final_price = self.price - discount_amount
#         return final_price
# obj=Product("laptop",2000,10)
# print("Discount price: ",obj.calculate_discount())

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")
# class Bike(Vehicle):
#     def start(self):
#         print("Bike is starting")
# obj1=Vehicle()
# obj2=Bike()
# obj1.start()
# obj2.start()

# class Calculator:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x + other.x
# obj1=Calculator(10)
# obj2=Calculator(20)
# print(obj1+obj2)

# class InvalidAgeError(Exception):
#     pass
# def validate_age(age):
#     if age < 18:
#         raise InvalidAgeError("Age must be 18 or above")
#     else:
#         print("Age is valid")
# try:
#     age=20
#     validate_age(age)
# except InvalidAgeError as e:
#     print("Invalid age: ",e)     

# class School:
#     def __init__(self):
#         self.students=[]
#     def add_student(self,name,mark):
#         self.students.append((name,mark))
#     def display_topper(self):
#         topper=max(self.students,key=lambda student:student[1])
#         print("Topper: ",topper[0])
#         print("Marks: ",topper[1])
# school= School()
# school.add_student("Hiba", 90)
# school.add_student("Fida", 75)
# school.add_student("Diya", 95)
# school.display_topper()

# import time
# class Timer:
#     def __init__

# class Playlist:
#     def __init__(self):
#         self.songs=[]
#     def add_song(self,song):
#         self.songs.append(song)
#     def remove_song(self,song):
#         if song in self.songs:
#             self.songs.remove(song)
#         else:
#             print("Song Not Found")
#     def display_songs(self):
#         print(self.songs)
# obj=Playlist()
# obj.add_song("perfect")
# obj.add_song("shape of you")
# obj.add_song("believer")
# obj.display_songs()
# obj.remove_song("believer")
# obj.display_songs()

# class Polygon:
#     def __init__(self,*args):
#         self.sides=args
#     def display_sides(self):
#         print("sides: ",self.sides)
#         print("Number of sides: ",len(self.sides))
# obj=Polygon(10,20,30)
# obj.display_sides()

# class UserAuthentication:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#     def login(self, username, password):
#         if self.username == username and self.password == password:
#             print("Login successful")
#         else:
#             print("Invalid username or password")
# obj = UserAuthentication("hiba", "1234")
# obj.login("hiba", "1234")
# obj.login("hiba", "5678")

# class NumberSeries:
#     def __init__(self, num):
#         self.num= num
#     def __iter__(self):
#         return iter(self.num)
# obj = NumberSeries([10, 20, 30, 40, 50])
# for num in obj:
#     print(num)

# class History:
#     def __init__(self):
#         self.operations= []
#     def add_operation(self, operation):
#         self.operations.append(operation)
#     def display_history(self):
#         print(self.operations)
# obj = History()
# obj.add_operation("Login")
# obj.add_operation("Open file")
# obj.add_operation("Logout")
# obj.display_history()

# class Mailbox:
#     def __init__(self):
#         self.mails = []
#     def add_mail(self,mail):
#         self.mails.append(mail)
#     def delete_mail(self,mail):
#         self.mails.remove(mail)
# obj = Mailbox()
# obj.add_mail("Hello")
# obj.add_mail("Welcome")
# print(obj.mails)
# obj.delete_mail("Hello")
# print(obj.mails)

# import copy
# class Student:
#     def __init__(self,name,marks):
#         self.name= name
#         self.marks= marks
# obj1 = Student("Hiba", [80, 90, 95])
# obj2 = copy.deepcopy(obj1)
# obj2.marks.append(100)
# print(obj1.marks)
# print(obj2.marks)

# class Order:
#     def __init__(self,price):
#         self.price=price
#     def calculate_tax(self):
#         return self.price * 0.05
#     def calculate_gst(self):
#         return self.price * 0.05
#     def total_bill(self):
#         return self.price + self.calculate_tax() + self.calculate_gst()
# obj = Order(1000)
# print("Tax:", obj.calculate_tax())
# print("GST:", obj.calculate_gst())
# print("Total bill:", obj.total_bill())

