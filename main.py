# Functions:
# This function counts class members number
def count_class_members(taken_dict):
    return len(taken_dict)

# This function calculates the average of students grades
def calc_average(taken_dict):
    count = count_class_members(taken_dict)
    if count == 0:
        return 0
    grades_sum = 0
    for std_name in taken_dict:
        grades_sum += taken_dict[std_name]
    average = grades_sum/count
    return round(average, 2)

# This function finds the highest grade in the dictionary
def highest_grade(taken_dict):
    if count_class_members(taken_dict)!=0:
        highest = 0
        for std_name in taken_dict:
            grade = taken_dict[std_name]
            if grade > highest:
                highest = taken_dict[std_name]
        return highest
    else:
        return 0

# This function finds the lowest grade in the dictionary
def lowest_grade(taken_dict):
    if count_class_members(taken_dict)!=0:
        lowest = 100
        for std_name in taken_dict:
            grade = taken_dict[std_name]
            if grade < lowest:
                lowest = taken_dict[std_name]
        return lowest
    else:
        return 0

# This function finds the list of students who got the given grade
def find_stds(grade, taken_dict):
    name = []
    for key, val in taken_dict.items():
        if val == grade:
            name.append(key)
    if len(name) == 0:
        return "No students"
    else:
        return name

# This function finds the top student who got thee highest grade
def top_student(taken_dict):
    grade = highest_grade(taken_dict)
    find_stds(grade, taken_dict)

# This function finds the level of the given grade:
# "Excellent": (90-100) , "Good": (75-89), or "Needs improvement": (less than 75)
def performance(grade):
    if(grade>=90 and grade<=100):
        return "Excellent"
    if(grade>=75 and grade<=89):
        return "Good"
    else:
        return "Needs Improvement"

# This function checks if the input data type is numeric
def check_if_num(message):
    while True:
        data = input(message)
        try:
            number = float(data)
            return number
        except ValueError:
            print("Invalid grade value, enter a float or integer.")

# *******************
# Program starts here:
# *******************
print("Welcome to this Student Grade Management System.")
# Entering data:
check = "go on"
data_dict = {}
while(check != "stop"):
    name = input("Enter student name (or type 'done' to finish): ")
    if name == "done":
        check= "stop"
    else:
        grade = check_if_num("Enter student grade: ")
        data_dict[name]=grade
# Report:
# 1-Calculating and collecting needed data for the report:
std_num = count_class_members(data_dict)
grades_av = calc_average(data_dict)
highest = highest_grade(data_dict)
lowest = lowest_grade(data_dict)
highest_stds = ", ".join(find_stds(highest_grade(data_dict),data_dict))
lowest_stds = ", ".join(find_stds(lowest_grade(data_dict),data_dict))

# 2-Printing the report:
print(14*"\n")
print(f"""Class Performance Report
------------------------
Total Students: {std_num}
Average Grade: {grades_av}
Highest Grade: {highest} ({highest_stds})
Lowest Grade: {lowest} ({lowest_stds})
""")

print("Performance Breakdown:")
for std_name in data_dict:
    print(f"{std_name} - {data_dict[std_name]} ({performance(data_dict[std_name])})")