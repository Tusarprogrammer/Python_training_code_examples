#Python for object oriented programming

# Python classes and objects

# A class is a blue print to create object

class Employee1:
    name = "Ram"
    id = "2022ID1"
    address = "RaghunathPur"
    mobile = "67587689986"
    email = "ram@gmail.com"

#create object of this class

Object1 = Employee1()
print(Object1.name,Object1.id,Object1.address,Object1.mobile,Object1.email)

Object2 = Employee1()
print(Object2.name,Object2.id,Object2.address,Object2.mobile,Object2.email)

#class with __init_() method
print("=============================Class with __init__() method ==================================")
class Employee:
    def __init__(self,name,id, address,mobile,email):
        print("Hi I am __init__() method ",name)
        self.name = name
        self.id = id
        self.address = address
        self.mobile = mobile
        self.email = email
    def displayEmployee(self):
        print(self.name,self.email,self.mobile,self.id,self.address)

first_employee = Employee("Madhu","2022#1","Bhubaneswar","654765687678","Madhu@gmail.com")
print("Displaying employee data")
first_employee.displayEmployee()



print("Before Object modification")
print(first_employee.name,first_employee.id,first_employee.address,first_employee.mobile,first_employee.email)

first_employee.name = "Pavan Kumar"
first_employee.mobile = "66666666666666"
first_employee.email = "Myemail@gmail.com"
#del first_employee.email
#del first_employee
print("After Object modification")
print(first_employee.name,first_employee.id,first_employee.address,first_employee.mobile,first_employee.email)

second_employee = Employee("Rajesh","2022#2","Balasore","325525325","Rajesh@gmail.com")

print(second_employee.name,second_employee.id,second_employee.address,second_employee.mobile,second_employee.email)

second_employee = Employee("Rajesh","2022#2","Balasore","325525325","Rajesh@gmail.com")

print(second_employee.name,second_employee.id,second_employee.address,second_employee.mobile,second_employee.email)


class MathOpearations:
    def __init__(self, first_param, second_param):
        self.first_param = first_param
        self.second_param = second_param

    def add(self):
        return self.first_param+self.second_param

    def multi(self):
        return self.first_param * self.second_param

    def subtractio(self):
        return self.first_param - self.second_param

    def division(self):
        return self.first_param / self.second_param

    def modularDiv(self):
        return self.first_param % self.second_param

mathObj = MathOpearations(10,20)
print(mathObj.add())
print(mathObj.multi())


'''
Basics 

Data structures
List//array
Dictionary
Tuple
set

Functions
lamda

File handling

class, objects, object oriented programming

'''