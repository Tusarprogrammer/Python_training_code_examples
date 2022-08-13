# Python Tuple

# Another built-in data type

#======================================================================

names_tuple = ("Ram","Madhu","Naveen")
#names_tuple[0] = "Krishna"
print(type(names_tuple))
print(names_tuple)

names_list = ["Ram","Madhu","Naveen"]
names_list[0] = "Krishna" # I am changing the list
print(type(names_list))
print(names_list)

#=======================================================================

names_tuple = ("Ram","Madhu","Naveen")
#names_tuple[0] = "Krishna"
names_tuple_converted_to_list = list(names_tuple)
names_tuple_converted_to_list[0] = "Krishna"
names_tuple = tuple(names_tuple_converted_to_list)
print(type(names_tuple))
print(names_tuple)

#=====================================================================

print(len(names_tuple))

#=====================================================================

first_tuple = ("a","b","c")
second_tuple = ("d","e","f")
print(first_tuple+second_tuple) # Merging of tuples

#=====================================================================

#Unpacking tuples

data_tuple = ("Mango","Banana","Apple")

(first_fruit,second_fruit,third_fruit) = data_tuple

print(first_fruit)
print(second_fruit)
print(third_fruit)

#=====================================================================

#indexing of tuples
print("=============Indexing====================")
data_tuple = ("Mango","Banana","Apple")

print(data_tuple[1])
print(data_tuple[-1])
print(data_tuple[-2])
print(data_tuple[-3])
print(data_tuple[0])

#=====================================================================


thisset = {"apple", "banana", "cherry"}
print(thisset)
print(thisset[0])

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)















