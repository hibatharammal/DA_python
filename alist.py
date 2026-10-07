#____ASSIGNMENT____ 

# a=[i*i for i in range(1,101)]
# print (a)

# a="WelcomE to IndiA" 
# a=[char for char in a if char.isupper()]
# print (a)

# a=[[1,2],[3,4]]
# a=[i for n in a for i in n]
# print(a)

# a=[1,2,3,4,5,6,7,8,9]
# a=[i**2 if(i%2==0) else i for i in a]
# print (a)

# a=[i**3 for i in range(1,20) if (i%3==0)]
# print(a)

# a="i am eating a banana"
# a=[i for i in a.split() if(i[0] in "aeiou")]
# print(a)

# a=["my","name","is","hiba"]
# a=[i[::-1] for i in a]
# print(a)

# a=[1,2,None,3,4,None,None,6,7]
# a=[0 if i==None else i for i in a]
# print(a)

# a=[1,"hello",2.5,3,5,True,"hai",8]
# a=[i for i in a i ==char]

# a=[1,2,3]
# b=["a","b","c"]
# c=[(i,j)for i in a for j in b]
# print (c)

# matrix =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# diagonal= [matrix[i][i]for i in range(3)]
# print (diagonal)

# n =[1,2,3,4,5]
# n=[i*10+j for i in n for j in n]
# print (n)

# ids =[101,102,103]
# names = ["hiba","fasil","keyaan"]
# d =[{"id":i,"name":n} for i,n in zip(ids, names)]
# print (d)

# t=[35,20,30,40,15]
# t=["Hot" if i>=30 else "cold" for i in t]
# print (t)

a=[10,"hello",20,40,"hai"]
a=[str for i in a if i==int]
print (a)