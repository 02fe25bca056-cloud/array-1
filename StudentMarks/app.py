def get_student_details():
    print("=== Student Course Marks ===")

    name = input("Enter student name: ")
    program = input("Enter program: ")
    semester = input("Enter semester: ")
    courses = []
    count = int(input("How many courses? "))
    for i in range(count):
        course = input("Enter course name: ")
        marks = float(input("Enter marks: "))
        courses.append((course, marks))
    print("\n===== STUDENT INFORMATION =====")
    print("Name:", name)
    print("Program:", program)
    print("Semester:", semester)
    print("\nRegistered Courses and Marks:")
    low_marks = []
    for course, marks in courses:
        if marks < 50:
            print(f"WARNING: {course}: {marks:g} - BELOW 50")
            low_marks.append(course)
        else:
            print(f"{course}: {marks:g}")
    print("\nCourses scoring below 50:")
    if low_marks:
        for course in low_marks:
            print("-", course)
    else:
        print("No courses scored below 50.")
if __name__ == "__main__":
    get_student_details()