print("This is my third python program")
print("\n") # new line characher
# This is an inline comment in poython
print("python is very simple to learn")
print("we can do procedural,functional,object oriented programming in pyton")
print("python is an indented programming lanmguage")
print("heloooo")

"""
Hello 
This is a multi line comment

"""

# comment 1
# comment 2
# comment 3

first_variable = 10
second_variable = 20

sum = first_variable+second_variable

print("sum is", sum)


print("sum is",first_variable+second_variable)

x = 10
print(type(x))
x = "hello"
print(type(x))

x = 'hello'
print(type(x))

x, y, z = "Orange", "Banana", "Cherry"

print(x,y,z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z)

x = 5
y = "John"
#print(x + y)

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


a = "Hello, World!"
print(a[1])

#looping through a string
for x in "banana":
  print(x)


#length of a string
a = "Hello, World!"
print(len(a))

#check if a string is present
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#string slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
a = "Hello"
b = "World"
c = a + b
print(c)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))



x = [y for y in range(10)]

print(x)

z = [p+2 for p in x]
print(z)
print("helloooooooooooo")
z = [p+2 if p==0 else p+1 for p in x if p%2==0]
print(z)

for a in range(10):
    print(a)

abc = range(10)
print("abc")
print(abc)

