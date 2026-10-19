# class Rectangle:
#     def __init__(self,length,breadth):
#             self.length= length
#             self.breadth= breadth
#     def area(self):
#         return self.length * self.breadth
# r=Rectangle(5,4)
# print(r.area())

# class A:
#     def hello(self):
#         print("A")
# class B(A):
#     def hai(self):
#         print("B")
# class C(B):
#     pass
# obj=C()
# obj.hello()
# obj.hai()

# class A:
#     def greet(self):
#         print("Hello from A")
# class B:
#     def greet(self):
#         print("Hello from B")
# class C(A,B):
#     pass
# obj = C()
# obj.greet()
# print(C.__mro__)

# class Even:
#     def __init__ (self,number):
#         self.number= number
#     def Odd(self):
#         if self.number %2==0:
#             return ("even")
#         else:
#             return ("odd")
# even= Even(6)
# print(even.Odd())

# class Parent:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"{self.name}")
# class Child(Parent):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def display(self):
#         super().display()
#         print(f"{self.name}---{self.age}")
# obj=Child("sneha",45)
# obj.display()

# class Bank:
#     def __init__(self,name,dept,salary):
#         self.name=name
#         self._dept=dept
#         self.__salary=salary
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self,amount):
#         if amount>0:
#             self.__salary=amount 
# b=Bank("sneha","HR",50000)
# print(b.name)
# print(b._dept)
# # print(b.__salary)
# print(b.get_salary())
# print(b._Bank__salary)
# b.set_salary(55000)
# print(b.get_salary())

# from abc import ABC,abstractmethod 
# class Shape(ABC):
#     @abstractmethod 
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         return 0.5*self.base*self.height
# c=Circle(5)
# print(c.area())
# t=Triangle(8,6)
# print(t.area())

# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
# calc = Calculator()
# print(calc.add(10,20,30))
# print(calc.add(10,20))

# class Calculator:
#     def add(self,*args):
#         return sum(args)
# calc = Calculator()
# print(calc.add(2,3))
# print(calc.add(1,2,3,4))
    
# class Audio:
#     def play(self):
#         print("audio")
# class Video:
#     def play(self):
#         print("video")
# def play_media(media):
#     media.play()
# audio=Audio()
# video=Video()
# play_media(audio)
# play_media(video)

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        if isinstance(other,Vector):
            return Vector(self.x+other.x,self.y+other.y)
        return NotImplemented
    def __str__(self):
        return f"Vector({self.x},{self.y})"
v1=Vector(2,4)
v2=Vector(1,3)
v3=v1+v2
print(v3)