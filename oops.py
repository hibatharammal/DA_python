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

class Parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"{self.name}")
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def display(self):
        super().display()
        print(f"{self.name}---{self.age}")
obj=Child("sneha",45)
obj.display()