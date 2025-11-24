def generate_report(students, average, topper):
    """Generate a simple report."""
    print("\n=== Student Report ===")
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {average:.2f}" if average else "No average available")
    if topper:
        print(f"Topper: {topper['name']} ({topper['marks']} marks)")
    print("\nPerformance Summary:")
    for s in students:
        status = "Pass" if s["marks"] >= 40 else "Fail"
        print(f"{s['name']} - {status}")
