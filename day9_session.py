dict_for_student = {"name":"Sawan",
        "age":20,
        "qualification":"BTech",
        "address":"patia, bbsr",
        "phone":"2342424",
        "home_phone":"7657868989"
        }

print (dict_for_student['name'])
print (dict_for_student['age'])
print (dict_for_student['qualification'])
print (dict_for_student['address'])
print (dict_for_student['phone'])
print (dict_for_student['home_phone'])

print (dict_for_student.get('name'))
print (dict_for_student.get('age'))
print (dict_for_student.get('qualification'))
print (dict_for_student.get('address'))
print (dict_for_student.get('phone'))
print (dict_for_student.get('home_phone'))


dict_for_employee = {"name":"Sawan",
        "age":20,
        "qualification":"BTech",
        "address":"patia, bbsr",
        "phone":"2342424",
        "home_phone":"7657868989",
                     "employee_id":"EMP-10",
                     "salary":"10000",
                     "date_of_joining":"30-07-2022",
                     "designation":"director",
                     "office_location":"Bhubaneswar"
        }

print (dict_for_employee.get('name'))
print (dict_for_employee.get('age'))
print (dict_for_employee.get('qualification'))
print (dict_for_employee.get('address'))
print (dict_for_employee.get('phone'))
print (dict_for_employee.get('home_phone'))
print (dict_for_employee.get('employee_id'))
print (dict_for_employee.get('salary'))
print (dict_for_employee.get('date_of_joining'))
print (dict_for_employee.get('designation'))
print (dict_for_employee.get('office_location'))

print (dict_for_student)
dict_for_student['name'] = "Sawan Kumar Rathore"

print (dict_for_student)

dict_for_student.update({"State":"Odisha"})
dict_for_student.update({"Country":"India"})

print (dict_for_student)

dict_for_student['address'] = "Barmunda, Bhubaneswar"
dict_for_student.update({"Aadhar":"6565-6666-6666-4678"})
print (dict_for_student)

print (len(dict_for_student))


print ("===========================================================================================")

del dict_for_student['home_phone']

print (len(dict_for_student))

print (dict_for_student)

#dict_for_student.clear() # clears the dictionary data but the dictionary exists
print (dict_for_student)
print (len(dict_for_student))
print ("=================================================")
for item in dict_for_student:
    print(item)


for item in dict_for_student:
    print(dict_for_student[item])
print ("Displaying key value in a single loop")
for (key,value) in dict_for_student.items():
    print(key,":",value)


for (a,b) in dict_for_student.items():
    print(a,":",b)

semester = {"physics":50,
        "chemistry":80,
        "Maths":80,
        "computer":60,
        "english":66
        }

total_subjects = len(semester)

print (total_subjects)
total_marks = 0

for item in semester:
    total_marks += semester[item]
    #print(dict_for_student[item])
print (total_marks)

percentage = (total_marks/(total_subjects*100))*100
print ("percentage scored in the semester is below")
print (percentage)