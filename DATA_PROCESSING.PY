def calculate_average(students):
    """Calculate average marks of all students."""
    if not students:
        print("No students available.")
        return None
    total = sum(s["marks"] for s in students)
    avg = total / len(students)
    print(f"Average Marks: {avg:.2f}")
    return avg

def find_topper(students):
    """Find student with highest marks."""
    if not students:
        return None
    topper = max(students, key=lambda s: s["marks"])
    print(f" Topper: {topper['name']} with {topper['marks']} marks")
    return topper
