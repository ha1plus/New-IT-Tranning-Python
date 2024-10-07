#Function
print("Function")
print("Function 1")
def my_function():
  print("Hello from a function")

my_function()
print('\n')

print("Function 2")
def my_function1(fname, lname):
  print(fname + " " + lname)

my_function1("Emil", "Refsnes")
print('\n')

print("Function 3")
def my_function2(x):
  return 5 * x

print(my_function2(3))
print('\n')

print("Function 4")
def my_function3():
  return 5

print(my_function3())
print('\n')

#Variable Global and Local
print("Variable Global and Local")
print("Global")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

def myfunc1():
  global x
  x = "fantastic1"
  print("Python is " + x)

myfunc1()


print("Local")
def myfunc2():
  x = "fantastic"
  print("Python is " + x)

myfunc2()
print('\n')

#List and Tuple
print('List and Tuple')
print("List")
thislist = ["apple", "banana", "cherry"]
print(thislist)
print('\n')

print("List Append")
thislist.append("orange")
print(thislist)
print('\n')

print("List Insert")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "lemon")
print(thislist)
print('\n')

print("List Pop")
thislist.pop(1)
print(thislist)
print('\n')

print("Tuple")
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple)
print('\n')

print("Tuple Count 5")
x = thistuple.count(5)
print(x)
print('\n')

print("Tuple Index 8")
y = thistuple.index(8)
print(y)
print('\n')

#Set
print("Set")
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset.add("orange")
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset.remove("banana")
print(thisset)

for x in thisset:
  print(x)
print('\n')

#Dictionaries
print("Dictionaries")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
thisdict["year"] = 2018
thisdict["color"] = "red"
thisdict.pop("model")
print(thisdict)
print(thisdict["brand"])
print(type(thisdict))

thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)

for x in thisdict:
    try:
        print(x)
    except:
        print("An exception occurred")