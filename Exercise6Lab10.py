"""Write a program that displays the list of exams passed by a student, with their marks.
There is a file, classes.txt, which contains the names of all the courses provided in
the educational institution (a US college), the content of which will look like this:
CSC1
CSC2
CSC46
CSC151
MTH121
...
Then, for each course, a file is available (whose name is equal to the course code
followed by .txt) which lists the students who passed the related exam and contains the student identification numbers
(ID) and grades, such as this, which could be the
CSC2.txt file:
11234 A–
12547 B
16753 B+
21886 C
...
Write a program that asks the user for the identification (ID) of a student and
displays the list of exams that that student has passed, with the relative marks
obtained, as in this example:
Student ID 16753
CSC2 B+
MTH121 C+
CHN1 A
PHY50 A–
(7.28 M)"""

FILENAME = "classes.txt"
OSERROR = "OSError Opening File: "

def open_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except OSError as problem:
        print(f"{OSERROR}{problem}")
        exit(1)

def invalid(student_id):
    return False

def ask_for_student_id():
    student_id = input("Insert Identification Number: ")
    if invalid(student_id):
        print("Invalid Identification Number. Try again")
        return ask_for_student_id()
    return student_id

def data_base(filename):
    data = {}
    courses = open_file(filename)
    for course in courses:
        scores = open_file(f"{course}.txt")
        course_scores = []
        for score in scores:
            tupl = score.split()
            course_scores.append((tupl[0], tupl[1]))
        data[course] = course_scores
    return data

def search_id(data, student_id):
    print_string = f"{student_id}\n"
    for course in data:
        for i in data[course]:
            if i[0] == student_id:
                print_string = print_string + f"{course} " + i[1] + "\n"
    return print_string

def main():
    student_id = ask_for_student_id()
    data = data_base(FILENAME)
    print(search_id(data, student_id))


if __name__ == '__main__':
    main()
