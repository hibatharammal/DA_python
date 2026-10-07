# cubes = {a:a**3 for a in range(1,21)}
# print(cubes)

# a="i am eating an apple"
# a={i:a.count(i) for i in a if i in "aeiou"}
# print (a)

# a="my name is hiba"
# a={i:i[::-1] for i in a.split()}
# print (a)

# t=[("apple",10), ("banana",4),("milk",None),("orange",7)]
# t={i:j for i,j in t if j != None }
# print (t)

# a= {"apple":100,"banana":50,"organe":60}
# a= {i:j-(j*10/100) for i,j in a.items()}
# print (a)

# a= {"apple":100,"banana":50,"organe":60,"avacado":150}
# a= {i:j for i,j in a.items() if i[0]in "aeiou"}
# print(a.keys())

# a=["apple","banana","orange","grape"]

# n=[5,-3,0,7,-1]
# n={i:"positive" if i>0 else "negative" if i<0 else "zero" for i in n }
# print (n)

# a= "hello hiba hai hello hai"
# a= {i:a.split().count(i) for i in a.split()}
# print (a)

# d={"a":1,"b":2,"c":1,"d":2,"e":3}
# d={v:k for k, v in reversed(d.items())}
# print (d)

# n=[2,3,4,5,6,7]
# n= {i:True if i>1 and all(i%j!=0 for j in range(2,i)) else False for i in n}
# print (n)

# a=["apple","banana","apple","orange","banana","apple"]
# a={i:a.count(i) for i in a}
# print (a)

# d={i:"even" if i%2==0 else "odd" for i in range(1,31)}
# print (d)

# a=["a","b","c"]
# b=[10,20,30]
# c= if len(a)==len(b): {i:j for i,j in zip(a,b)} else {}
# print (c)

marks ={
    "hiba":75,
    "fida":32,
    "diya":60,
    "ziya":40
}
a= {i:"pass" if j>=40 else "Fail" for i,j in marks.items()}
print (a)