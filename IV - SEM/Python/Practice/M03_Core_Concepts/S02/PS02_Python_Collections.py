#1)Creating the list:
a = [10,20,30,40,50]
print(a)
b = list(10,20,312)
print(b)

#2)Accessing of list:
a = [10,20,30,40,50]
print(a[0])
print(a[-1])

#3)Creating list with repeated elements:
a = [10,20,30,40,50]
print(a * 2)

#4)Adding elements to a list:
a = [10,20,30,40,50]
a.append(100)
print(a)
a.insert(1,50)
print(a)

#5)Removing elements from list:
a = [10,20,30,40,50]
a.remove(40)
print(a)
a.pop()
print(a)

#6) Slicing
a = [10,20,30,40,50]
print(a[0:])
print(a[2:])
#reverse the list using slicing

#7) Leetcode problems(169,88,217)
#8) Set operation
a = set([10,20,30,40,50,])
b = set([20,30,45,40])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
