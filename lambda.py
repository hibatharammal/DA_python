# a=10
# b=6
# x= lambda a,b : abs(a-b)
# print (x(a,b))

# n=[10,20,30,40]
# a=map(lambda x:str(x),n)
# print (list(a))

# b=3
# h=6
# area = lambda b,h: 0.5*b*h
# print (area(b,h))

# n=[12,15,25,31,45,50,65]
# a= filter(lambda x: x%10==5,n)
# print (list(a))

# s= "mango"
# a= lambda i:"a" in i
# print (a(s))

# a=2
# b=3
# c=4
# mul=lambda a,b,c: a*b*c
# print (mul(a,b,c))

# a= ["madam","hello","level","python","radar"]
# palin = filter (lambda x :x[::-1]==x,a)
# print (list(palin))

# a=[1,2,3,4,5,6]
# n= map(lambda i:i+10,a)
# print (list(n))

# a= 25
# x= lambda i:i>=10 and i<=50
# print (x(a))

# a=["hello","python","hiba"]
# n= map(lambda i :i.upper(),a)
# print (list(n))

# a=["hello","python","hiba"]
# n= map(lambda i :i.capitalize(),a)
# print (list(n))

# a=[2,3,4,5,6,7,8,9,10]
# prime = filter(lambda x:all(x%i!=0 for i in range(2,x)),a)
# print (list(prime))

a=[10,20,30,40]
n= map(lambda x: "$"+str(x),a)
print (list(n))