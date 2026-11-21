import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def run_analysis(filename="students.csv"):
  print("\n================ DATA ANALYSIS REPORT ================")
  df = pd.read_csv(filename)

  # Handle missing values
  df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
  df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")
  df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
  df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

  print("\n--- Top 5 Records (Selected Columns) ---")
  print(df[["Roll_No", "Name", "Marks"]].head(5))

  print("\n--- High Scorers (Marks > 75, Sorted) ---")
  top_students = df[df["Marks"] > 75].sort_values(by="Marks", ascending=False)
  print(top_students[["Name", "Branch", "Marks"]].head(10))

  print("\n--- Branch-wise Average Marks (GroupBy) ---")
  branch_avg = df.groupby("Branch")["Marks"].mean()
  print(branch_avg)

  print("\n--- Statistical Summary ---")
  print(df[["Marks", "Attendance"]].describe())

  # NumPy operations
  marks_1d = np.array(df["Marks"])
  data_2d = np.array(df[["Marks", "Attendance"]])

  print("\n--- NumPy Calculations ---")
  print("First 5 Marks (1D Slicing):", np.round(marks_1d[:5], 2))
  print("First 2 Rows (2D Array):\n", np.round(data_2d[:2], 2))
  print(f"Total Sum: {np.sum(marks_1d):.2f} | Mean: {np.mean(marks_1d):.2f}")
  print(f"Max: {np.max(marks_1d):.2f} | Min: {np.min(marks_1d):.2f}")
  print(f"Standard Deviation: {np.std(marks_1d):.2f}")

  # Graph (Bar Chart)
  branch_avg.plot(
      kind="bar", color=["#4CAF50", "#2196F3", "#FF9800", "#E91E63"]
  )
  plt.title("Branch-wise Average Marks")
  plt.xlabel("Branch")
  plt.ylabel("Average Marks")
  plt.xticks(rotation=0)
  plt.show()