import os
import json

# ------------------- File Paths -------------------
COURSE_FILE = "courses.json"
STUDENT_FILE = "students.json"

# ------------------- File Handling -------------------
def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return {}

def save_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

# ------------------- Initialize Data -------------------
courses = load_data(COURSE_FILE)
students = load_data(STUDENT_FILE)

# ------------------- Course CRUD Operations -------------------
def add_course():
    cid = input("Enter Course ID: ")
    if cid in courses:
        print("Course already exists!")
        return
    name = input("Enter Course Name: ")
    duration = input("Enter Duration: ")
    fees = input("Enter Fees: ")
    courses[cid] = {
        "name": name,
        "duration": duration,
        "fees": fees
    }
    save_data(COURSE_FILE, courses)
    print("Course added successfully!")

def view_courses():
    if not courses:
        print("No courses available.")
        return
    print("\n--- Course List ---")
    for cid, info in courses.items():
        print(f"{cid} | {info['name']} | {info['duration']} | Fees: {info['fees']}")

def update_course():
    cid = input("Enter Course ID to update: ")
    if cid not in courses:
        print("Course not found!")
        return
    courses[cid]["name"] = input("Enter new course name: ")
    courses[cid]["duration"] = input("Enter new duration: ")
    courses[cid]["fees"] = input("Enter new fees: ")
    save_data(COURSE_FILE, courses)
    print("Course updated successfully!")

def delete_course():
    cid = input("Enter Course ID to delete: ")
    if cid in courses:
        del courses[cid]
        save_data(COURSE_FILE, courses)
        print("Course deleted successfully!")
    else:
        print("Course not found!")

# ------------------- Student CRUD Operations -------------------
def add_student():
    sid = input("Enter Student ID: ")
    if sid in students:
        print("Student already exists!")
        return
    name = input("Enter Student Name: ")
    email = input("Enter Student Email: ")
    students[sid] = {
        "name": name,
        "email": email,
        "enrolled_courses": {},
        "progress": {}
    }
    save_data(STUDENT_FILE, students)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students available.")
        return
    print("\n--- Student List ---")
    for sid, info in students.items():
        print(f"\nID: {sid}, Name: {info['name']}, Email: {info['email']}")
        if info["enrolled_courses"]:
            print(" Enrolled Courses:")
            for cid, cname in info["enrolled_courses"].items():
                prog = info["progress"].get(cid, 0)
                print(f"  - {cname} ({prog}%)")
        else:
            print(" No enrolled courses.")

def update_student():
    sid = input("Enter Student ID to update: ")
    if sid not in students:
        print("Student not found!")
        return
    students[sid]["name"] = input("Enter new name: ")
    students[sid]["email"] = input("Enter new email: ")
    save_data(STUDENT_FILE, students)
    print("Student updated successfully!")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    if sid in students:
        del students[sid]
        save_data(STUDENT_FILE, students)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

# ------------------- Enrollment & Progress -------------------
def enroll_student():
    sid = input("Enter Student ID: ")
    if sid not in students:
        print("Student not found!")
        return

    cid = input("Enter Course ID: ")
    if cid not in courses:
        print("Course not found!")
        return

    if cid in students[sid]["enrolled_courses"]:
        print("Student already enrolled in this course!")
        return

    students[sid]["enrolled_courses"][cid] = courses[cid]["name"]
    students[sid]["progress"][cid] = 0
    save_data(STUDENT_FILE, students)
    print("Student enrolled successfully!")

def update_progress():
    sid = input("Enter Student ID: ")
    if sid not in students:
        print("Student not found!")
        return

    cid = input("Enter Course ID: ")
    if cid not in students[sid]["enrolled_courses"]:
        print("Student not enrolled in this course!")
        return

    try:
        progress = int(input("Enter progress (0-100): "))
        if 0 <= progress <= 100:
            students[sid]["progress"][cid] = progress
            save_data(STUDENT_FILE, students)
            print("Progress updated successfully!")
        else:
            print("Progress must be between 0 and 100.")
    except ValueError:
        print("Invalid input! Enter a number.")

# ------------------- Main Menu -------------------
def main_menu():
    while True:
        print("\n=== Online Course Enrollment System ===")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Add Student")
        print("6. View Students")
        print("7. Update Student")
        print("8. Delete Student")
        print("9. Enroll Student")
        print("10. Update Progress")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            view_courses()
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            add_student()
        elif choice == "6":
            view_students()
        elif choice == "7":
            update_student()
        elif choice == "8":
            delete_student()
        elif choice == "9":
            enroll_student()
        elif choice == "10":
            update_progress()
        elif choice == "0":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# ------------------- Run Program -------------------
if __name__ == "__main__":
    main_menu()
