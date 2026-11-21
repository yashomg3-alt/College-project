import csv

VALID_BRANCHES = ("CSE", "IT", "ECE", "ME")


def load_data(filename="students.csv"):
  students = []
  with open(filename, mode="r", newline="") as file:
    for row in csv.DictReader(file):
      students.append(row)
  return students


def save_data(students, filename="students.csv"):
  fields = ["Roll_No", "Name", "Branch", "Marks", "Attendance"]
  with open(filename, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)


def add_student(students):
  roll = input("Enter Roll No: ")
  name = input("Enter Name: ")
  branch = input(f"Enter Branch {VALID_BRANCHES}: ").upper()
  if branch not in VALID_BRANCHES:
    branch = "CSE"
  marks = input("Enter Marks: ")
  att = input("Enter Attendance (%): ")
  students.append({
      "Roll_No": roll,
      "Name": name,
      "Branch": branch,
      "Marks": marks,
      "Attendance": att,
  })
  save_data(students)
  print("Record added!")


def display_all(students):
  branches_present = set()
  print("\n--- All Student Records ---")
  for s in students:
    branches_present.add(s["Branch"])
    print(
        f"Roll: {s['Roll_No']} | Name: {s['Name']} | Branch: {s['Branch']} |"
        f" Marks: {s['Marks']} | Att: {s['Attendance']}%"
    )
  print(f"\nUnique Branches (Set): {branches_present}")


def search_student(students):
  roll = input("Enter Roll No to search: ")
  for s in students:
    if s["Roll_No"] == roll:
      print("Found:", s)
      return
  print("Student not found.")


def update_student(students):
  roll = input("Enter Roll No to update: ")
  for s in students:
    if s["Roll_No"] == roll:
      s["Marks"] = input("Enter new Marks: ")
      s["Attendance"] = input("Enter new Attendance: ")
      save_data(students)
      print("Record updated!")
      return
  print("Student not found.")


def delete_student(students):
  roll = input("Enter Roll No to delete: ")
  for i, s in enumerate(students):
    if s["Roll_No"] == roll:
      students.pop(i)
      save_data(students)
      print("Record deleted!")
      return
  print("Student not found.")