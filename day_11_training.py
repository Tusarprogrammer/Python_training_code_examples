#keyword argument

def sum_of_4_nos(second_number, third_number, fourth_number,first_number):
    if(fourth_number == 2):
        return first_number + second_number + third_number + fourth_number
    elif(fourth_number == 1):
        return first_number * second_number * third_number * fourth_number


print(sum_of_4_nos(1,2,3,4))

print(sum_of_4_nos(first_number=1,fourth_number=2,third_number=3,second_number=4))
print(sum_of_4_nos(fourth_number=1,third_number=3,second_number=4,first_number=1))

print("=========================================================")
def get_full_name(first_name, second_name, last_name):
    DELIMETER = " "
    return first_name+DELIMETER+second_name+DELIMETER+last_name

print(get_full_name(first_name="Mr", second_name="Rajesh", last_name="Patnaik"))

print(get_full_name(second_name="Rajesh", first_name="Mr", last_name="Patnaik"))

print(get_full_name(last_name="Patnaik", second_name="Rajesh", first_name="Mr"))

#================Python Lambda=======================================

# => A small anonymous function
# => It has one expression and it can take any number of arguments
print("===========Running Lambda function===================")

# Lambda function expression
this_is_my_lambda = lambda my_number : my_number + 1000

print(this_is_my_lambda(10))

add_two_numbers = lambda param1,param2 : param1 + param2
print(add_two_numbers(10,50))

print(add_two_numbers(1000,50000))

#check_the_number=lambda param1:param1
#if param%2==0
check_if_a_number_is_even = lambda input_number : input_number%2 == 0

print(check_if_a_number_is_even(10))

print(check_if_a_number_is_even(11))

# 4 input parameters and check if their sum is greater than 100 and divisible by 2

check_if_sum_of_4_greter_than_100_and_div_by_2 = \
    lambda param1,param2,param3,param4 : \
    (param1+param2+param3+param4)>100 and (param1+param2+param3+param4)%2==0

print(check_if_sum_of_4_greter_than_100_and_div_by_2(40,50,60,40))

print(check_if_sum_of_4_greter_than_100_and_div_by_2(31,51,60,41))














