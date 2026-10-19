# a={z:z**3 for z in range(10) if (z%2!=0)}
# print (a)

# def odd(n):
#     for i in range(7):
#         for j in range (2*i+1):
    
#             print("*",end="")
#         print ()
# odd(n=7)

# n=[-3,-1,0,2,5]
# n={i:"positive" if i>0 else "negavite" if i<0 else "zero" for i in n} 
# print (n)

a=[[1,2],[3,4],[5,6]]
n= []
for i in a:
    for j in i:
        n.append(j)
print(n)


