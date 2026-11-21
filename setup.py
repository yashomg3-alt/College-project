import csv
import random

branches = ["CSE", "IT", "ECE", "ME"]
with open("students.csv", "w", newline="") as f:
  writer = csv.writer(f)
  writer.writerow(["Roll_No", "Name", "Branch", "Marks", "Attendance"])
  for i in range(1, 51):
    marks = "" if i in [10, 25] else random.randint(45, 98)
    att = random.randint(60, 100)
    writer.writerow(
        [100 + i, f"Student_{i}", random.choice(branches), marks, att]
    )
print("Done! students.csv file generated successfully.")