import analytics
import data_ops


def main():
  while True:
    students = data_ops.load_data()
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Display All Records")
    print("2. Add New Record")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Generate Summary Report (NumPy & Pandas)")
    print("7. Exit")

    choice = input("Enter choice (1-7): ")

    if choice == "1":
      data_ops.display_all(students)
    elif choice == "2":
      data_ops.add_student(students)
    elif choice == "3":
      data_ops.search_student(students)
    elif choice == "4":
      data_ops.update_student(students)
    elif choice == "5":
      data_ops.delete_student(students)
    elif choice == "6":
      analytics.run_analysis()
    elif choice == "7":
      print("Goodbye!")
      break
    else:
      print("Invalid choice!")


if __name__ == "__main__":
  main()