"""
Perform the following SQL queries on the Students table:
1. Retrieve every single column and row from the table to see all our current data.
2. Retrieve the list of student names and their corresponding majors only.
3. Retrieve all details for students who have a GPA of 3.5 or strictly higher.
4. List of all names and GPAs for students specifically majoring in 'Computer Science'.
5. Retrieve all students, but order the list from the highest GPA to the lowest GPA.
6. Find the single student with the absolute highest GPA in the university.
7. Enroll Edward Norton as a Drama major with a 3.4 GPA. Assign him ID number 5.
8. Bob Jones realized Mathematics isn't for him. Change his major to 'Data Science'.
9. Charlie Brown (id: 3) has transferred to a different university. Remove his record from the database entirely.
10. After all the insertions and deletions above, we need to know exactly how many students are currently enrolled.
"""

students = [
    {"id": 1, "name": "Alice Smith", "major": "Computer Science", "gpa": 3.8},
    {"id": 2, "name": "Bob Jones", "major": "Mathematics", "gpa": 3.2},
    {"id": 3, "name": "Charlie Brown", "major": "Physics", "gpa": 2.9},
    {"id": 4, "name": "Diana Prince", "major": "Computer Science", "gpa": 3.9},
]

def print_section(title, data):
    print(f"\n{'='*55}\n{title}\n{'-'*55}")
    if isinstance(data, list):
        if not data:
            print("   (No records found)")
        for item in data:
            if isinstance(item, dict):
                formatted = ", ".join(
                    f"{k.capitalize()}: {v}" for k, v in item.items()
                )
                print(f"  * {formatted}")
            else:
                print(f"  * {item}")
    elif isinstance(data, dict):
        formatted = ", ".join(f"{k.capitalize()}: {v}" for k, v in data.items())
        print(f"  * {formatted}")
    else:
        print(f"  * {data}")

print_section("1. ALL STUDENTS IN DATABASE", students)

names_and_majors = [
    {"name": s["name"], "major": s["major"]} for s in students
]
print_section("2. STUDENT NAMES & MAJORS", names_and_majors)

high_gpa = [s for s in students if s["gpa"] >= 3.5]
print_section("3. HIGH ACHIEVERS (GPA >= 3.5)", high_gpa)

cs_students = [
    {"name": s["name"], "gpa": s["gpa"]}
    for s in students
    if s["major"] == "Computer Science"
]
print_section("4. COMPUTER SCIENCE MAJORS", cs_students)

sorted_students = sorted(students, key=lambda s: s["gpa"], reverse=True)
print_section("5. RANKED BY GPA (DESCENDING)", sorted_students)

top_student = max(students, key=lambda s: s["gpa"])
print_section("6. TOP STUDENT IN UNIVERSITY", top_student)

students.append(
    {"id": 5, "name": "Edward Norton", "major": "Drama", "gpa": 3.4}
)
print_section("7. AFTER ENROLLING EDWARD NORTON", students)

for s in students:
    if s["name"] == "Bob Jones":
        s["major"] = "Data Science"
print_section("8. AFTER UPDATING BOB JONES TO DATA SCIENCE", students)

students = [s for s in students if s["id"] != 3]
print_section("9. AFTER REMOVING CHARLIE BROWN (ID: 3)", students)

print_section("10. TOTAL CURRENTLY ENROLLED STUDENTS", len(students))