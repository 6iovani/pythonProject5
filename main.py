#Giovani Martins

#open txt file, read lines, split into list, assign strings into dictionary
def load_data():
    student_file = open("students.txt", "r")
    student_lines = student_file.readlines()
    student_data = []
    for line in student_lines:
        line = line.strip()
        line = line.split("|")
        student_dictionary = {'name': line[0],
                              'id': line[1],
                              'credits': line[2],
                              'gpa': line[3]}
        student_data.append(student_dictionary)
    return student_data
#prompt user screen
def print_menu():
    print("----Please select from the following----")
    print("[1] add a student")
    print("[2] find masters students")
    print("[3] find students on probation")
    print("[4] find honors students")
    print("[5] Quit")
    print("=================================================")


def perform_command(choice):
#add student
    student_data = load_data()
    if choice == "1":
        student_name = input("What is the student's name?:")
        student_number = int(input(f"What is {student_name}'s id number?:"))
        student_credits = int(input(f"What is {student_name}'s credits?:"))
        student_gpa = float(input(f"What is {student_name}'s gpa?:"))
        new_student_data = {
            'name': student_name,
            'id': student_number,
            'credits': student_credits,
            'gpa': student_gpa
        }
        student_data.append(new_student_data)
#find master students
    elif choice == "2":
        student_credits = student_data[2]
        for credit in student_data:
            if int(credit['credits']) < 25:
                master_student = credit['name']
                print(master_student)
#find probation students
    elif choice == "3":
        student_gpa = student_data[3]
        for gpa in student_data:
            if float((gpa['gpa'])) < 2.0:
                probation_student = gpa['name']
                print(probation_student)
#find honnor students
    elif choice == "4":
        student_gpa = student_data[3]
        for gpa in student_data:
            if float((gpa['gpa'])) > 3.0:
                honor_student = gpa['name']
                print(honor_student)
#end program
    elif choice == "5":
        exit(0)
#run program
def main():
    student_data = load_data()
    while True:
        print_menu()
        user_selection = input("Your choice 1-4:")
        perform_command(user_selection)
main()
