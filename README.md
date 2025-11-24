# STUDENT GRADE MANAGEMENT

## OVERVIEW

The Student Grade Management System is an application developed to assist Teachers, Schools, and Students in managing academic performance. The system allows Student Marks to be stored, processed, and analyzed effectively by recording, updating, and retrieving results with minimal effort.

## FEATURES

1. Managing Student Information


Register additional students


Modify or remove student information


Maintain student record details like ID, name, class, and section




2. Grades Entry & Processing


Enter marks for a number of subjects


Automatically calculate:


Total marks


Percentage


Grade (A, B, C, etc)


Pass/Fail status





3. Report Generation


Individual report cards


Class summary performance report


Subject-wise highest, lowest and average marks




4. Search & Retrieve


Find students by ID, name or class




View historical performance report records

## TECHNOLOGY AND TOOLS USED 

1. Functional Testing

1.1 Test Adding a Student

Steps:

1. Run the project.


2. In the menu, click on “Add Student”.


3. Sample details:

Name

Roll number

Marks in each subject



4. Save the record.



Expected result:

The student submission should be visible in the storage file - CSV/JSON/DB.

No error message should be displayed.

The program should confirm successful insertion.



---
 If you want more of these types of posts, please let me know in the comments.

1.2 Test Viewing All Students

Steps:

1. Add at least 3–5 student records.


2. Click "View All Students".



Expected result:

All records seem correct.

The columns visible are Roll Number, Name, Marks, Total, Percentage, Grade.

No missing or corrupted data.



---

1.3 Test Updating a Student

Steps:

1. Select "Update Student Details".


2. Enter an existing roll number.


3. Change marks or name.



Expected result:

Updated values are appropriately stored.

Old values are replaced.

System confirms the update.



---

1.4 Test Deleting a Student

Steps:

1. Select "Delete Student".


2. Enter the Roll Number of an already enrolled student.



Expected result:

That record needs to be removed from CSV/JSON/DB.

The list of students should not show that entry anymore.



---

1.5 Test Calculating Grades

Steps:

1. Enter marks for 5 subjects.


2. Check:

Total = the sum of all marks

Percentage = Total / No. of Subjects

Grade according to percentage




Expected result: Grade should match the defined grading logic.

Example:

≥ 90 → A

80–89 → B

70–79 → C

60–69 → D



< 60 → F

---
# TESTING INSTRUCTION

2.1 Test Marks Range

Try entering:

Negative marks

Marks above 100


Non-numeric input

Expected result:

System should prevent invalid entries.



Show appropriate message: “Invalid input for marks.”

---

2.2 Test Missing Fields

Leave fields empty or enter blank spaces.

Expected outcome:

Program should prompt for valid input.



No empty record should be added.

---

2.3 Duplicate Roll Number Test

Add two students of the same roll number.

Expected result:

System should detect duplicates.



Reject or overwrite depending on design - mention in output.

---

3. File / Database Testing

3.1 CSV/JSON File Check

After adding students:

Open the file manually.

Verify that all fields are stored correctly.


Ensure no corrupted or incomplete entries.

3.2 Checking SQLite Database

Using SQLite browser / command line:

Check if tables are created.



Verify that rows are inserted, updated, and deleted correctly.

---

4. Menu Navigation Testing

Steps:


1. Input invalid menu choices (example: 9, 0, letters)



2. Just press Enter without input

Expected outcome:

System should display: "Invalid choice. Please try again."



Program should not crash.

---

5. Performance Testing (Small-scale)

Steps:


1. Add 50–100 sample student entries.

2. Test:

Viewing list

Searching




Calculating Grades

Expected result:

The system should respond without lag.



No data loss.

---

6. Chart Testing (If charts are implemented)

Directions:

1. Create:

Grade distribution

Marks comparison



Trend charts



2. Check graphs display correctly.

expected result:

Proper axes labeling



Correct data mapping

---

7. Error Handling Testing

Manually try to cause errors:

Enter text where numbers are expected

Delete record that does not exist


Update an empty database


Expected result: Program should display appropriate messages and keep on running safely.

---

8. Final User Acceptance Testing UAT

Let another person test the system.

Checklist:

Easy to navigate

Clear instructions

Correct calculation

No program crashes Useful output

# SCREENSHOT

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/22bfe19f-0fec-4e16-bf16-356d0c5d6ee6" />


