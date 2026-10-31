students = {
"S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
"S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
"S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
"S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
"S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}},
}
def calculate_total(marks):
    mark=marks.values()
    return sum(mark)
def calculate_average(marks):
    sum=calculate_total(marks)
    avg=round(sum/(len(marks)),2)
    return avg
def get_grade(average):
    if(average>=90):
        return 'A'
    elif(average>=75 and average<90):
        return 'B'
    elif(average>=60 and average<75):
        return 'C'
    elif(average>=40 and average<60):
        return 'D'
    else: return 'F'

def check_result(marks,pass_mark=40):
    mark=marks.values()
    res=[]
    res=list(filter(lambda mk: mk<pass_mark,mark))
    if (len(res)!=0):
        return 'Fail'
    else:
        return 'Pass'
def student_summary(student):
    st_summ={}
    st_summ['name']=student['name']
    st_summ['total']=calculate_total(student['marks'])
    st_summ['average']=calculate_average(student['marks'])
    st_summ['grade']=get_grade(st_summ['average'])
    st_summ['result']=check_result(student['marks'])
    return st_summ

def add_student(data,student_id,name,**marks):
    ids=data.keys()
    if(student_id not in ids):
        data[student_id]={'name':name,'marks':marks}
        return True
    else:
        return False

def update_marks(data,student_id,**changes):
    ids=data.keys()
    subs=changes.keys()
    if(student_id in ids):
        for i in subs:
            data[student_id]['marks'][i]=changes[i]
        return True
    else:
        return False

def remove_student(data,student_id):
    ids=data.keys()
    if(student_id in ids): 
        data.pop(student_id)
        return True
    else:
        return False      

def print_report(data):
    result_list = []

    for student_id, student in data.items():
        average = calculate_average(student["marks"])
        result_list.append((average, student_id))

    result_list.sort(reverse=True)

    print(f"{'ID':<6}{'Name':<8}{'Total':<6}{'Avg':<8}{'Grade':<7}  Result")
    print("-" * 42)

    for average, student_id in result_list:
        summary = student_summary(data[student_id])

        print(
            f"{student_id:<6}"
            f"{summary['name']:<8}"
            f"{summary['total']:<6}"
            f"{summary['average']:<8.2f}"
            f"{summary['grade']:<7}  "
            f"{summary['result']}"
        )



def class_statistics(data, *subjects):
    total_pass = 0
    highest_average = -1
    topper = ""

    subject_totals = {}
    subject_averages = {}

    if len(subjects) == 0:
        subjects = tuple(data[list(data.keys())[0]]["marks"].keys())

    for subject in subjects:
        subject_totals[subject] = 0

    for student in data.values():

        marks = student["marks"]
        average = calculate_average(marks)
        result = check_result(marks)

        if result == "Pass":
            total_pass = total_pass + 1

        if average > highest_average:
            highest_average = average
            topper = student["name"]

        for subject in subjects:
            subject_totals[subject] = subject_totals[subject] + marks[subject]

    for subject in subjects:
        subject_averages[subject] = round(
            subject_totals[subject] / len(data), 1
        )

    pass_percentage = round((total_pass / len(data)) * 100, 1)

    return {
        "topper": topper,
        "pass_percentage": pass_percentage,
        "subject_averages": subject_averages
    }



def main():



    print("Task 1: One student")

    print(student_summary(students["S101"]))

    print(check_result(students["S102"]["marks"]))
    print(check_result(students["S102"]["marks"], pass_mark=35))
    print(check_result(students["S102"]["marks"], 35))




    print("\nTask 2: Report")

    print_report(students)



    print("\nTask 3: Update marks")

    print(update_marks(students, "S102", Maths=55))

    print(update_marks(students, "S999", Maths=60))

    corrections = {"Python": 50, "Stats": 58}

    print(update_marks(students, "S102", **corrections))

    print(student_summary(students["S102"]))




    print("\nTask 4: Add student")

    print(add_student(students, "S106", "Farhan",
                      Python=70, Maths=35, Stats=74))

    print(add_student(students, "S101", "Zara",
                      Python=80, Maths=80, Stats=80))

    print(students["S106"])




    print("\nTask 5: Remove student")

    print(remove_student(students, "S104"))

    print(remove_student(students, "S104"))

    print(len(students))


  

    print("\nTask 6: Final report and statistics")

    print_report(students)

    stats = class_statistics(students)

    print("Topper:", stats["topper"])

    print("Pass percentage:", stats["pass_percentage"])

    print("Subject averages:", stats["subject_averages"])

    stats = class_statistics(students, "Python", "Stats")

    print("Python and Stats only:", stats["subject_averages"])




main()

     
    

    