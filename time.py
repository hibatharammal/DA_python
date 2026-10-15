# from datetime import datetime
# now=datetime.now()
# print(now.time())
# print(now.date())
# print(now.month)
# print(now.year)

a={1,2,3,2,1}
print (a)
empty_set= set()
print(empty_set)
a.add(100)
a.update([101,102])
a.remove(2)
print (a)

num= frozenset({1,2,3,3,4,2})
print(num)

try:
    num.add(100)
except AttributeError as e:
    print(f"{e}")