#==========Python Set built-in data type

data_set = {"bbsr","brpr","sbpr","blsr","rkl"} # [], (), {}

print(type(data_set))
print(data_set)

#print(data_set)

#print(data_set)

#print(data_set)

data_set = {1,2,3,4,5}
data_set = {"1","2","3","4","5"}
print(data_set)

#With duplicates
data_set = {"1","2","3","4","5","1","2","4","4"}
print(data_set)
print(len(data_set))

data_cities = {"Cuttack","Bhubaneswar","Jajpur","Baleswar","Sambalpur","Rourkela",
               "Cuttack","Bhubaneswar","Jajpur","Baleswar","Sambalpur","Rourkela","Koraput"}
print(len(data_cities))

print("====================Adding element into a set in python================================")

india_cities = {"Delhi","Mumbai"}

india_cities.add("Chennai")
print(india_cities)

character_set = {"A"}
character_set.add("B")
character_set.add("C")
character_set.add("D")
character_set.add("E")
print(character_set)
print(type(character_set))

print("========Python Program to update set with list data=========")

set_data = {"A","B","C"}

list_data = ["D","E","F","A","B"]

set_data.update(list_data)
print(set_data)

print("========Python Program to update set with another set data=========")

set_data = {"A","B","C"}

another_set_data = {"D","E","F","A","B"}

set_data.update(another_set_data)
print(set_data)


print("========Python Program to update set with another tuple data=========")

set_data = {"A","B","C"}

another_tuple_data = ("D","E","F","A","B")

set_data.update(another_tuple_data)
print(set_data)

print("===================Finding common elements between 2 sets================")

set1 = {"A","B","C"}
set2 = {"A","B","D","E"}

for item in set2:
    for item1 in set1:
        if item==item1:
            print(item)


set3 = set1.difference(set2)
print(set3)
set3 = set1.intersection(set2)
print(set3)

set3 = set1.union(set2)
print(set3)



dict = {"name":"Sawan",
        "age":20,
        "qualification":"BTech",
        "address":"patia, bbsr",
        "phone":"2342424"
        }
print(dict)
print(dict.keys())
print(dict.values())

















