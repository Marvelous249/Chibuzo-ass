x = [1, 2 , 3 ,4, 5]
y = list()
print(x[1+3])

x = [1, 2 , 3 ,4, 5]
y = list("eniola")
print(y)

x = [1, 2 , 3 ,4, 5]
y = list([1, 2, 3])
print(y)

x = [1, 2 , 3 ,4, 5]
y = list([1, 2, 3])
print(y+x)

x = [1, 2 , 3 ,4, 5]
y = list([1, 2, 3])
z = []
z.extend(x)
z.extend(y)
print(z)

x = [1, 2 , 3 ,4, 5]
y = list([1, 2, 3])
z = []
z.append(x)
z.append(y)
print(z)

x = [1, 2.0, True, "ore", [2, 3]]
y = list([1, 2, 3])
z = []
z.extend(x)
z.extend(y)
print(z)

x = [1, 2.0, True, "ore", [2, 3]]
y = list([1, 2, 3])
z = []
z.extend(x)
z.extend(y)
print("eniola" not in x)

x = [1, 2.0, True, "ore", [2, 3]]
y = list([1, 2, 3])
print(id(x))

x += "janet"

print(x)
print(id(x))

a = 1
print(id(a))

a +=3

print(a)
print(id(a))

x = [1, 2.0, True, "ore", [2, 3]]
y = list([1, 2, 3])
x += "hello"
print(x)

x = [1, 2.0, True, "ore", [2, 3]]
y = list([1, 2, 3])
print(x[2:5])

x = [1, 2.0, True, "ore", [2, 3]]
y = list([1, 2, 3])
print(x[::-1])

x = [1, 2.0, True, "ore", [2, 3]]
y = list([1, 2, 3])
print(x[1::2])




