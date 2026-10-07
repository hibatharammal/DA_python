# def add(a,b):
#     add= a+b
#     return add
# print (add(5,6))

# def even(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "odd"
    
# print (even(6))

# x=2
# y=3
# a=lambda x,y:0.5*x*y
# a=a(x,y)
# print (a)

# a=["apple","orange","banana"]
# n=lambda x: x[-1]
# print (n(a))

# l=[1,2,3,4]
# output=list(map(lambda x:x**3,l))
# print(output)

# l=[1,2,3,4,5,6]
# output= list(filter(lambda X:X%2!=0,l))
# print(output)

# def fact(n):
#     if n<=1:
#         return n
#     return n*fact(n-1)
# print (fact(5))

# def recurse(n):
#     if n== 5:
#         return 
#     print (n)
#     recurse(n+1)
# recurse(0)

try: x=10/2
except ZeroDivisionError:
    print ("error")
else:
    print("success")
finally:
    print("cleanup")

# class InvalidAgeError(Exception):
#     pass
# def check_age(age):
#     if age < 18:
#         raise InvalidAgeError("Age must be 18+")
# check_age(15)

# def add():
#     print ("Hello")
# add()