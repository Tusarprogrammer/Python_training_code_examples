# functions in python
'''
f(x) = x+10
f(1) = 1+10 = 11
f(2) = 2+10 = 12
'''

# line no 8 to 10 is called the method definition
def my_function():
    print("Hello People , Good morning")
    print("Today is a holiday!!")

print("Calling my function for the first time")
my_function() # function call/invocation statement
print("Calling my function for the second time")
my_function()

def display_my_family():
    print("==================My Family Details below===================")
    print("My name is Akash")
    print("My father's name is Rajesh")
    print("My mother's name is Madhu")
    print("My Grandpa's name is Rakesh")
    print("My Grandma's name is Radha")
    print("My Sister's name is Priya")
    print("My Brother's name is Suresh")

display_my_family()

def add_two_nos(param1,param2):
    print("Sum of passed Params is below for ",param1,", ",param2)
    print(param1+param2)

add_two_nos(10,20)

#add_two_nos(10)

def add_three_nos(first_number=10, second_number=20, third_number=30): # default values/parameters
    print("Sum of passed Params is below for ",first_number,", ",second_number,", ",third_number)
    print(first_number + second_number + third_number)

add_three_nos()

add_three_nos(1,2)

add_three_nos(1)

add_three_nos(1,1,1)


# function to check if a provided number is even or odd
def check_no_is_even_or_odd(input_number):
    if input_number%2 == 0:
        print(input_number,"is an even number")
    else:
        print(input_number,"is an odd number")


check_no_is_even_or_odd(10)

check_no_is_even_or_odd(11)

# function with a return value

def get_full_name(first_name, middle_name, last_name):
    #return first_name + " " +middle_name + " " +last_name
    return first_name + middle_name + last_name


full_name = get_full_name("Manoj", "Kumar", "Patnaik")

print(full_name)

def sum_of_4_nos(first_number, second_number, third_number, fourth_number):
    return first_number + second_number + third_number + fourth_number

print(sum_of_4_nos(1,2,3,4))

# Arbitrary arguments
print("============Arbitrary arguments=============")
def sum_of_n_nos(*passed_numbers):
    sum = 0
    for param in passed_numbers:
        #print(param)
        sum = sum+param
    return sum

sum1 = sum_of_n_nos(1,2,3)
print("Sum 1 is ")
print(sum1)

sum2 = sum_of_n_nos(1,2,22,333,45,567,55,23423,234324,24324,243324,1231,23423)











