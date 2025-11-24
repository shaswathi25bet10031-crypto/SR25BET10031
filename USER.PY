students = []

def add_student(name, marks):
    """Add a student with name and marks."""
    student = {"name": name, "marks": marks}
    students.append(student)
    print(f"✅ Added student: {name}")

def list_students():
    """List all students."""
    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Marks: {s['marks']}")
    return students

def remove_student(name):
    """Remove a student by name."""
    global students
    students = [s for s in students if s["name"] != name]
    print(f"❌ Removed student: {name}")
