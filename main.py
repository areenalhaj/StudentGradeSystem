import string


def count_class_members(taken_dict):
    return len(taken_dict)

def calc_average(taken_dict):
    count = count_class_members(taken_dict)
    if count == 0:
        return 0
    grades_sum = 0
    for std_name in taken_dict:
        grades_sum += taken_dict[std_name]
    average = grades_sum/count
    return average

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

def lowest_grade(taken_dict):
    if count_class_members(taken_dict)!=0:
        lowest = 100
        for std_name in taken_dict:
            grade = taken_dict[std_name]
            if grade < lowest:
                lowest = taken_dict[std_name]
                lowest_name = std_name
        return lowest
    else:
        return 0

def highest_and_lowest_grade(taken_dict):
    if count_class_members(taken_dict)!=0:
        lowest = 100
        highest = 0
        for std_name in taken_dict:
            grade = taken_dict[std_name]
            if grade < lowest:
                lowest = taken_dict[std_name]
            if grade > highest:
                highest = taken_dict[std_name]
        return [highest, lowest]
    else:
        return 0

def find_stds(grade, taken_dict):
    name = []
    for key, val in taken_dict.items():
        if val == grade:
            name.append(key)
    if len(name) == 0:
        return "No students"
    else:
        return name

def top_student(taken_dict):
    grade = highest_grade(taken_dict)
    find_stds(grade, taken_dict)


def performance(grade):
    if(grade>=90 and grade<=100):
        return "Excellent"
    if(grade>=75 and grade<=89):
        return "Good"
    else:
        return "Needs Improvement"

print("Welcome to this Student Grade Management System.")
print()
check = "go on"
data_dict = {}
while(check != "stop"):
    name = input("Enter student name (or type 'done' to finish): ")
    if name == "done":
        check= "stop"
    else:
        grade = float(input("Enter Ali's grade: "))
        data_dict[name]=grade


# count_class_members(data_dict)
# calc_average(data_dict)

# highest_grade(data_dict)
# lowest_grade(data_dict)
# highest_and_lowest_grade(data_dict)
# top_student(data_dict)

print(f"""Class Performance Report
------------------------
Total Students:{count_class_members(data_dict)}
Average Grade: {round(calc_average(data_dict), 2)}
Highest Grade: {highest_grade(data_dict)} ({", ".join(find_stds(highest_grade(data_dict),data_dict))})
Lowest Grade: {lowest_grade(data_dict)} ({", ".join(find_stds(lowest_grade(data_dict),data_dict))})
""")

performance(90)