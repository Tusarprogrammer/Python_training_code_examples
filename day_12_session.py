# File handling in python

# Read the content of a file in python

file_path = "mydatafile.txt"

file_obj = open(file_path,"r") # r is called read mode

print("==============File Content is diplayed below====================")
print(file_obj.read())
file_obj.close()

file_obj = open(file_path,"r") # r is called read mode

print("==============File Content upto certain character====================")
print(file_obj.read(10))
file_obj.close()

print("==============Python Readline=====================")

file_path = "students_list.txt"
file_obj = open(file_path,"r") # r is called read mode

#print(file_obj.readline())
#print(file_obj.readline())
for student in file_obj:
    print(student)
file_obj.close()

# check if a student present in the file


file_obj = open(file_path,"r") # r is called read mode

#print(file_obj.readline())
#print(file_obj.readline())
search_student = "Raghu"
is_present = True
for student in file_obj:
    if student.strip("\n") == search_student:
        print(search_student,"is present")
        is_present = False
    #print(student)
if(is_present):
    print(search_student, "is absent")
file_obj.close()

# File writing in Python

# => a =-> Append mode
# => w => Write mode


file_path = "store_data.txt"
file_obj = open(file_path,"a") # a is called append mode
file_obj.write("\nGood day!!")
file_obj.close()


file_path = "store_data.txt"
file_obj = open(file_path,"w") # w is called write mode
file_obj.write("\nGood day!!")
file_obj.close()

source_file_path = "source_file.txt"
source_file_obj = open(source_file_path,"r") # r is called read mode

destination_file_path = "destination_file.txt"
destination_file_obj = open(destination_file_path,"w") # w is called write mode
destination_file_obj.write(source_file_obj.read())


source_file_obj.close()
destination_file_obj.close()




